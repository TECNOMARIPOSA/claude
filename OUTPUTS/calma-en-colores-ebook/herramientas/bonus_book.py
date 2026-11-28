"""Build a bonus PDF: cover + welcome/how-to + index + 3 pages per illustration + closing.
usage: python3 bonus_book.py config.json
config: key, title, subtitle, cover (png), work_prefix, cfg_dir, out_dir, out_pdf, intro (paragraph), what (list of 3 bullets)
"""
import os, sys, json, glob, io, subprocess
from PIL import Image, ImageDraw, ImageFont

EB = '/tmp/claude-0/-home-user-claude/3f280c0c-aac6-5fb1-b584-e0838e3758c8/scratchpad/eb'
conf = json.load(open(sys.argv[1]))
OUT = conf['out_dir']; os.makedirs(OUT + '/thumbs', exist_ok=True); os.makedirs(OUT + '/final', exist_ok=True)
cfgs = {os.path.basename(p)[:-5]: json.load(open(p)) for p in sorted(glob.glob(conf['cfg_dir'] + '/*.json'))}
slugs = sorted(cfgs); N = len(slugs)
start = {s: 4 + 3 * i for i, s in enumerate(slugs)}
TOTAL = 4 + 3 * N
css = open(EB + '/book/p002.html').read().split('<style>')[1].split('</style>')[0]


def work(s): return '%s/work/%s%s' % (EB, conf['work_prefix'], s)


def thumb(s, k=None):
    if k is None:
        p = '%s/thumbs/%s.jpg' % (OUT, s)
        if not os.path.exists(p):
            im = Image.open(work(s) + '/color_page.png').convert('RGB'); im.thumbnail((420, 525)); im.save(p, quality=88)
    else:
        p = '%s/thumbs/%s-p%d.jpg' % (OUT, s, k)
        if not os.path.exists(p):
            im = Image.open(work(s) + '/page%d.png' % k).convert('RGB'); im.thumbnail((520, 740)); im.save(p, quality=88)
    return p


def page(cls, body):
    return '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body><div class="page %s">%s</div></body></html>' % (css, cls, body)


s0 = slugs[0]
thumbs = ''.join('<img src="file://%s">' % thumb(s) for s in slugs)
extra = '''.grid10{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin-top:14px;width:86%;margin-left:7%;}
.steps .step img{width:66%;margin:0 auto;}
.steps .step p{font-size:11px;}
.step .no{margin:8px 0 4px;}
.lead{font-size:13.5px;line-height:1.6;}
.grid10 img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:8px;border:3px solid #fff;box-shadow:0 10px 20px -14px rgba(46,47,36,.55);display:block;}'''
pages = {}
pages['p002'] = page('', '''<style>%s</style><div class="frame"></div><div class="wrap" style="top:70px">
<div class="head" style="margin-bottom:14px"><div class="eyebrow">Tu bono de regalo</div><h2>%s</h2><div class="rule"></div></div>
<p class="lead" style="text-align:center">%s</p>
<div class="grid10">%s</div>
<div class="steps" style="margin-top:18px">
<div class="step"><img src="file://%s"><div class="no">1</div><h3>Descubre</h3><p>Conoce el tema, sus datos curiosos y la música sugerida.</p></div>
<div class="step"><img src="file://%s"><div class="no">2</div><h3>Elige tus colores</h3><p>Mira la ilustración y su paleta numerada. Puedes cambiar los colores.</p></div>
<div class="step"><img src="file://%s"><div class="no">3</div><h3>Pinta por números</h3><p>Cada número corresponde al mismo número de la paleta.</p></div></div>
<div class="tips" style="margin-top:14px"><div class="box o"><h4>Materiales e impresión</h4><ul><li>Imprime en papel A4 o A3, por partes si quieres.</li><li>Usa lápices, marcadores o lápices acuarelables.</li><li>Con acuarela, usa papel grueso apto para pintura.</li></ul></div>
<div class="box p"><h4>Para recordar</h4><ul><li>Acceso ilimitado: reimprime cuando quieras.</li><li>No hay colores correctos: lo importante es disfrutar.</li><li>Bastan 20 minutos para tu ritual.</li></ul></div></div>
</div><div class="brandline">Calma en colores</div>''' % (extra, conf['title'], conf['intro'], thumbs, thumb(s0, 1), thumb(s0, 2), thumb(s0, 3)))

rows = ''.join('<a data-slug="%s"><span class="no">%s</span><span class="t">%s</span><span class="s">· %s</span><span class="p">%d</span></a>' % (s, cfgs[s]['num'], cfgs[s]['title'], cfgs[s]['sub'], start[s]) for s in slugs)
pages['p003'] = page('', '''<div class="frame"></div><div class="wrap">
<div class="head" style="margin-bottom:16px"><div class="eyebrow">Índice</div><h2>%s</h2><div class="rule"></div></div>
<div class="ix">%s</div></div><div class="brandline">Calma en colores</div>''' % (conf['title'], rows))

