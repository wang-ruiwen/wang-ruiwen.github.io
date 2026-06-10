# -*- coding: utf-8 -*-
# Generates 10 self-contained design previews of the homepage (same real
# content, ten different visual languages). Output: previews/01..10-*.html
import os

NAME  = "Ruiwen WANG"
ROLE  = "PhD Candidate · AI Infra · LLM Pretraining · Hybrid Parallelism"
AFFIL = "Sorbonne Université × EURECOM × Huawei Paris · Paris, France"
A1 = ("Third-year PhD candidate in Computer Science at Sorbonne Université and "
      "EURECOM, working at the intersection of AI Systems, Parallel Computing "
      "and Performance Engineering.")
A2 = ("I build profiling-free planners for hybrid-parallel LLM pretraining — "
      "validated on Huawei Ascend-910 clusters of up to 10K+ NPUs and "
      "benchmarked against Megatron-LM.")
AV = "/images/avatar.jpg"
LINKS = [("Email","mailto:wangrw0124@gmail.com"),
         ("Scholar","https://scholar.google.com/citations?user=AR1nHEUAAAAJ"),
         ("ORCID","https://orcid.org/0009-0000-6709-5970"),
         ("GitHub","https://github.com/wang-ruiwen")]
TOPICS = ["hybrid parallelism","pipeline bubbles","symbolic cost modelling",
          "Mixture of Experts","Ascend NPU","ILP optimisation"]
PUBS = [
 ("R. Wang, P. Fang, C. Li, T. Tachon, R. Appuswamy",
  "PRISM: Profiling-Free Symbolic Memory-Driven Strategy Planner for Large DNN Training",
  "SCA / HPCAsia 2026"),
 ("R. Wang, C. Li, T. Tachon, R. Appuswamy, T. Su",
  "BMPipe: Bubble-Memory Co-optimization Strategy Planner for Very-Large DNN Training",
  "IEEE CLUSTER 2025"),
 ("R. Wang, C. Li, R. Appuswamy, Y. Yuan",
  "H²O: Holistic Hyper-Parameter Optimization for Large-Scale DNN Training",
  "Euro-Par 2025 · Best Poster"),
 ("R. Wang, C. Li, H. Wang, R. Appuswamy, Y. Yuan",
  "ManuMatic: Strategy Injection for Robust Automatic Hybrid Parallelism",
  "IFIP NPC 2025"),
]

FONTS = """
@font-face{font-family:'Source Serif 4';font-weight:400 700;font-display:swap;src:url('/fonts/source-serif-4-latin-wght-normal.woff2') format('woff2');}
@font-face{font-family:'Inter';font-weight:400 700;font-display:swap;src:url('/fonts/inter-latin-wght-normal.woff2') format('woff2');}
@font-face{font-family:'Source Code Pro';font-weight:400;font-display:swap;src:url('/fonts/source-code-pro-latin-400-normal.woff2') format('woff2');}
*{box-sizing:border-box;}
"""

def page(css, body):
    return ("<!doctype html><html lang=en><head><meta charset=utf-8>"
            "<meta name=viewport content='width=device-width,initial-scale=1'>"
            "<title>preview</title><style>" + FONTS + css + "</style></head><body>"
            + body + "</body></html>")

def links_html(sep="", cls=""):
    return sep.join(f'<a class="{cls}" href="{u}">{t}</a>' for t,u in LINKS)

