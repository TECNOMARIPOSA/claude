import os, json, glob, sys
from PIL import Image

EB = '/tmp/claude-0/-home-user-claude/3f280c0c-aac6-5fb1-b584-e0838e3758c8/scratchpad/eb'
REPO = '/home/user/claude/OUTPUTS/calma-en-colores-ebook'
OUT = EB + '/book'
os.makedirs(OUT + '/thumbs', exist_ok=True)
cover_art = sys.argv[1]

cfgs = {}
for p in sorted(glob.glob(REPO + '/herramientas/cfg/*.json')):
    c = json.load(open(p)); cfgs[os.path.basename(p)[:-5]] = c
slugs = sorted(cfgs)
assert len(slugs) == 65, len(slugs)
themes = [
    ('Postales del mundo', slugs[0:20], 'Lugares famosos para viajar con el pincel', 'tematica-1-postales-del-mundo'),
    ('Flores y jardines', slugs[20:45], 'Un jardín de color para cada día', 'tematica-2-flores-y-jardines'),
    ('Animales', slugs[45:65], 'Compañeros de calma, de la sabana al hogar', 'tematica-3-animales'),
]
# page map
FRONT = 6   # cover, intro, how-to, 3 index pages
start = {}
page = FRONT
div_page = []
for ti, (_, sl, _, _) in enumerate(themes):
    page += 1; div_page.append(page)
    for s in sl:
        start[s] = page + 1; page += 3
closing_page = page + 1
TOTAL = closing_page
json.dump(dict(start=start, div=div_page, closing=closing_page, total=TOTAL), open(OUT + '/map.json', 'w'))


def color_src(slug):
    n = slug[:2]
    if n == '01': return EB + '/out4/color_page.png'
    if n == '02': return EB + '/out6/color_page.png'
    return EB + '/work/%s/color_page.png' % slug


def thumb(slug, w=420):
    p = OUT + '/thumbs/%s.jpg' % slug
    if not os.path.exists(p):
        im = Image.open(color_src(slug)).convert('RGB'); im.thumbnail((w, int(w * 1.25))); im.save(p, quality=88)
    return p


def pagethumb(slug, k, w=520):
    ext = 'jpg' if k < 3 else 'png'
    nm = ['pagina-1-presentacion', 'pagina-2-referencia-color', 'pagina-3-colorear-numerado'][k - 1]
    tdir = [t for t in themes if slug in t[1]][0][3]
    p = OUT + '/thumbs/%s-p%d.jpg' % (slug, k)
    if not os.path.exists(p):
        im = Image.open('%s/%s/%s/%s.%s' % (REPO, tdir, slug, nm, ext)).convert('RGB'); im.thumbnail((w, int(w * 1.42))); im.save(p, quality=88)
    return p


