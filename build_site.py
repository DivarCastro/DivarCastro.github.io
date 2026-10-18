# -*- coding: utf-8 -*-
"""Genera el sitio (ES/EN/PT) y los 3 PDFs a partir de content.py.
Sitio:  python build_site.py
PDFs:   python build_site.py --pdf   (requiere: pip install playwright && playwright install chromium)
"""
import sys, pathlib, html
from content import L, LINKS, PUBS, REFS

ROOT = pathlib.Path(__file__).parent.resolve()
e = html.escape
PAGES = {"es": ("index.html", "cv.html", "CV_Divar_Castro_Rodas_2026.pdf"),
         "en": ("en/index.html", "cv_en.html", "CV_Divar_Castro_Rodas_2026_EN.pdf"),
         "pt": ("pt/index.html", "cv_pt.html", "CV_Divar_Castro_Rodas_2026_PT.pdf")}

def pub_html(p, cls="pub", year=False):
    y, au, ti, jo, doi = p
    pre = f'<span class="year">{y}</span> · ' if year else ''
    return (f'<p class="{cls}">{pre}{e(au)} ({y}). <em>{e(ti)}</em> {e(jo)} '
            f'<a href="https://doi.org/{doi}">DOI</a></p>')

def ref_role(t, i):
    return t["ref_role"] if i < 2 else t["ref_role_m"]

# ---------------------------------------------------------------- SITIO
def site(code):
    t = L[code]; sub = code != "es"; up = "../" if sub else ""
    lang_links = []
    for c in ("es", "en", "pt"):
        href = {"es": up or "./", "en": ("./" if code == "en" else up + "en/"), "pt": ("./" if code == "pt" else up + "pt/")}[c]
        cur = ' class="cur" aria-current="true"' if c == code else ''
        lang_links.append(f'<a href="{href}" hreflang="{c}"{cur}>{c.upper()}</a>')
    nav = "".join(f'<a href="#{i}">{e(n)}</a>' for i, n in t["nav"])
    jobs = "".join(
        f'<div class="card"><h3>{e(j[0])} — {e(j[1])}</h3><p class="meta">{e(j[2].replace(" | ", " · "))}</p><ul>' +
        "".join(f"<li>{e(b)}</li>" for b in t["jobs_web"][k]) + "</ul></div>" for k, j in enumerate(t["jobs"]))
    projs = "".join(
        f'<div class="card"><h3>{e(p[0])}</h3><p class="meta">{e(p[1])}</p><p>{e(p[2])}' +
        (f' <a href="{p[3]}">{p[3].replace("https://","")}</a>' if p[3] else "") + "</p></div>" for p in t["projects"])
    evs = "".join(f'<li><strong>{e(a)}</strong> — {e(b)}</li>' for a, b in t["events"])
    edu = "".join(f'<div class="card"><h3>{e(a)} — {e(b)}</h3><p class="meta">{e(c)}' + (" · " + e(d[0]) if d else "") + "</p></div>" for a, b, c, d in t["edu"])
    aw = "".join(f'<li><span class="year">{y}</span> — {e(x)}</li>' for y, x in t["awards"])
    tags = lambda xs: "".join(f"<span>{e(x)}</span>" for x in xs)
    li = lambda xs: "".join(f"<li>{e(x)}</li>" for x in xs)
    return f'''<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(t["title"])}</title>
<meta name="description" content="{e(t["desc"])}">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<nav><div class="in">
  <a href="#about"><strong>DCR</strong></a>{nav}
  <span class="sp"></span><div class="lang" aria-label="Language">{"".join(lang_links)}</div>
</div></nav>
<main>
<header class="hero" id="about">
  <div class="avatar"><img src="{up}assets/foto.jpg" alt="Divar Castro Rodas" onerror="this.replaceWith('DC')"></div>
  <div>
    <h1>Divar Castro Rodas</h1>
    <p class="role">{e(t["role"])}<br>{e(t["affil"])}</p>
    <div class="links">
      <a href="mailto:{LINKS["email"]}">{t["email_lbl"]}</a>
      <a href="{LINKS["github"]}">GitHub</a>
      <a href="{LINKS["linkedin"]}">LinkedIn</a>
      <a href="{LINKS["orcid"]}">ORCID</a>
      <a href="{LINKS["rg"]}">ResearchGate</a>
      <a href="{LINKS["lattes"]}">Lattes</a>
      <a href="{up}assets/{PAGES[code][2]}">{t["pdf_btn"]}</a>
    </div>
  </div>
</header>
<section><h2>{t["h"]["about"]}</h2><p>{e(t["about"][0])}</p>
  <div class="grid">
    <div class="card"><h3>{t["h"]["skills"]}</h3><div class="tags" style="margin-top:8px">{tags(t["skills_web"])}</div></div>
    <div class="card"><h3>{t["h"]["lang"]}</h3><ul>{li(t["langs"])}</ul></div>
    <div class="card"><h3>{t["h"]["interests"]}</h3><div class="tags" style="margin-top:8px">{tags(t["interests"])}</div></div>
  </div></section>
<section id="experiencia"><h2>{t["h"]["exp"]}</h2>{jobs}</section>
<section id="proyectos"><h2>{t["h"]["proj"]}</h2><div class="grid">{projs}</div></section>
<section id="publicaciones"><h2>{t["h"]["pubs"]}</h2>{"".join(pub_html(p, year=True) for p in PUBS)}</section>
<section id="ponencias"><h2>{t["h"]["talks"]}</h2><div class="card"><ul>{evs}</ul></div></section>
<section id="educacion"><h2>{t["h"]["edu"]}</h2>{edu}
  <div class="card"><h3>{t["h"]["selcourses"]}</h3><ul>{li(t["courses_web"])}</ul></div></section>
<section id="reconocimientos"><h2>{t["h"]["awards"]}</h2><div class="card"><ul>{aw}</ul></div></section>
</main>
<footer>© <span id="y"></span> Divar Castro Rodas · {e(t["footer"])}</footer>
<script src="{up}script.js"></script>
</body>
</html>
'''