# ---------------------------------------------------------------- 01 editorial
def editorial():
    css = """
body{margin:0;background:#fafafa;color:#1d2336;font-family:'Source Serif 4',Georgia,serif;line-height:1.65;}
.wrap{max-width:760px;margin:0 auto;padding:48px 28px;counter-reset:s;}
.hero{text-align:center;}
.hero img{width:104px;height:104px;border-radius:50%;object-fit:cover;border:1px solid rgba(20,26,43,.12);box-shadow:0 10px 30px rgba(20,26,43,.06);}
.name{font-size:2rem;font-weight:700;letter-spacing:-.025em;color:#141a2b;margin:.7rem 0 .25rem;}
.role{font-family:Inter,sans-serif;font-size:.9rem;color:#535d6f;margin:0 0 .2rem;}
.affil{font-family:Inter,sans-serif;font-size:.82rem;color:#6a7488;margin:0 0 .7rem;}
.links a{font-family:Inter,sans-serif;color:#2c5dbf;text-decoration:none;margin:0 .4rem;font-size:.85rem;border-bottom:1px solid rgba(75,129,232,.3);}
h2{font-family:Inter,sans-serif;font-size:1.25rem;color:#141a2b;border-bottom:1px solid rgba(75,129,232,.14);padding-bottom:.4rem;margin:2.3rem 0 1rem;}
h2::before{counter-increment:s;content:counter(s,decimal-leading-zero) " ";color:#4b81e8;font-size:.7em;}
p{font-size:1rem;}
.pub{border-top:1px solid rgba(75,129,232,.12);padding:.7rem 0;}
.pa{font-size:.88rem;margin:0 0 .12rem;}.pa b{color:#2c5dbf;}
.pt{font-size:.95rem;font-style:italic;margin:0 0 .12rem;}
.pv{font-family:Inter,sans-serif;font-size:.79rem;color:#6a7488;margin:0;}
"""
    pubs = "".join(
        f'<div class=pub><p class=pa><b>{a.split(",")[0]}</b>,{",".join(a.split(",")[1:])}</p>'
        f'<p class=pt>{t}.</p><p class=pv>{v}</p></div>' for a,t,v in PUBS)
    body = f"""<div class=wrap><div class=hero><img src="{AV}" alt="">
<h1 class=name>{NAME}</h1><p class=role>{ROLE}</p><p class=affil>{AFFIL}</p>
<p class=links>{links_html()}</p></div>
<h2>About</h2><p>{A1}</p><p>{A2}</p>
<h2>Selected publications</h2>{pubs}</div>"""
    return page(css, body)

# ---------------------------------------------------------------- 02 latex
def latex():
    css = """
body{margin:0;background:#fff;color:#111;font-family:'Source Serif 4',Georgia,'Times New Roman',serif;line-height:1.5;}
.wrap{max-width:660px;margin:0 auto;padding:56px 32px;counter-reset:s;}
.title{text-align:center;font-size:1.7rem;font-weight:700;line-height:1.25;margin:0 0 .9rem;}
.authors{text-align:center;font-size:1.05rem;margin:0 0 .15rem;}
.affil2{text-align:center;font-size:.85rem;color:#444;font-style:italic;margin:0 0 1.5rem;}
.abs{margin:0 1.6rem 1.7rem;font-size:.9rem;}
.abs .h{text-align:center;font-variant:all-small-caps;letter-spacing:.06em;font-weight:700;font-size:.95rem;margin-bottom:.25rem;}
h2{font-size:1.05rem;font-weight:700;margin:1.7rem 0 .5rem;}
h2::before{counter-increment:s;content:counter(s) "\\00a0\\00a0";}
p{font-size:.95rem;text-align:justify;hyphens:auto;margin:0 0 .7rem;}
.r{font-size:.86rem;margin:0 0 .55rem;padding-left:1.7rem;text-indent:-1.7rem;line-height:1.45;}
.r b{font-weight:700;}.r i{font-style:italic;color:#333;}
a{color:#7a1f2b;text-decoration:none;}
"""
    refs = "".join(
        f'<p class=r>[{i+1}]&ensp;{a}. <b>{t}</b>. <i>{v}</i>.</p>'
        for i,(a,t,v) in enumerate(PUBS))
    body = f"""<div class=wrap>
<h1 class=title>Systematic &amp; Portable Optimisation of Hybrid Parallelism for Large-Scale Distributed Training</h1>
<p class=authors>{NAME}</p>
<p class=affil2>Sorbonne Université · EURECOM · Huawei Paris</p>
<div class=abs><div class=h>Abstract</div><p>{A1} {A2}</p></div>
<h2>Research</h2><p>I formulate parallelism planning as closed-form, hardware-parametric
cost surfaces solved by lightweight ILPs — spanning DP/TP/PP/VPP/SP/EP/OP — so that
foundation-scale training is planned without per-cluster profiling and stays portable
across hardware and model changes.</p>
<h2>Selected Publications</h2>{refs}
<p style="font-size:.82rem;color:#666;margin-top:1.4rem">{links_html(" · ")}</p>
</div>"""
    return page(css, body)