CSS = '''
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,400;1,9..144,500&family=Inter:wght@300;400;500;600;700&display=swap');
:root{--olive:#7d7f52;--olive-deep:#5c5e3a;--olive-wash:#eceedd;--cream:#f7f3e6;--cream-lt:#fffdf6;--orange:#eba46b;--orange-deep:#c06f35;--peach:#fdeedd;--ink:#2e2f24;--soft:#6b6c5b;--line:#e3dfcd;}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:794px;height:1123px;background:#fff;font-family:'Inter',sans-serif;color:var(--ink);}
.page{width:794px;height:1123px;position:relative;overflow:hidden;background:var(--cream-lt);}
.frame{position:absolute;inset:26px;border:2px solid var(--orange);border-radius:22px;}
.frame:after{content:'';position:absolute;inset:7px;border:1px solid var(--line);border-radius:16px;}
.eyebrow{font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--olive);font-weight:700;}
h1,h2{font-family:'Fraunces',serif;font-weight:500;color:var(--ink);letter-spacing:-.012em;}
h2 em,h1 em{font-style:italic;color:var(--orange-deep);}
.rule{width:64px;height:2px;background:linear-gradient(90deg,transparent,var(--orange),transparent);margin:14px auto;}
.brandline{position:absolute;left:0;right:0;bottom:52px;text-align:center;font-family:'Fraunces',serif;font-style:italic;font-size:15px;color:var(--orange-deep);}
/* cover */
.cover{background:var(--cream);}
.cover .art{position:absolute;inset:0;background-size:cover;background-position:center;}
.cover .panel{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:430px;padding:40px 24px 34px;text-align:center;background:rgba(255,253,246,.94);border-radius:200px / 150px;border:2px solid var(--orange);box-shadow:0 20px 50px -20px rgba(92,94,58,.5);}
.cover h1{font-size:54px;line-height:1.02;margin:12px 0 4px;}
.cover .tag{font-family:"Fraunces",serif;font-style:italic;font-size:17px;color:var(--olive-deep);}
.cover .chips{display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin-top:18px;}
.cover .chips span{font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;font-weight:600;color:var(--olive-deep);background:var(--olive-wash);border:1px solid var(--line);padding:6px 11px;border-radius:50px;}
.cover .num{display:inline-block;margin-top:16px;background:var(--orange);color:var(--ink);font-weight:700;font-size:13px;letter-spacing:.08em;padding:9px 20px;border-radius:50px;text-transform:uppercase;}
/* generic content */
.wrap{position:absolute;left:70px;right:70px;top:78px;}
.head{text-align:center;margin-bottom:26px;}
.head h2{font-size:38px;margin-top:10px;}
.lead{font-size:14.5px;line-height:1.7;color:var(--soft);}
.lead b{color:var(--ink);}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:26px;}
.card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px;text-align:center;box-shadow:0 14px 30px -22px rgba(92,94,58,.5);}
.card .tt{display:grid;grid-template-columns:repeat(3,1fr);gap:5px;margin-bottom:12px;}
.card .tt img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:7px;display:block;}
.card h3{font-family:'Fraunces',serif;font-weight:600;font-size:18px;}
.card .n{font-size:30px;font-family:'Fraunces',serif;color:var(--orange-deep);font-weight:600;line-height:1.1;margin-top:4px;}
.card p{font-size:12px;color:var(--soft);margin-top:4px;line-height:1.45;}
.big{margin-top:22px;text-align:center;background:var(--peach);border:1px solid #f3d9bd;border-radius:16px;padding:16px 22px;font-size:14px;line-height:1.6;}
.big b{color:var(--orange-deep);}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}
.step{text-align:center;}
.step img{width:100%;border-radius:10px;border:1px solid var(--line);box-shadow:0 14px 28px -20px rgba(46,47,36,.5);display:block;}
.step .no{display:inline-flex;width:30px;height:30px;border-radius:50%;background:var(--orange);color:var(--ink);font-weight:700;align-items:center;justify-content:center;margin:12px 0 6px;font-family:'Fraunces',serif;font-size:16px;}
.step h3{font-family:'Fraunces',serif;font-size:16px;font-weight:600;}
.step p{font-size:11.5px;color:var(--soft);line-height:1.5;margin-top:3px;}
.tips{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:24px;}
.box{border-radius:16px;padding:16px 18px;}
.box.o{background:var(--olive-wash);border:1px solid var(--line);}
.box.p{background:var(--peach);border:1px solid #f3d9bd;}
.box h4{font-family:'Fraunces',serif;font-size:16px;font-weight:600;margin-bottom:8px;color:var(--olive-deep);}
.box.p h4{color:var(--orange-deep);}
.box ul{list-style:none;}
.box li{font-size:12px;line-height:1.5;padding:4px 0 4px 14px;position:relative;color:var(--ink);}
.box li:before{content:'';position:absolute;left:0;top:11px;width:6px;height:6px;border-radius:50%;background:var(--orange);}
/* index */
.ix{margin-top:6px;}
.ix a{display:flex;align-items:baseline;gap:8px;text-decoration:none;color:var(--ink);padding:6px 4px;border-bottom:1px dotted #d9d4bd;}
.ix a .no{font-family:'Fraunces',serif;font-weight:600;color:var(--orange-deep);width:30px;font-size:15px;}
.ix a .t{font-size:14px;font-weight:500;flex:0 1 auto;}
.ix a .s{font-size:11px;color:var(--soft);font-style:italic;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.ix a .p{font-family:'Fraunces',serif;font-weight:600;font-size:15px;color:var(--olive-deep);min-width:30px;text-align:right;}
/* divider */
.div{background:radial-gradient(ellipse at 50% 0%,rgba(125,127,82,.16),transparent 60%),var(--cream-lt);text-align:center;}
.div .big1{font-family:'Fraunces',serif;font-size:150px;font-weight:500;color:var(--orange);line-height:1;margin-top:110px;}
.div h1{font-size:54px;margin-top:6px;}
.div .sub{font-family:'Fraunces',serif;font-style:italic;font-size:20px;color:var(--olive-deep);margin-top:10px;}
.div .count{display:inline-block;margin-top:20px;background:var(--olive-wash);border:1px solid var(--line);border-radius:50px;padding:8px 20px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--olive-deep);}
.div .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:46px 80px 0;}
.div .grid img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:10px;border:4px solid #fff;box-shadow:0 14px 28px -18px rgba(46,47,36,.55);display:block;}
/* closing */
.close{text-align:center;background:radial-gradient(ellipse at 50% 100%,rgba(235,164,107,.2),transparent 60%),var(--cream-lt);}
.close h1{font-size:46px;margin-top:150px;line-height:1.1;}
.close p{max-width:520px;margin:20px auto 0;font-size:15px;line-height:1.75;color:var(--soft);}
.close .grid{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;margin:44px 70px 0;}
.close .grid img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:8px;display:block;}
'''


