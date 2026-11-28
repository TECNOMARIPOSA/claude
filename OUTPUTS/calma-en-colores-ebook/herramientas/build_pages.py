import sys, json, base64, os
d = sys.argv[1]          # work dir with palette.json, lineart_*.png
base = sys.argv[2]       # colour illustration png
pal = json.load(open(d + '/palette.json'))


def b64(p, mime='image/png'):
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(p, 'rb').read()).decode())


color = b64(base)
free = b64(d + '/lineart_free.png')
numd = b64(d + '/lineart_numbered.png')

cfg = json.load(open(sys.argv[3]))
NUM, TITLE, SUB = cfg['num'], cfg['title'], cfg['sub']

css = '''
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Inter:wght@300;400;500;600&display=swap');
:root{--olive:#7d7f52;--olive-deep:#5c5e3a;--olive-wash:#eceedd;--cream:#f7f3e6;--cream-lt:#fffdf6;--orange:#eba46b;--orange-deep:#c06f35;--peach:#fdeedd;--ink:#2e2f24;--soft:#6b6c5b;--line:#e3dfcd;}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:794px;height:1123px;background:#fff;font-family:'Inter',sans-serif;color:var(--ink);}
.page{width:794px;height:1123px;position:relative;overflow:hidden;background:#fff;}
.foot{position:absolute;left:0;right:0;bottom:22px;text-align:center;font-family:'Fraunces',serif;font-style:italic;font-size:13px;color:var(--orange-deep);letter-spacing:.02em;}
.foot small{font-family:'Inter',sans-serif;font-style:normal;font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:#9a9a8a;margin-left:10px;}
/* P1 */
.card{position:absolute;inset:26px;border:2px solid var(--orange);border-radius:22px;background:linear-gradient(180deg,var(--cream-lt),#fff 40%);}
.card:after{content:'';position:absolute;inset:7px;border:1px solid var(--line);border-radius:16px;pointer-events:none;}
.hd{text-align:center;padding-top:42px;}
.orn{display:inline-flex;align-items:center;gap:12px;font-family:'Fraunces',serif;font-size:30px;font-weight:500;color:var(--olive-deep);}
.orn i{display:block;width:46px;height:1.5px;background:linear-gradient(90deg,transparent,var(--orange));}
.orn i:last-child{transform:scaleX(-1);}
h1{font-family:'Fraunces',serif;font-weight:500;font-size:40px;letter-spacing:-.01em;margin-top:10px;color:var(--ink);}
.sub{font-family:'Fraunces',serif;font-style:italic;font-size:19px;color:var(--orange-deep);margin-top:6px;}
.desc{max-width:560px;margin:14px auto 0;text-align:center;font-size:14.5px;line-height:1.6;color:var(--soft);}
.body{display:grid;grid-template-columns:290px 1fr;gap:30px;padding:36px 54px 0 54px;align-items:start;}
.pic{border-radius:18px;overflow:hidden;box-shadow:0 18px 36px -20px rgba(92,94,58,.55);border:5px solid #fff;outline:1px solid var(--line);}
.pic img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;}
.sec h2{font-family:'Fraunces',serif;font-weight:600;font-size:19px;color:var(--orange-deep);display:flex;align-items:center;gap:8px;margin-bottom:8px;}
.sec h2 b{display:inline-flex;width:26px;height:26px;border-radius:50%;background:var(--peach);align-items:center;justify-content:center;font-size:14px;color:var(--orange-deep);font-family:'Inter',sans-serif;}
.sec ul{list-style:none;}
.sec li{font-size:13.2px;line-height:1.55;color:var(--ink);padding:7px 0 7px 16px;border-bottom:1px solid var(--line);position:relative;}
.sec li:last-child{border:none;}
.sec li:before{content:'';position:absolute;left:0;top:15px;width:7px;height:7px;border-radius:50%;background:var(--orange);}
.sec li strong{color:var(--olive-deep);}
.play{margin:44px 54px 0;display:grid;grid-template-columns:1fr 1fr;gap:22px;}
.box{border-radius:18px;padding:22px 24px;}
.music{background:var(--olive-wash);border:1px solid var(--line);}
.music h2{color:var(--olive-deep);}
.music h2 b{background:#fff;color:var(--olive-deep);}
.music p{font-size:13.5px;line-height:1.6;color:var(--ink);}
.music em{display:block;margin-top:8px;font-family:'Fraunces',serif;font-size:13px;color:var(--soft);}
.how{background:var(--peach);border:1px solid #f3d9bd;}
.how p{font-size:13.5px;line-height:1.6;}
.quote{position:absolute;left:70px;right:70px;bottom:104px;text-align:center;}
.quote q{display:block;font-family:'Fraunces',serif;font-style:italic;font-size:23px;line-height:1.4;color:var(--olive-deep);quotes:'\\201C' '\\201D';}
.quote:before{content:'';display:block;width:60px;height:1.5px;margin:0 auto 16px;background:linear-gradient(90deg,transparent,var(--orange),transparent);}
.brand{position:absolute;left:0;right:0;bottom:44px;text-align:center;font-family:'Fraunces',serif;font-style:italic;font-size:21px;color:var(--orange-deep);}
.brand small{display:block;font-family:'Inter',sans-serif;font-style:normal;font-size:8.5px;letter-spacing:.3em;text-transform:uppercase;color:#a3a28f;margin-top:3px;}
/* P2 */
.p2img{position:absolute;left:107px;top:40px;width:580px;border-radius:6px;overflow:hidden;box-shadow:0 14px 32px -18px rgba(46,47,36,.5);}
.p2img img{display:block;width:100%;aspect-ratio:4/5;object-fit:cover;}
.pal{position:absolute;left:60px;right:60px;top:810px;}
.pal h3{text-align:center;font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--olive-deep);font-weight:600;margin-bottom:10px;}
.sw{display:grid;grid-template-columns:repeat(10,1fr);gap:6px 4px;}
.sw div{text-align:center;}
.sw span{display:block;height:24px;border-radius:5px;border:1px solid rgba(0,0,0,.12);}
.sw b{display:block;font-size:11px;margin-top:2px;color:var(--ink);font-weight:600;}
.sw i{display:block;font-style:normal;font-size:6.5px;color:#8a8a7a;letter-spacing:.02em;}
/* P3/4 */
.art{position:absolute;left:29px;top:70px;width:736px;height:920px;}
.art img{display:block;width:100%;height:100%;}
.tip{position:absolute;left:0;right:0;top:1006px;text-align:center;font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:#7a7a6a;}
'''