# ---------------------------------------------------------------- 03 tufte
def tufte():
    css = """
body{margin:0;background:#fffff8;color:#111;font-family:'Source Serif 4',Palatino,Georgia,serif;line-height:1.7;}
.wrap{max-width:1180px;margin:0 auto;padding:60px 5% 60px 8%;}
.name{font-size:2.5rem;font-weight:600;letter-spacing:-.01em;margin:0 0 .15rem;line-height:1.08;}
.role{font-size:1.05rem;font-style:italic;color:#3a3a3a;margin:0 0 .4rem;}
.links a{color:#111;font-size:.85rem;margin-right:1rem;text-decoration:none;border-bottom:1px solid #bbb;}
.body{max-width:55%;}
h2{font-size:1.5rem;font-weight:400;font-style:italic;margin:2.2rem 0 .5rem;}
p{font-size:1.05rem;}
.note{float:right;clear:right;width:34%;margin-right:-44%;margin-top:.3rem;font-size:.82rem;line-height:1.5;color:#444;font-style:italic;}
.pub{margin-bottom:.8rem;}.pub .pt{font-style:italic;}.pub .pv{font-size:.82rem;color:#555;}
.pub .pa{font-size:.85rem;color:#444;}
"""
    pubs = "".join(
        f'<div class=pub><div class=pt>{t}</div><div class=pv>{v} — {a}</div></div>'
        for a,t,v in PUBS)
    body = f"""<div class=wrap>
<h1 class=name>{NAME}</h1><p class=role>{ROLE}</p>
<p class=links>{links_html()}</p>
<div class=body>
<h2>About</h2>
<p class=lead><span class=note>Planners studied in the thesis are integrated into Huawei's
MindSpore / D-Rec runtime and validated on Ascend-910 clusters of up to 10K+ NPUs.</span>{A1}</p>
<p>{A2}</p>
<h2>Selected work</h2>{pubs}
</div></div>"""
    return page(css, body)

# ---------------------------------------------------------------- 04 swiss
def swiss():
    css = """
body{margin:0;background:#fff;color:#111;font-family:Inter,'Helvetica Neue',Arial,sans-serif;line-height:1.5;-webkit-font-smoothing:antialiased;}
.wrap{max-width:880px;margin:0 auto;padding:56px 32px;}
.top{border-top:3px solid #111;padding-top:16px;display:flex;justify-content:space-between;font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;}
.top .r{color:#e4002b;}
.name{font-size:4.2rem;font-weight:800;letter-spacing:-.045em;line-height:.95;margin:34px 0 16px;}
.role{font-size:1.05rem;max-width:32ch;color:#222;margin:0;}
.links{font-size:.76rem;text-transform:uppercase;letter-spacing:.08em;margin-top:18px;}
.links a{color:#111;text-decoration:none;margin-right:1.1rem;border-bottom:2px solid #e4002b;padding-bottom:2px;}
h2{font-size:.78rem;text-transform:uppercase;letter-spacing:.16em;color:#e4002b;margin:46px 0 14px;font-weight:700;}
p{font-size:1.1rem;max-width:60ch;line-height:1.6;}
.row{display:grid;grid-template-columns:9rem 1fr;gap:1rem;border-top:1px solid #ddd;padding:14px 0;}
.yr{font-size:.74rem;text-transform:uppercase;letter-spacing:.06em;color:#999;padding-top:3px;}
.pt{font-weight:600;font-size:1rem;}.pv{font-size:.82rem;color:#666;}
"""
    pubs = "".join(
        f'<div class=row><div class=yr>{v}</div><div><div class=pt>{t}</div></div></div>'
        for a,t,v in PUBS)
    body = f"""<div class=wrap>
<div class=top><span>{NAME}</span><span class=r>Paris · 2026</span></div>
<h1 class=name>AI Infra<br>for LLM<br>pretraining.</h1>
<p class=role>{ROLE}</p>
<p class=links>{links_html()}</p>
<h2>About</h2><p>{A1} {A2}</p>
<h2>Selected publications</h2>{pubs}</div>"""
    return page(css, body)