# ---------------------------------------------------------------- CV (PDF)
CV_CSS = (ROOT / "cv.css").read_text(encoding="utf-8")

def cv(code):
    t = L[code]; h = t["h"]
    li = lambda xs: "".join(f"<li>{e(x)}</li>" for x in xs)
    jobs = "".join(
        f'<p class="job">{e(j[0])} <span>— {e(j[1])}</span></p><p class="when">{e(j[2])}</p><ul>{li(j[3])}</ul>' for j in t["jobs"])
    edu = "".join(
        f'<p class="job">{e(a)} <span>— {e(b)}</span></p><p class="when">{e(c)}</p>' + (f"<ul>{li(d)}</ul>" if d else "")
        for a, b, c, d in t["edu"])
    ev = lambda lst: "".join(f'<p class="ev"><b>{e(a)}</b> — {e(b)}</p>' for a, b in lst)
    refs = "".join(f'<p class="ev"><b>{e(n)}</b> — {e(ref_role(t, i))}, {e(inst)} | {e(m)}</p>' for i, (n, inst, m) in enumerate(REFS))
    aw = "".join(f"<li>{e(x)}</li>" if y.startswith("20") and False else f"<li>{e(x)}</li>" for y, x in t["awards"])
    return f'''<!doctype html>
<html lang="{code}"><head><meta charset="utf-8"><title>CV Divar Castro Rodas 2026 ({code.upper()})</title>
<style>{CV_CSS}</style></head><body>
<div class="page">
<header><img class="ph" src="assets/foto.jpg" alt=""><div><h1>DIVAR CASTRO RODAS</h1><p>{e(t["role_full"])}</p></div></header>
<aside>
  <h3>{h["contact"]}</h3>
  <p>{LINKS["email"]}</p><p>Guayaquil, {"Equador" if code=="pt" else "Ecuador"}</p>
  <p><a href="{LINKS["linkedin"]}">LinkedIn: /in/divar-castro-rodas</a></p>
  <p><a href="{LINKS["orcid"]}">ORCID: 0000-0002-2197-2277</a></p>
  <p><a href="{LINKS["lattes"]}">Lattes (CNPq)</a></p>
  <p><a href="{LINKS["rg"]}">ResearchGate</a></p>
  <p><a href="{LINKS["github"]}">GitHub: /DivarCastro</a></p>
  <h3>{h["lang"]}</h3>{"".join(f"<p>{e(x)}</p>" for x in t["langs"])}
  <h3>{h["skills"]}</h3><ul>{li(t["skills"])}</ul>
  <h3>{h["soft"]}</h3><ul>{li(t["soft"])}</ul>
  <h3>{h["interests"]}</h3><ul>{li(t["interests"])}</ul>
</aside>
<main>
  <h2>{h["profile"]}</h2><p style="text-align:justify;margin:0">{e(t["about"][0])}</p>
  <h2>{h["expcv"]}</h2>{jobs}
</main></div>
<div class="page" style="grid-template-rows:1fr"><aside class="blank"></aside><main>
  <h2>{h["educv"]}</h2>{edu}
  <h2>{h["pubs"]}</h2>{"".join(pub_html(p) for p in PUBS)}
  <h2>{h["talkscv"]}</h2>{ev(t["events"][:6])}
</main></div>
<div class="page" style="grid-template-rows:1fr"><aside class="blank"></aside><main>
  {ev(t["events"][6:])}
  <h2>{h["courses"]}</h2><ul class="small">{li(t["courses"])}</ul>
  <h2>{h["awards"]}</h2><ul>{aw}</ul>
  <h2>{h["refs"]}</h2>{refs}
</main></div>
</body></html>
'''

def main(pdf=False):
    for code, (idx, cvf, pdff) in PAGES.items():
        p = ROOT / idx; p.parent.mkdir(exist_ok=True)
        p.write_text(site(code), encoding="utf-8")
        (ROOT / cvf).write_text(cv(code), encoding="utf-8")
        print("OK", idx, cvf)
    if pdf:
        from playwright.sync_api import sync_playwright
        (ROOT / "assets").mkdir(exist_ok=True)
        with sync_playwright() as pw:
            b = pw.chromium.launch(); pg = b.new_page()
            for code, (idx, cvf, pdff) in PAGES.items():
                pg.goto((ROOT / cvf).as_uri()); pg.wait_for_load_state("networkidle")
                pg.pdf(path=str(ROOT / "assets" / pdff), format="Letter", print_background=True,
                       margin=dict(top="0", right="0", bottom="0", left="0"))
                print("PDF", pdff)
            b.close()

if __name__ == "__main__":
    main("--pdf" in sys.argv)
