from pathlib import Path
import json
W=Path(__file__).resolve().parent
fonts=(W/'fonts/fonts.css').read_text()
NOISE="""background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .29 0 0 0 0 .23 0 0 0 0 .18 0 0 0 1 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")"""
CSS="""%s
:root{--areia:#E6DDD2;--bege:#CABBA9;--taupe:#9A8D7C;--grafite:#52493F;--preto:#141514;--creme:#F3ECE2;--ouro:#B8976A;--tinta:#2A241F}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1920px;overflow:hidden;position:relative;font-family:Poppins,sans-serif;-webkit-font-smoothing:antialiased}
.abs{position:absolute}
.noise{position:absolute;inset:0;opacity:.11;mix-blend-mode:multiply;%s}
.lab{font-family:Outfit;font-weight:400;letter-spacing:.4em;text-transform:uppercase}
.beams{position:absolute;inset:-200px;background:repeating-linear-gradient(118deg,rgba(255,240,215,0) 0 140px,rgba(255,240,215,.4) 180px 250px,rgba(255,240,215,0) 310px 460px);filter:blur(24px)}
""" % (fonts, NOISE)
LEAF=lambda stroke,w,op: f'<svg viewBox="0 0 100 100" width="{w}" height="{w}" style="opacity:{op}"><path d="M18 92 C14 52, 40 18, 90 6 C92 50, 64 86, 18 92 Z" fill="none" stroke="{stroke}" stroke-width="1.1"/></svg>'
def page(body): return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'


from pathlib import Path
import json


EXTRA="""<style>
.bgw{position:absolute;inset:0;background:linear-gradient(180deg,#F2ECE4,#EAE2D7)}
.glow{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(255,224,182,.75),rgba(255,224,182,0) 66%)}
.h1{font-weight:300;color:var(--tinta);letter-spacing:-.02em;line-height:1}
.h1 b{font-weight:600}
.card{background:rgba(250,246,240,.72);border:1px solid rgba(154,141,124,.28);border-radius:28px;box-shadow:0 20px 50px rgba(74,60,48,.08);backdrop-filter:blur(6px)}
table{width:100%;border-collapse:collapse}
td,th{padding:0}
.obs{font-weight:300;font-size:25px;color:var(--grafite);line-height:1.45}
</style>"""
def base(inner, glowpos="right:-300px;top:-260px"):
    return page(EXTRA+f'''<div class="bgw"></div><div class="glow" style="{glowpos};width:1100px;height:1100px"></div><div class="beams" style="opacity:.55"></div><div class="noise"></div>'''+inner)

ICON={
'pix':'<svg width="64" height="64" viewBox="0 0 64 64" fill="none" stroke="#4A3C30" stroke-width="2.2"><path d="M32 6 L58 32 L32 58 L6 32 Z"/><path d="M20 32 L32 20 L44 32 L32 44 Z"/></svg>',
'card':'<svg width="64" height="64" viewBox="0 0 64 64" fill="none" stroke="#4A3C30" stroke-width="2.2"><rect x="6" y="14" width="52" height="36" rx="6"/><path d="M6 24 H58"/><path d="M14 40 H28"/></svg>',
'swap':'<svg width="64" height="64" viewBox="0 0 64 64" fill="none" stroke="#4A3C30" stroke-width="2.2"><rect x="6" y="10" width="18" height="44" rx="4"/><rect x="40" y="10" width="18" height="44" rx="4"/><path d="M28 26 H36 M33 22 L37 26 L33 30"/><path d="M36 38 H28 M31 34 L27 38 L31 42"/></svg>',
'no':'<svg width="44" height="44" viewBox="0 0 64 64" fill="none" stroke="#9A8D7C" stroke-width="2.6"><circle cx="32" cy="32" r="24"/><path d="M15 15 L49 49"/></svg>',
}

def boletim(kicker,title,sub,facts,fonte):
    li=''.join(f'''<div style="display:flex;gap:34px;padding:30px 0;border-top:1px solid rgba(154,141,124,.3)">
  <div style="font-family:Outfit;font-weight:500;font-size:26px;color:#8A6E48;padding-top:8px;width:44px;flex-shrink:0">0{i}</div>
  <div style="font-weight:400;font-size:34px;color:var(--tinta);line-height:1.35">{f}</div></div>''' for i,f in enumerate(facts,1))
    return base(f'''
<div class="abs" style="left:96px;right:96px;top:240px;display:flex;justify-content:space-between;align-items:center">
 <div style="display:flex;align-items:center;gap:18px"><div style="width:14px;height:14px;border-radius:50%;background:#8A6E48"></div>
 <span class="lab" style="font-size:23px;color:var(--grafite);font-weight:500">boletim tech gr</span></div>
 <img src="logo_brown.png" style="width:104px">
</div>
<div class="abs" style="left:96px;right:96px;top:420px">
 <div class="lab" style="font-size:22px;color:var(--taupe)">{kicker}</div>
 <div class="h1" style="font-size:92px;margin-top:22px;line-height:1.04">{title}</div>
 <div style="font-weight:300;font-size:34px;color:var(--grafite);margin-top:30px;line-height:1.4">{sub}</div>
</div>
<div class="abs card" style="left:64px;right:64px;top:900px;padding:10px 44px 6px">{li.replace('border-top:1px solid rgba(154,141,124,.3)','',1)}</div>
<div class="abs" style="left:96px;right:96px;bottom:300px;display:flex;justify-content:space-between;align-items:center">
 <span style="font-weight:300;font-size:22px;color:var(--taupe)">Fonte: {fonte}</span>
 <span class="lab" style="font-size:21px;color:#4A3C30;font-weight:500">siga para mais &nbsp;→</span>
</div>''', glowpos="left:-380px;top:-320px")

# Uso: python3 boletim.py dados.json
# dados.json = {"slug":"2026-10-30_tema","kicker":"novidade apple","title":"Linha 1<br><b>destaque</b>",
#   "sub":"Frase curta.<br>Segunda linha.","facts":["fato 1","fato 2","fato 3","fato 4"],"fonte":"Apple Newsroom"}
# Gera <slug>.html; depois: node shot.js <slug>  -> out/<slug>.png
if __name__=="__main__":
    import sys
    d=json.load(open(sys.argv[1]))
    (W/(d['slug']+'.html')).write_text(boletim(d['kicker'],d['title'],d['sub'],d['facts'],d['fonte']))
    print(W/(d['slug']+'.html'))