# ---------------------------------------------------------------- 05 terminal
def terminal():
    css = """
body{margin:0;background:#0b0e14;color:#c8d3e0;font-family:'Source Code Pro',monospace;line-height:1.65;font-size:14px;}
.wrap{max-width:820px;margin:0 auto;padding:46px 26px;}
.p{color:#3ddc84;}.m{color:#7c8699;}.y{color:#e0af68;}
.name{font-size:1.7rem;color:#e6edf3;font-weight:600;margin:.3rem 0 .1rem;}
.role{color:#7aa2f7;margin:0 0 .2rem;}.affil{color:#7c8699;}
.box{border:1px solid #1f2733;border-radius:6px;padding:14px 16px;margin:18px 0;background:#0e1320;}
h2{color:#3ddc84;font-size:1rem;margin:26px 0 10px;font-weight:600;}
h2::before{content:'## ';color:#3a4658;}
a{color:#7aa2f7;text-decoration:none;}
.pub{margin:12px 0;border-left:2px solid #1f2733;padding-left:12px;}
.pub .pt{color:#e6edf3;}.pub .pv{color:#7c8699;font-size:.92em;}.pub b{color:#e0af68;}
.links a{margin-right:1.1rem;}
"""
    pubs = "".join(
        f'<div class=pub><div class=pt>{t}</div><div class=pv><b>{v}</b> — {a}</div></div>'
        for a,t,v in PUBS)
    body = f"""<div class=wrap>
<div><span class=p>ruiwen@phd</span><span class=m>:~$</span> whoami</div>
<h1 class=name>{NAME}</h1><p class=role>{ROLE}</p><p class=affil>{AFFIL}</p>
<div class=box><span class=m># about</span><br>{A1}<br><br>{A2}</div>
<h2>publications</h2>{pubs}
<h2>links</h2><p class=links>{links_html()}</p></div>"""
    return page(css, body)

# ---------------------------------------------------------------- 06 air
def air():
    css = """
body{margin:0;background:#fff;color:#2a2a2a;font-family:Inter,system-ui,sans-serif;line-height:1.7;font-weight:350;}
.wrap{max-width:600px;margin:0 auto;padding:88px 28px;text-align:center;}
img{width:84px;height:84px;border-radius:50%;object-fit:cover;}
.name{font-size:1.9rem;font-weight:600;letter-spacing:-.02em;margin:1.1rem 0 .35rem;}
.role{font-size:.9rem;color:#999;margin:0 0 .25rem;}
.affil{font-size:.8rem;color:#bbb;margin:0 0 1.2rem;}
.links a{color:#4f46e5;text-decoration:none;margin:0 .55rem;font-size:.85rem;}
.rule{width:36px;height:1px;background:#e8e8e8;margin:3rem auto;}
h2{font-size:.74rem;text-transform:uppercase;letter-spacing:.2em;color:#c4c4c4;font-weight:600;margin:0 0 1.1rem;}
.body{text-align:left;}
p{font-size:1.02rem;color:#444;}
.pub{margin:1.1rem 0;}.pub .pt{color:#2a2a2a;font-size:.98rem;}.pub .pv{font-size:.8rem;color:#aaa;}
"""
    pubs = "".join(f'<div class=pub><div class=pt>{t}</div><div class=pv>{v}</div></div>'
                   for a,t,v in PUBS)
    body = f"""<div class=wrap><img src="{AV}" alt="">
<h1 class=name>{NAME}</h1><p class=role>{ROLE}</p><p class=affil>{AFFIL}</p>
<p class=links>{links_html()}</p>
<div class=rule></div>
<div class=body><h2 style="text-align:center">About</h2><p>{A1}</p><p>{A2}</p></div>
<div class=rule></div>
<div class=body><h2 style="text-align:center">Selected publications</h2>{pubs}</div></div>"""
    return page(css, body)

