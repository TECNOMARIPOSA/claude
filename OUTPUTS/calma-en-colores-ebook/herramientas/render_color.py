import sys, json, numpy as np, cv2
from PIL import Image
d = sys.argv[1]
N = np.load(d + '/N.npy'); pal = json.load(open(d + '/palette.json'))
H, W = N.shape; FW, FH = 2300, 2875
colors = {p['n']: tuple(int(p['hex'][i:i+2], 16) for i in (1, 3, 5)) for p in pal}
best = np.full((FH, FW), -1.0, np.float32); out = np.zeros((FH, FW, 3), np.uint8)
for n, c in colors.items():
    p = cv2.GaussianBlur((N == n).astype(np.float32), (0, 0), 1.4)
    p = cv2.resize(p, (FW, FH), interpolation=cv2.INTER_CUBIC)
    m = p > best; best[m] = p[m]; out[m] = c
Image.fromarray(out).save(d + '/color_page.png')
print('ok')
