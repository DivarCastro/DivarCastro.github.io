"""Genera assets/CV_Divar_Castro_Rodas_2026.pdf a partir de cv.html.
Uso (una vez):  pip install playwright && playwright install chromium
Luego:          python build_pdf.py
"""
import pathlib
from playwright.sync_api import sync_playwright

root = pathlib.Path(__file__).parent.resolve()
out = root / "assets" / "CV_Divar_Castro_Rodas_2026.pdf"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto((root / "cv.html").as_uri())
    pg.wait_for_load_state("networkidle")
    pg.pdf(path=str(out), format="Letter", print_background=True,
           margin=dict(top="0", right="0", bottom="0", left="0"))
    b.close()
print("PDF generado:", out)