# ---------------------------------------------------------------- 07 brutalist
def brutalist():
    css = """
body{margin:0;background:#f4f1ea;color:#111;font-family:Inter,Arial,sans-serif;line-height:1.5;}
.wrap{max-width:820px;margin:0 auto;padding:38px 24px;}
.card{background:#fff;border:3px solid #111;box-shadow:7px 7px 0 #111;padding:22px;margin-bottom:26px;}
.name{font-family:'Source Code Pro',monospace;font-size:2.5rem;font-weight:600;letter-spacing:-.02em;margin:0 0 8px;}
.role{font-family:'Source Code Pro',monospace;font-size:.82rem;background:#ff5c00;color:#111;display:inline-block;padding:3px 8px;border:2px solid #111;}
.affil{font-size:.85rem;margin-top:12px;}
.links a{font-family:'Source Code Pro',monospace;font-size:.78rem;color:#111;text-decoration:none;border:2px solid #111;padding:3px 8px;margin:12px 8px 0 0;display:inline-block;background:#fff;}
h2{font-family:'Source Code Pro',monospace;font-size:1rem;text-transform:uppercase;letter-spacing:.04em;border-bottom:3px solid #111;padding-bottom:6px;margin:0 0 14px;}
p{font-size:1rem;}
.pub{border-bottom:2px dashed #111;padding:11px 0;}.pub:last-child{border-bottom:none;}
.pub .pt{font-weight:700;}.pub .pa{font-size:.82rem;color:#444;}
.pub .pv{font-family:'Source Code Pro',monospace;font-size:.74rem;background:#111;color:#fff;padding:2px 6px;display:inline-block;margin-top:5px;}
"""
    pubs = "".join(
        f'<div class=pub><div class=pt>{t}</div><div class=pa>{a}</div>'
        f'<span class=pv>{v}</span></div>' for a,t,v in PUBS)
    body = f"""<div class=wrap>
<div class=card><h1 class=name>{NAME}</h1><div><span class=role>{ROLE}</span></div>
<div class=affil>{AFFIL}</div><div class=links>{links_html()}</div></div>
<div class=card><h2>About</h2><p>{A1}</p><p>{A2}</p></div>
<div class=card><h2>Publications</h2>{pubs}</div></div>"""
    return page(css, body)

# ---------------------------------------------------------------- 08 magazine
def magazine():
    css = """
body{margin:0;background:#f7f3ec;color:#2b2622;font-family:'Source Serif 4',Georgia,serif;line-height:1.6;}
.wrap{max-width:740px;margin:0 auto;padding:54px 32px;}
.kicker{font-family:Inter,sans-serif;text-transform:uppercase;letter-spacing:.24em;font-size:.7rem;color:#7a1f2b;text-align:center;margin-bottom:14px;}
.name{font-size:3.7rem;font-weight:700;text-align:center;letter-spacing:-.02em;line-height:1;margin:0 0 12px;}
.role{font-family:Inter,sans-serif;text-align:center;font-size:.88rem;color:#6a5f54;margin:0;}
.rule{border:none;border-top:2px solid #7a1f2b;width:56px;margin:22px auto;}
h2{font-family:Inter,sans-serif;font-size:.78rem;text-transform:uppercase;letter-spacing:.18em;color:#7a1f2b;margin:2.2rem 0 1rem;text-align:center;}
p{font-size:1.06rem;}
.lead::first-letter{font-size:3.3em;float:left;line-height:.78;font-weight:700;margin:.04em .09em 0 0;color:#7a1f2b;}
.pub{text-align:center;margin:1.2rem 0;}
.pub .pt{font-style:italic;font-size:1.06rem;}
.pub .pa{font-family:Inter,sans-serif;font-size:.8rem;color:#6a5f54;margin-top:.15rem;}
.pub .pv{font-family:Inter,sans-serif;font-size:.74rem;color:#9a8f84;text-transform:uppercase;letter-spacing:.1em;margin-top:.1rem;}
.links{text-align:center;font-family:Inter,sans-serif;font-size:.82rem;margin-top:1.4rem;}
.links a{color:#7a1f2b;text-decoration:none;margin:0 .5rem;}
"""
    pubs = "".join(
        f'<div class=pub><div class=pt>{t}</div><div class=pa>{a}</div><div class=pv>{v}</div></div>'
        for a,t,v in PUBS)
    body = f"""<div class=wrap>
<div class=kicker>AI Systems · Parallel Computing</div>
<h1 class=name>{NAME}</h1><p class=role>{ROLE}</p>
<hr class=rule>
<h2>About</h2><p class=lead>{A1}</p><p>{A2}</p>
<hr class=rule>
<h2>Selected publications</h2>{pubs}
<p class=links>{links_html()}</p></div>"""
    return page(css, body)