sw = ''.join('<div><span style="background:%s"></span><b>%d</b><i>%s</i></div>' % (p['hex'], p['n'], p['hex'].upper()) for p in pal)
rows_note = 'Cada número de la lámina corresponde a un color de la paleta'

facts = ''.join('<li><strong>%s</strong> %s</li>' % (f[0], f[1]) for f in cfg['facts'])
p1 = '''<div class="page"><div class="card">
<div class="hd"><div class="orn"><i></i>%(num)s<i></i></div><h1>%(title)s</h1><div class="sub">%(sub)s</div>
<p class="desc">%(desc)s</p></div>
<div class="body"><div class="pic"><img src="%(color)s"></div>
<div class="sec"><h2><b>?</b>¿Sabías que&hellip;?</h2><ul>%(facts)s</ul></div></div>
<div class="play"><div class="box music sec"><h2><b>&#9835;</b>Pon play</h2><p>%(music)s</p><em>(Ideal para acompañar este momento de calma.)</em></div>
<div class="box how sec"><h2><b>&#10047;</b>Tu momento</h2><p>%(moment)s</p></div></div>
<div class="quote"><q>%(quote)s</q></div>
<div class="brand">Calma en colores<small>Pintura por números antiestrés</small></div>
</div></div>''' % dict(num=NUM, title=TITLE, sub=SUB, color=color, desc=cfg['desc'], facts=facts, music=cfg['music'], moment=cfg['moment'], quote=cfg['quote'])

p2 = '''<div class="page"><div class="p2img"><img src="%(color)s"></div>
<div class="pal"><h3>Paleta de colores sugerida</h3><div class="sw">%(sw)s</div></div>
<div class="foot">Calma en colores<small>%(num)s · %(title)s · Referencia a color</small></div></div>''' % dict(color=color, sw=sw, num=NUM, title=TITLE)

p3 = '''<div class="page"><div class="art"><img src="%(a)s"></div>
<div class="tip">%(note)s</div>
<div class="foot">Calma en colores<small>%(num)s · %(title)s · Colorea por números</small></div></div>''' % dict(a=numd, note=rows_note, num=NUM, title=TITLE)

p4 = '''<div class="page"><div class="art"><img src="%(a)s"></div>
<div class="tip">Elige tus propios colores</div>
<div class="foot">Calma en colores<small>%(num)s · %(title)s · Colorea libremente</small></div></div>''' % dict(a=free, num=NUM, title=TITLE)

for i, body in enumerate([p1, p2, p3], 1):
    open('%s/p%d.html' % (d, i), 'w').write('<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>%s</body></html>' % (css, body))
print('ok')
