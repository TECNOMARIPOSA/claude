import sys, json, os
import numpy as np, cv2
from scipy import ndimage as ndi
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw, ImageFont

src, outdir = sys.argv[1], sys.argv[2]
K = int(sys.argv[3]) if len(sys.argv) > 3 else 28
MIN_AREA = int(sys.argv[4]) if len(sys.argv) > 4 else 1500   # at working res
MIN_R = float(sys.argv[5]) if len(sys.argv) > 5 else 11.0     # min inscribed radius at working res

W = int(os.environ.get('SEG_W', 1150)); H = int(W * 1.25)   # working resolution (4:5)
FW, FH = 2300, 2875          # final line-art resolution (A4 @300dpi, with margins)
S = FW / W

img = cv2.imread(src)
img = cv2.resize(img, (W, H), interpolation=cv2.INTER_AREA)
flat = cv2.pyrMeanShiftFiltering(img, int(os.environ.get('SEG_SP', 8)), int(os.environ.get('SEG_SR', 16)))
lab = cv2.cvtColor(flat, cv2.COLOR_BGR2LAB).astype(np.float32)

rng = np.random.RandomState(0)
idx = rng.choice(W * H, 120000, replace=False)
km = KMeans(n_clusters=K, n_init=3, random_state=0).fit(lab.reshape(-1, 3)[idx])
L = km.predict(lab.reshape(-1, 3)).reshape(H, W).astype(np.int32)

kernel = np.ones((3, 3), np.uint8)


def majority(L, sigma):
    best = np.full(L.shape, -1.0, np.float32)
    out = L.copy()
    for k in np.unique(L):
        p = cv2.GaussianBlur((L == k).astype(np.float32), (0, 0), sigma)
        m = p > best
        best[m] = p[m]
        out[m] = k
    return out


L = majority(L, float(os.environ.get('SEG_S1', 3.0)))
L = majority(L, float(os.environ.get('SEG_S2', 2.0)))


def components(L):
    C = np.zeros_like(L)
    n = 0
    for lbl in np.unique(L):
        m, k = ndi.label(L == lbl)
        C[m > 0] = m[m > 0] + n
        n += k
    return C, n


for it in range(40):
    C, n = components(L)
    areas = ndi.sum(np.ones_like(C), C, index=np.arange(1, n + 1))
    # inscribed radius per component
    changed = 0
    order = np.argsort(areas)
    objs = ndi.find_objects(C)
    for ci in order:
        cid = ci + 1
        a = areas[ci]
        if a >= MIN_AREA * 6:
            continue
        sl = objs[ci]
        y0, y1 = max(sl[0].start - 4, 0), min(sl[0].stop + 4, H)
        x0, x1 = max(sl[1].start - 4, 0), min(sl[1].stop + 4, W)
        sub = (C[y0:y1, x0:x1] == cid)
        r = cv2.distanceTransform(sub.astype(np.uint8), cv2.DIST_L2, 3).max()
        if a >= MIN_AREA and r >= MIN_R:
            continue
        ring = cv2.dilate(sub.astype(np.uint8), kernel, iterations=2).astype(bool) & ~sub
        nb = L[y0:y1, x0:x1][ring]
        own = L[y0:y1, x0:x1][sub][0]
        nb = nb[nb != own]
        if nb.size == 0:
            continue
        vals, cnt = np.unique(nb, return_counts=True)
        dist = np.linalg.norm(km.cluster_centers_[vals] - km.cluster_centers_[own], axis=1)
        L[y0:y1, x0:x1][sub] = vals[np.argmax(cnt / (1.0 + dist / 12.0))]
        changed += 1
    print('pass', it, 'merged', changed, flush=True)
    if changed == 0:
        break

C, n = components(L)
print('regions', n, 'labels', len(np.unique(L)))

# final palette from mean source colour of each label (use the flattened image)
labels = np.unique(L)
remap = {l: i for i, l in enumerate(labels)}
Lr = np.vectorize(remap.get)(L)
cols = []
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32)
for i in range(len(labels)):
    cols.append(rgb[Lr == i].mean(axis=0))