def page_html(cls, body):
    return '<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body><div class="page %s">%s</div></body></html>' % (CSS, cls, body)


pages = {}
# 1 cover
pages['p001'] = page_html('cover', '''<div class="art" style="background-image:url('file://%s')"></div>
<div class="panel"><div class="eyebrow">Pintura por números antiestrés</div><h1>Calma<br>en colores</h1><div class="rule"></div>
<div class="tag">65 ilustraciones para pintar con calma</div>
<div class="chips"><span>Postales del mundo</span><span>Flores y jardines</span><span>Animales</span></div></div>''' % cover_art)

# 2 welcome
cards = ''
for name, sl, hook, _ in themes:
    ts = ''.join('<img src="file://%s">' % thumb(s) for s in sl[:3])
    cards += '<div class="card"><div class="tt">%s</div><h3>%s</h3><div class="n">%d</div><p>ilustraciones<br>%s</p></div>' % (ts, name, len(sl), hook)
pages['p002'] = page_html('', '''<div class="frame"></div><div class="wrap">
<div class="head"><div class="eyebrow">Bienvenida</div><h2>Gracias por darte <em>este momento</em></h2><div class="rule"></div></div>
<p class="lead" style="text-align:center">Este ebook reúne <b>65 ilustraciones</b> para pintar por números, pensadas para que bajes el ritmo, desconectes del celular y disfrutes de un rato solo para ti. No necesitas experiencia: <b>eliges un color, sigues los números y te dejas llevar.</b></p>
<div class="cards">%s</div>
<div class="big">Cada ilustración tiene <b>3 páginas</b>: una presentación con datos curiosos y música sugerida, una referencia a color con su paleta numerada y la lámina para colorear con números. En total, <b>195 páginas</b> para pintar.</div>
</div><div class="brandline">Calma en colores</div>''' % cards)

