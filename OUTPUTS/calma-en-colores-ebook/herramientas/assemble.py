import os, json, glob, io
from PIL import Image, ImageDraw, ImageFont
import img2pdf
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link

EB = os.getcwd(); REPO = '/home/user/claude/OUTPUTS/calma-en-colores-ebook'
B = EB + '/book'; F = B + '/final'; os.makedirs(F, exist_ok=True)
mp = json.load(open(B + '/map.json')); links = json.load(open(B + '/links.json'))
cfgs = {os.path.basename(p)[:-5]: json.load(open(p)) for p in glob.glob(REPO + '/herramientas/cfg/*.json')}
slugs = sorted(cfgs)
themes = [('tematica-1-postales-del-mundo', slugs[0:20]), ('tematica-2-flores-y-jardines', slugs[20:45]), ('tematica-3-animales', slugs[45:65])]
TOTAL = mp['total']
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 34)

seq = []   # (page_no, src_path, kind)
for n in range(1, 8): seq.append((n, '%s/p%03d.png' % (B, n), 'front'))
page = 7
for ti, (d, sl) in enumerate(themes):
    if ti > 0:
        page += 1; seq.append((page, '%s/p%03d.png' % (B, mp['div'][ti]), 'front'))
    for s in sl:
        for k, (nm, ext) in enumerate([('pagina-1-presentacion', 'jpg'), ('pagina-2-referencia-color', 'jpg'), ('pagina-3-colorear-numerado', 'png')], 1):
            page += 1; seq.append((page, '%s/%s/%s/%s.%s' % (REPO, d, s, nm, ext), 'ill%d' % k))
page += 1; seq.append((page, '%s/p%03d.png' % (B, mp['closing']), 'front'))
assert page == TOTAL, (page, TOTAL)
# sanity: start map matches
for s, st in mp['start'].items():
    assert any(p == st and ('/%s/' % s) in src for p, src, _ in seq), s

def stamp(im, n, gray):
    d = ImageDraw.Draw(im); W, H = im.size
    d.text((W - 150, H - 46), str(n), font=font, fill=(110 if gray else (138, 138, 122)), anchor='rm')
    return im

full, light = [], []
for n, src, kind in seq:
    im = Image.open(src)
    if kind == 'ill3':
        im = im.convert('L')
        if n != 1: stamp(im, n, True)
        p = '%s/f%03d.png' % (F, n); im.save(p, dpi=(300, 300), optimize=True); full.append(p)
        lim = im.resize((1240, 1754), Image.LANCZOS).convert('L'); lp = '%s/l%03d.jpg' % (F, n); lim.save(lp, quality=82, dpi=(150, 150)); light.append(lp)
        continue
    im = im.convert('RGB')
    if n != 1: stamp(im, n, False)
    if kind == 'ill1' or kind == 'ill2':
        big = im.resize((1654, 2339), Image.LANCZOS)
    else:
        big = im
    p = '%s/f%03d.jpg' % (F, n); big.save(p, quality=86, dpi=(200 if big.size[0] < 2000 else 300,) * 2); full.append(p)
    lim = im.resize((1240, 1754), Image.LANCZOS); lp = '%s/l%03d.jpg' % (F, n); lim.save(lp, quality=80, dpi=(150, 150)); light.append(lp)
print('pages', len(full))

A4 = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
lay = img2pdf.get_layout_fun(A4)

def build(files, out):
    data = img2pdf.convert(files, layout_fun=lay, title='Calma en colores - Pintura por números antiestrés', author='Calma en colores')
    r = PdfReader(io.BytesIO(data)); w = PdfWriter(); w.append(r)
    # outline
    w.add_outline_item('Portada', 0); w.add_outline_item('Bienvenida', 1); w.add_outline_item('Cómo usar tu ebook', 2)
    ix = w.add_outline_item('Índice', 3)
    names = ['Postales del mundo', 'Flores y jardines', 'Animales']
    for ti, (d, sl) in enumerate(themes):
        w.add_outline_item('Índice · ' + names[ti], 3 + ti, parent=ix)
    for ti, (d, sl) in enumerate(themes):
        par = w.add_outline_item('Colección %d · %s' % (ti + 1, names[ti]), mp['div'][ti] - 1)
        for s in sl:
            c = cfgs[s]; w.add_outline_item('%s · %s' % (c['num'], c['title']), mp['start'][s] - 1, parent=par)
    w.add_outline_item('Cierre', TOTAL - 1)
    # links
    sc = 595.276 / 794.0
    for key, rects in links.items():
        pi = int(key[1:]) - 1
        for rc in rects:
            x1 = rc['x'] * sc; x2 = (rc['x'] + rc['w']) * sc
            y2 = 841.89 - rc['y'] * sc; y1 = 841.89 - (rc['y'] + rc['h']) * sc
            w.add_annotation(page_number=pi, annotation=Link(rect=(x1, y1, x2, y2), target_page_index=mp['start'][rc['slug']] - 1))
    w.page_mode = '/UseOutlines'
    with open(out, 'wb') as f: w.write(f)
    print(out, round(os.path.getsize(out) / 1e6, 1), 'MB')

build(full, '/tmp/claude-0/-home-user-claude/3f280c0c-aac6-5fb1-b584-e0838e3758c8/scratchpad/eb/ebook_full.pdf')
build(light, '/tmp/claude-0/-home-user-claude/3f280c0c-aac6-5fb1-b584-e0838e3758c8/scratchpad/eb/ebook_light.pdf')