# ---------------------------------------------------------------- 09 broadsheet
def broadsheet():
    css = """
body{margin:0;background:#fbfaf7;color:#1a1a1a;font-family:'Source Serif 4','Times New Roman',serif;line-height:1.55;}
.wrap{max-width:840px;margin:0 auto;padding:38px 28px;}
.mast{border-top:4px double #1a1a1a;border-bottom:4px double #1a1a1a;padding:12px 0;text-align:center;margin-bottom:4px;}
.name{font-size:3rem;font-weight:700;letter-spacing:.06em;margin:0;text-transform:uppercase;}
.dateline{display:flex;justify-content:space-between;font-family:Inter,sans-serif;font-size:.7rem;text-transform:uppercase;letter-spacing:.12em;border-bottom:1px solid #1a1a1a;padding:6px 2px;margin-bottom:22px;color:#444;}
.role{text-align:center;font-style:italic;font-size:1.05rem;margin:0 0 20px;}
h2{font-family:Inter,sans-serif;font-size:.72rem;text-transform:uppercase;letter-spacing:.16em;border-bottom:1px solid #1a1a1a;padding-bottom:4px;margin:0 0 12px;}
.cols{column-count:2;column-gap:30px;column-rule:1px solid #ccc;}
.cols p{font-size:.95rem;text-align:justify;hyphens:auto;margin:0 0 .7rem;}
.lead::first-letter{font-size:2.7em;float:left;line-height:.78;font-weight:700;margin:.03em .07em 0 0;}
.pub{break-inside:avoid;margin-bottom:.8rem;}.pub .pt{font-weight:600;font-size:.96rem;}
.pub .pv{font-family:Inter,sans-serif;font-size:.74rem;color:#666;}
.links{font-family:Inter,sans-serif;font-size:.78rem;margin-top:1.2rem;}.links a{color:#1a1a1a;margin-right:1rem;}
"""
    pubs = "".join(f'<div class=pub><div class=pt>{t}</div><div class=pv>{v}</div></div>'
                   for a,t,v in PUBS)
    body = f"""<div class=wrap>
<div class=mast><h1 class=name>{NAME}</h1></div>
<div class=dateline><span>Paris, France</span><span>AI Infra · MLSys</span><span>Vol. PhD · 2026</span></div>
<p class=role>{ROLE}</p>
<h2>About the researcher</h2>
<div class=cols><p class=lead>{A1}</p><p>{A2}</p>
<h2 style="margin-top:1rem">Selected publications</h2>{pubs}</div>
<p class=links>{links_html()}</p></div>"""
    return page(css, body)

# ---------------------------------------------------------------- 10 glass
def glass():
    css = """
body{margin:0;min-height:100vh;background:linear-gradient(160deg,#eef2ff 0%,#f5f3ff 45%,#fdf2f8 100%);color:#1e293b;font-family:Inter,system-ui,sans-serif;line-height:1.65;}
.wrap{max-width:720px;margin:0 auto;padding:52px 24px;}
.card{background:rgba(255,255,255,.62);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.85);border-radius:20px;box-shadow:0 12px 40px rgba(99,102,241,.13);padding:26px;margin-bottom:20px;}
.hero{text-align:center;}
img{width:90px;height:90px;border-radius:50%;object-fit:cover;border:3px solid #fff;box-shadow:0 8px 24px rgba(99,102,241,.28);}
.name{font-size:2rem;font-weight:700;letter-spacing:-.02em;margin:.55rem 0 .25rem;background:linear-gradient(90deg,#6366f1,#a855f7);-webkit-background-clip:text;background-clip:text;color:transparent;}
.role{font-size:.88rem;color:#64748b;margin:0 0 .2rem;}.affil{font-size:.78rem;color:#94a3b8;margin:0;}
.links a{font-size:.82rem;color:#6366f1;text-decoration:none;margin:0 .5rem;font-weight:500;}
.links{margin-top:.8rem;}
h2{font-size:.74rem;text-transform:uppercase;letter-spacing:.14em;color:#a855f7;font-weight:700;margin:0 0 .9rem;}
p{font-size:1rem;margin:0 0 .6rem;}
.tags{display:flex;flex-wrap:wrap;gap:8px;}
.tag{font-size:.76rem;background:rgba(99,102,241,.1);color:#6366f1;border-radius:999px;padding:4px 12px;}
.pub{padding:.6rem 0;border-bottom:1px solid rgba(148,163,184,.2);}.pub:last-child{border-bottom:none;}
.pub .pt{font-weight:600;font-size:.94rem;}.pub .pv{font-size:.78rem;color:#94a3b8;}
"""
    pubs = "".join(f'<div class=pub><div class=pt>{t}</div><div class=pv>{v}</div></div>'
                   for a,t,v in PUBS)
    tags = "".join(f'<span class=tag>{x}</span>' for x in TOPICS)
    body = f"""<div class=wrap>
<div class="card hero"><img src="{AV}" alt="">
<h1 class=name>{NAME}</h1><p class=role>{ROLE}</p><p class=affil>{AFFIL}</p>
<p class=links>{links_html()}</p></div>
<div class=card><h2>About</h2><p>{A1}</p><p>{A2}</p></div>
<div class=card><h2>Focus</h2><div class=tags>{tags}</div></div>
<div class=card><h2>Selected publications</h2>{pubs}</div></div>"""
    return page(css, body)