# 3 how to
s0 = slugs[0]
pages['p003'] = page_html('', '''<div class="frame"></div><div class="wrap">
<div class="head"><div class="eyebrow">Cómo usar tu ebook</div><h2>Tres páginas, <em>un solo ritual</em></h2><div class="rule"></div></div>
<div class="steps">
<div class="step"><img src="file://%s"><div class="no">1</div><h3>Descubre</h3><p>Conoce el lugar, la flor o el animal, sus datos curiosos y la música sugerida.</p></div>
<div class="step"><img src="file://%s"><div class="no">2</div><h3>Elige tus colores</h3><p>Mira la ilustración a color y su paleta numerada. Es una guía: puedes cambiar los colores.</p></div>
<div class="step"><img src="file://%s"><div class="no">3</div><h3>Pinta por números</h3><p>Cada número de la lámina corresponde al mismo número de la paleta.</p></div></div>
<div class="tips">
<div class="box o"><h4>Materiales</h4><ul><li>Lápices, marcadores o lápices acuarelables: usa lo que tengas.</li><li>Si usas acuarela u otra pintura con agua, imprime en papel grueso apto para pintura.</li><li>Para enmarcar tu obra, elige un papel de mejor calidad.</li></ul></div>
<div class="box o"><h4>Impresión</h4><ul><li>Imprime en cualquier papel A4 o A3.</li><li>Puedes imprimir por partes: solo las páginas que vayas a pintar.</li><li>En una copistería, cuenta con qué vas a pintar y te recomendarán el papel.</li></ul></div>
<div class="box p"><h4>Tu ritual</h4><ul><li>Prepara una bebida caliente y enciende una vela si quieres.</li><li>Pon la música sugerida de cada ilustración.</li><li>Bastan 20 minutos: sin prisa y lejos del celular.</li></ul></div>
<div class="box p"><h4>Para recordar</h4><ul><li>Tienes acceso ilimitado: reimprime las láminas todas las veces que quieras.</li><li>Puedes empezar por la ilustración que más te llame la atención.</li><li>No hay colores correctos: lo importante es disfrutar.</li></ul></div></div>
</div><div class="brandline">Calma en colores</div>''' % (pagethumb(s0, 1), pagethumb(s0, 2), pagethumb(s0, 3)))

# 4-6 index
links = {}
for ti, (name, sl, hook, _) in enumerate(themes):
    rows = ''
    for s in sl:
        c = cfgs[s]
        rows += '<a data-slug="%s"><span class="no">%s</span><span class="t">%s</span><span class="s">· %s</span><span class="p">%d</span></a>' % (s, c['num'], c['title'], c['sub'], start[s])
    pages['p%03d' % (4 + ti)] = page_html('', '''<div class="frame"></div><div class="wrap">
<div class="head" style="margin-bottom:12px"><div class="eyebrow">Índice · Colección %d</div><h2>%s</h2><div class="rule"></div></div>
<div class="ix">%s</div></div><div class="brandline">Calma en colores</div>''' % (ti + 1, name, rows))

# dividers + closing
for ti, (name, sl, hook, _) in enumerate(themes):
    g = ''.join('<img src="file://%s">' % thumb(s) for s in sl[:4])
    pages['p%03d' % div_page[ti]] = page_html('div', '''<div class="frame"></div><div class="eyebrow" style="margin-top:78px">Colección</div>
<div class="big1" style="margin-top:20px">%d</div><h1>%s</h1><div class="sub">%s</div><div class="count">%d ilustraciones · %d páginas</div>
<div class="grid">%s</div><div class="brandline">Calma en colores</div>''' % (ti + 1, name, hook, len(sl), len(sl) * 3, g))
import random
random.seed(7)
pick = [slugs[i] for i in (0, 5, 22, 30, 47, 58)]
g = ''.join('<img src="file://%s">' % thumb(s) for s in pick)
pages['p%03d' % closing_page] = page_html('close', '''<div class="frame"></div><div class="eyebrow" style="margin-top:78px">Hasta pronto</div>
<h1>Gracias por pintar<br><em>con calma</em></h1><div class="rule"></div>
<p>Esperamos que cada página te haya regalado un momento tranquilo. Vuelve a imprimir tus láminas favoritas y pinta con otros colores: una misma ilustración puede ser distinta cada vez.</p>
<div class="grid">%s</div><div class="brandline">Calma en colores · Pintura por números antiestrés</div>''' % g)

for k, h in pages.items():
    open('%s/%s.html' % (OUT, k), 'w').write(h)
print(len(pages), 'pages; total', TOTAL, '; closing', closing_page, '; div', div_page)