cols = np.array(cols)
hsv = cv2.cvtColor(np.clip(cols, 0, 255).astype(np.uint8).reshape(-1, 1, 3), cv2.COLOR_RGB2HSV).reshape(-1, 3).astype(np.float32)
hsv[:, 1] = np.clip(hsv[:, 1] * 1.14, 0, 255)
hsv[:, 2] = np.clip(hsv[:, 2] * 1.03, 0, 255)
cols = cv2.cvtColor(hsv.astype(np.uint8).reshape(-1, 1, 3), cv2.COLOR_HSV2RGB).reshape(-1, 3).astype(np.float32)

# order palette: neutrals (low chroma) first by lightness desc, then by hue, lightness desc
labc = cv2.cvtColor(cols.reshape(-1, 1, 3).astype(np.uint8), cv2.COLOR_RGB2LAB).reshape(-1, 3).astype(float)
chroma = np.hypot(labc[:, 1] - 128, labc[:, 2] - 128)
hue = (np.degrees(np.arctan2(labc[:, 2] - 128, labc[:, 1] - 128)) + 360) % 360
hue_shift = (hue - 20) % 360     # warm tones (red/orange/yellow) first
neutral = chroma < 14
key = []
for i in range(len(cols)):
    if neutral[i]:
        key.append((0, -labc[i, 0], 0))
    else:
        key.append((1, int(hue_shift[i] // 45), -labc[i, 0]))
order = sorted(range(len(cols)), key=lambda i: key[i])
newnum = {old: k + 1 for k, old in enumerate(order)}   # number 1..N
N = np.vectorize(lambda v: newnum[v])(Lr)             # per-pixel palette number
pal = [{'n': newnum[i], 'hex': '#%02x%02x%02x' % tuple(int(round(c)) for c in cols[i])} for i in range(len(cols))]
pal.sort(key=lambda d: d['n'])
json.dump(pal, open(outdir + '/palette.json', 'w'))
np.save(outdir + '/N.npy', N.astype(np.uint8))

# preview of the quantised result (what the finished piece will look like)
q = np.zeros((H, W, 3), np.uint8)
for i in range(len(cols)):
    q[Lr == i] = cols[i].astype(np.uint8)
Image.fromarray(q).save(outdir + '/quantized.png')

# ---- line art at final resolution ----
line = np.full((FH, FW), 255, np.uint8)
C, n = components(Lr)
thick = int(os.environ.get('SEG_THICK', 4))
numbers = []
objs = ndi.find_objects(C)
for cid in range(1, n + 1):
    sl = objs[cid - 1]
    y0, y1, x0, x1 = sl[0].start, sl[0].stop, sl[1].start, sl[1].stop
    mloc = (C[y0:y1, x0:x1] == cid)
    sub = np.pad(mloc.astype(np.uint8), 1)
    cnts, _ = cv2.findContours(sub, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    for c in cnts:
        c = c.reshape(-1, 2).astype(np.float32) - 1
        if len(c) < 3:
            continue
        # light smoothing of the pixel staircase
        k = 9
        if len(c) > 2 * k:
            ker = np.ones(k) / k
            cx = np.convolve(np.r_[c[-k:, 0], c[:, 0], c[:k, 0]], ker, 'same')[k:-k]
            cy = np.convolve(np.r_[c[-k:, 1], c[:, 1], c[:k, 1]], ker, 'same')[k:-k]
            c = np.stack([cx, cy], 1)
        c = (c + [x0 + 0.5, y0 + 0.5]) * S
        cv2.polylines(line, [np.round(c * 16).astype(np.int32)], True, 0, thick, cv2.LINE_AA, shift=4)
    dt = cv2.distanceTransform(sub, cv2.DIST_L2, 5)[1:-1, 1:-1]
    r = dt.max()
    py, px = np.unravel_index(np.argmax(dt), dt.shape)
    numbers.append((int(N[y0:y1, x0:x1][mloc][0]), (px + x0 + 0.5) * S, (py + y0 + 0.5) * S, r * S))

Image.fromarray(line).save(outdir + '/lineart_free.png')

numimg = Image.fromarray(line).convert('L')
d = ImageDraw.Draw(numimg)
fp = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
for num, x, y, r in numbers:
    size = int(max(int(os.environ.get('SEG_MINFONT', 24)), min(48, r * 0.95)))
    f = ImageFont.truetype(fp, size)
    d.text((x, y), str(num), font=f, fill=40, anchor='mm')
numimg.save(outdir + '/lineart_numbered.png')
print('palette', len(pal), 'regions', len(numbers))