pick = ''.join('<img src="file://%s">' % thumb(s) for s in slugs[:6])
pages['p%03d' % TOTAL] = page('close', '''<div class="frame"></div><div class="eyebrow" style="margin-top:78px">Hasta pronto</div>
<h1>Gracias por pintar<br><em>con calma</em></h1><div class="rule"></div>
<p>Esperamos que cada página te regale un momento tranquilo. Vuelve a imprimir tus láminas favoritas y pinta con otros colores: una misma ilustración puede ser distinta cada vez.</p>
<div class="grid">%s</div><div class="brandline">Calma en colores · %s</div>''' % (pick, conf['title']))

for k, h in pages.items(): open('%s/%s.html' % (OUT, k), 'w').write(h)
subprocess.run(['node', EB + '/render_book.js', OUT], check=True)
links = json.load(open(OUT + '/links.json'))

# cover: upscaled flat cover to A4
cov = Image.open(conf['cover']).convert('RGB')
W, H = 2480, 3508
sc = max(W / cov.size[0], H / cov.size[1]); cov = cov.resize((round(cov.size[0] * sc), round(cov.size[1] * sc)), Image.LANCZOS)
x = (cov.size[0] - W) // 2; y = (cov.size[1] - H) // 2
cov.crop((x, y, x + W, y + H)).save(OUT + '/p001.png')

font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 34)
def stamp(im, n, gray):
    d = ImageDraw.Draw(im); w, h = im.size
    d.text((w - 150, h - 46), str(n), font=font, fill=(110 if gray else (138, 138, 122)), anchor='rm')

seq = [(1, OUT + '/p001.png', 'front'), (2, OUT + '/p002.png', 'front'), (3, OUT + '/p003.png', 'front')]
pg = 3
for s in slugs:
    for k in (1, 2, 3):
        pg += 1; seq.append((pg, '%s/page%d.png' % (work(s), k), 'ill%d' % k))
pg += 1; seq.append((pg, '%s/p%03d.png' % (OUT, TOTAL), 'front'))
assert pg == TOTAL
full, light = [], []
for n, src, kind in seq:
    im = Image.open(src)
    if kind == 'ill3':
        im = im.convert('L'); stamp(im, n, True)
        im = im.point(lambda v: 255 if v > 200 else (0 if v < 90 else v))
        p = '%s/final/f%03d.png' % (OUT, n); im.save(p, dpi=(300, 300), optimize=True); full.append(p)
        lp = '%s/final/l%03d.jpg' % (OUT, n); im.resize((1240, 1754), Image.LANCZOS).save(lp, quality=82, dpi=(150, 150)); light.append(lp)
        continue
    im = im.convert('RGB')
    if n != 1: stamp(im, n, False)
    big = im.resize((1654, 2339), Image.LANCZOS) if kind in ('ill1', 'ill2') else im
    p = '%s/final/f%03d.jpg' % (OUT, n); big.save(p, quality=87, dpi=(200 if big.size[0] < 2000 else 300,) * 2); full.append(p)
    lp = '%s/final/l%03d.jpg' % (OUT, n); im.resize((1240, 1754), Image.LANCZOS).save(lp, quality=80, dpi=(150, 150)); light.append(lp)

import img2pdf
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
lay = img2pdf.get_layout_fun((img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297)))

def build(files, out):
    data = img2pdf.convert(files, layout_fun=lay, title=conf['title'] + ' - Calma en colores', author='Calma en colores')
    r = PdfReader(io.BytesIO(data)); w = PdfWriter(); w.append(r)
    w.add_outline_item('Portada', 0); w.add_outline_item('Bienvenida', 1); ix = w.add_outline_item('Índice', 2)
    for s in slugs: w.add_outline_item('%s · %s' % (cfgs[s]['num'], cfgs[s]['title']), start[s] - 1)
    w.add_outline_item('Cierre', TOTAL - 1)
    sc = 595.276 / 794.0
    for key, rects in links.items():
        pi = int(key[1:]) - 1
        for rc in rects:
            w.add_annotation(page_number=pi, annotation=Link(rect=(rc['x'] * sc, 841.89 - (rc['y'] + rc['h']) * sc, (rc['x'] + rc['w']) * sc, 841.89 - rc['y'] * sc), target_page_index=start[rc['slug']] - 1))
    w.page_mode = '/UseOutlines'
    with open(out, 'wb') as f: w.write(f)
    print(out, round(os.path.getsize(out) / 1e6, 1), 'MB', len(PdfReader(out).pages), 'pages')

build(full, conf['out_pdf']); build(light, conf['out_pdf'].replace('.pdf', '-ligero.pdf'))