# ---------------------------------------------------------------- 11 apple
def apple():
    css = """
:root{--t:#1d1d1f;--s:#6e6e73;--g:#86868b;--blue:#0066cc;--btn:#0071e3;--panel:#f5f5f7;}
body{margin:0;background:#fff;color:var(--t);font-family:Inter,-apple-system,'SF Pro Display',BlinkMacSystemFont,'Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased;line-height:1.47;letter-spacing:-.01em;}
.nav{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.72);backdrop-filter:saturate(1.8) blur(20px);-webkit-backdrop-filter:saturate(1.8) blur(20px);border-bottom:1px solid rgba(0,0,0,.08);}
.nav-in{max-width:980px;margin:0 auto;display:flex;align-items:center;gap:26px;height:46px;padding:0 22px;font-size:.82rem;}
.nav-in .brand{font-weight:600;}.nav-in .sp{flex:1;}
.nav-in a{color:#1d1d1f;opacity:.82;text-decoration:none;}.nav-in a:hover{opacity:1;color:var(--blue);}
section{padding:88px 22px;text-align:center;}
.wrapn{max-width:820px;margin:0 auto;}
.eyebrow{font-size:1.2rem;color:var(--g);font-weight:600;margin:0 0 4px;}
h1{font-size:clamp(2.6rem,7vw,4.2rem);font-weight:700;letter-spacing:-.03em;line-height:1.05;margin:.18em 0 .28em;}
.hero img{width:92px;height:92px;border-radius:50%;object-fit:cover;box-shadow:0 6px 24px rgba(0,0,0,.12);}
.hero .sub{font-size:clamp(1.2rem,2.6vw,1.55rem);color:var(--s);font-weight:500;letter-spacing:-.01em;margin:0 auto 1.5em;max-width:26ch;}
.cta{display:inline-flex;gap:20px;align-items:center;flex-wrap:wrap;justify-content:center;}
.btn{background:var(--btn);color:#fff;font-size:1.06rem;padding:.7em 1.35em;border-radius:980px;text-decoration:none;}
.lnk{color:var(--blue);font-size:1.06rem;text-decoration:none;}
.lnk::after{content:" ›";}
h2{font-size:clamp(2rem,5vw,3rem);font-weight:700;letter-spacing:-.025em;line-height:1.08;margin:0 0 .32em;}
.panel{background:var(--panel);}
.lead{font-size:clamp(1.15rem,2.3vw,1.4rem);color:var(--s);font-weight:400;max-width:36ch;margin:0 auto;line-height:1.42;}
.dark{background:#000;color:#f5f5f7;}
.dark h2{color:#f5f5f7;}
.stats{display:flex;justify-content:center;gap:60px;flex-wrap:wrap;margin-top:28px;}
.num{font-size:clamp(2.6rem,6vw,3.9rem);font-weight:700;letter-spacing:-.02em;line-height:1;}
.lab{color:var(--g);font-size:1rem;margin-top:10px;}
.accent{color:#2997ff;}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:20px;max-width:980px;margin:44px auto 0;text-align:left;}
.tile{background:var(--panel);border-radius:22px;padding:30px 30px 26px;}
.tile .ev{font-size:.82rem;color:var(--g);font-weight:600;margin:0 0 10px;}
.tile h3{font-size:1.6rem;font-weight:700;letter-spacing:-.02em;margin:0 0 8px;}
.tile p{font-size:1rem;color:var(--s);margin:0 0 14px;line-height:1.42;}
.tile .lnk{font-size:1rem;}
.pubs{max-width:720px;margin:0 auto;text-align:left;}
.pub{padding:20px 0;border-top:1px solid rgba(0,0,0,.1);}.pub:first-child{border-top:none;}
.pub h4{font-size:1.15rem;font-weight:600;letter-spacing:-.01em;margin:0 0 4px;}
.pub .pv{color:var(--g);font-size:.95rem;}
.foot{background:var(--panel);color:var(--g);font-size:.78rem;padding:30px 22px;text-align:center;border-top:1px solid rgba(0,0,0,.08);}
.foot a{color:var(--g);text-decoration:none;}
"""
    SYS = [
      ("PRISM","SCA / HPCAsia 2026","Profiling-free symbolic memory-driven strategy planner. 92–96% memory-prediction accuracy; up to 1.43× MFU over Megatron-LM."),
      ("BMPipe","IEEE CLUSTER 2025","Bubble–memory co-optimisation planner. 1.36× over Megatron-Even on 10K+ NPUs; ILP solves in under 200 ms."),
      ("H²O","Euro-Par 2025 · Best Poster","Holistic two-level hyper-parameter optimisation. +36.7% over the D-Rec baseline on 128 devices — without profiling."),
      ("ManuMatic","IFIP NPC 2025","Strategy injection for robust automatic hybrid parallelism. Up to 2.24× over D-Rec with expert parallelism."),
    ]
    tiles = "".join(f'<div class=tile><p class=ev>{v}</p><h3>{n}</h3><p>{b}</p>'
                    f'<a class=lnk href="#work">Learn more</a></div>' for n,v,b in SYS)
    pubs = "".join(f'<div class=pub><h4>{t}</h4><div class=pv>{v} · {a}</div></div>'
                   for a,t,v in PUBS)
    flinks = " · ".join(f'<a href="{u}">{tx}</a>' for tx,u in LINKS)
    body = f"""
<nav class=nav><div class=nav-in><span class=brand>Ruiwen WANG</span><span class=sp></span>
<a href="#work">Research</a><a href="#work">Systems</a><a href="#pubs">Publications</a><a href="{LINKS[0][1]}">Contact</a></div></nav>
<section class=hero><div class=wrapn>
<img src="{AV}" alt="">
<p class=eyebrow>PhD Candidate · AI Infra · LLM Pretraining</p>
<h1>Ruiwen WANG</h1>
<p class=sub>Profiling-free planning for hybrid-parallel LLM pretraining.</p>
<p class=cta><a class=btn href="#work">Read the work</a><a class=lnk href="{LINKS[0][1]}">Get in touch</a></p>
</div></section>
<section class=panel><div class=wrapn>
<h2>Research.</h2>
<p class=lead>Closed-form, hardware-parametric cost surfaces solved by lightweight ILPs — planning parallelism at foundation scale without per-cluster profiling, and staying portable when the hardware or model changes.</p>
</div></section>
<section class=dark><div class=wrapn>
<h2>Proven at scale.</h2>
<div class=stats>
<div><div class=num>10K+</div><div class=lab>Ascend-910 NPUs</div></div>
<div><div class="num accent">1.43×</div><div class=lab>MFU vs Megatron-LM</div></div>
<div><div class=num>&lt;200ms</div><div class=lab>ILP at production scale</div></div>
</div></div></section>
<section id=work><div class=wrapn style="max-width:980px">
<h2>Systems.</h2>
<p class=lead>Four planners built during the PhD — each a concrete production-readiness property.</p>
<div class=grid>{tiles}</div>
</div></section>
<section id=pubs class=panel><div class=wrapn>
<h2>Selected publications.</h2>
<div class=pubs>{pubs}</div>
</div></section>
<footer class=foot>© 2026 Ruiwen WANG · {flinks}</footer>
"""
    return page(css, body)

SKINS = [("01-editorial",editorial),("02-latex",latex),("03-tufte",tufte),
         ("04-swiss",swiss),("05-terminal",terminal),("06-air",air),
         ("07-brutalist",brutalist),("08-magazine",magazine),
         ("09-broadsheet",broadsheet),("10-glass",glass),("11-apple",apple)]

here = os.path.dirname(os.path.abspath(__file__))
for fid, fn in SKINS:
    with open(os.path.join(here, fid + ".html"), "w", encoding="utf-8") as f:
        f.write(fn())
print("wrote", len(SKINS), "previews")
