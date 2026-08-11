"""Generic CenseoAI-branded PDF generator.
Usage: python3 gen_branded_pdf.py <src.md> <out-base> "<title-html>" "<subtitle>" <repo-rel-dir>
"""
import markdown, re, sys, base64, pathlib, subprocess, posixpath

HERE = pathlib.Path(__file__).parent
REPO_ROOT = HERE.parent
SRC, OUT_BASE, TITLE, SUB, RELDIR = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]
REPO = "https://github.com/censeotc/claude-code-starter/blob/claude/ai-brain-webinar-guide-fbsoa7"

logo_uri = "data:image/png;base64," + base64.b64encode((REPO_ROOT / "docs/assets/censeoai-logo.png").read_bytes()).decode()
footer_logo_uri = "data:image/png;base64," + base64.b64encode((REPO_ROOT / "docs/assets/censeoai-logo-horizontal.png").read_bytes()).decode()

md = pathlib.Path(SRC).read_text()
body = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists"])

def fix_href(m):
    href = m.group(1)
    if href.startswith(("http://", "https://", "#", "mailto:")):
        return m.group(0)
    return f'href="{REPO}/{posixpath.normpath(posixpath.join(RELDIR, href))}"'

body = re.sub(r'href="([^"]+)"', fix_href, body)

css = """
@page { size: A4; margin: 22mm 18mm; }
@page :first { margin: 0; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
       font-size: 10.5pt; line-height: 1.55; color: #1c2333; margin: 0; }
.cover { page-break-after: always; position: relative; width: 210mm; height: 296mm;
         overflow: hidden; background: #fff; display: flex; flex-direction: column;
         justify-content: center; align-items: center; text-align: center; }
.streak { position: absolute; height: 14px; border-radius: 7px; transform: rotate(-38deg); }
.s-royal { background: linear-gradient(90deg, #0c2d8a, #1a4fd0); }
.s-cyan  { background: linear-gradient(90deg, #29abe2, #7fd0f2); }
.badge { width: 100mm; }
.tagline { font-size: 13pt; font-weight: 700; letter-spacing: 6px; color: #0c2d8a; margin-top: 4mm; }
.tagline .the { color: #29abe2; }
.cover-rule { width: 70mm; height: 3px; margin: 9mm auto;
              background: linear-gradient(90deg, #1a4fd0, #29abe2); border: none; }
.cover-title { font-size: 25pt; font-weight: 700; color: #0c2d8a; line-height: 1.25; margin: 0 14mm; }
.cover-sub { font-size: 11.5pt; color: #44506b; margin: 6mm auto 0; max-width: 130mm; }
.cover-meta { position: absolute; bottom: 9mm; left: 0; right: 0;
              font-size: 9.5pt; color: #44506b; letter-spacing: 1px; }
.cover-meta b { color: #1a4fd0; }
h1 { font-size: 20pt; line-height: 1.25; color: #0c2d8a; border-bottom: 3px solid;
     border-image: linear-gradient(90deg,#1a4fd0,#29abe2) 1; padding-bottom: 10px; }
h2 { font-size: 14.5pt; color: #0c2d8a; margin-top: 1.6em; border-bottom: 1px solid #c9d8f2;
     padding-bottom: 4px; page-break-after: avoid; }
h3 { font-size: 11.5pt; color: #1a4fd0; margin-top: 1.3em; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
a { color: #1a4fd0; text-decoration: none; }
strong { color: #0c2d8a; }
code { font-family: 'Consolas', 'Menlo', monospace; font-size: 9pt; background: #eaf3fc;
       border-radius: 3px; padding: 1px 4px; color: #0c2d8a; }
pre { background: #f4f8fd; border: 1px solid #c9d8f2; border-radius: 6px; padding: 10px 12px;
      overflow-x: hidden; white-space: pre-wrap; word-wrap: break-word; }
pre code { background: none; padding: 0; font-size: 8.6pt; line-height: 1.45; color: #1c2333; }
table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 9.3pt;
        page-break-inside: avoid; }
th { background: linear-gradient(90deg, #0c2d8a, #1a4fd0); color: #fff; text-align: left;
     padding: 6px 8px; font-weight: 600; }
td { border: 1px solid #c9d8f2; padding: 5px 8px; vertical-align: top; }
tr:nth-child(even) td { background: #f2f7fd; }
blockquote { margin: 0.9em 0; padding: 8px 14px; background: #eaf3fc;
             border-left: 4px solid #29abe2; border-radius: 0 6px 6px 0; page-break-inside: avoid; }
hr { border: none; border-top: 1px solid #c9d8f2; margin: 1.6em 0; }
.footer-note { margin-top: 2em; font-size: 8.5pt; color: #44506b;
               border-top: 2px solid #1a4fd0; padding-top: 8px; }
.footer-note b { color: #1a4fd0; }
"""

streaks = "".join(
    f'<div class="streak {c}" style="{pos}width:{w}mm;"></div>'
    for c, pos, w in [
        ("s-royal", "top:14mm;left:-18mm;", 60), ("s-cyan", "top:26mm;left:-30mm;", 55),
        ("s-royal", "top:36mm;left:-44mm;", 50), ("s-cyan", "bottom:36mm;right:-30mm;", 55),
        ("s-royal", "bottom:26mm;right:-44mm;", 60), ("s-cyan", "bottom:16mm;right:-18mm;", 50)])

cover = f"""<div class="cover">{streaks}
  <img class="badge" src="{logo_uri}" alt="CenseoAI">
  <div class="tagline">SCALE <span class="the">THE</span> PROVEN</div>
  <hr class="cover-rule">
  <div class="cover-title">{TITLE}</div>
  <div class="cover-sub">{SUB}</div>
  <div class="cover-meta"><b>CenseoAI</b> &nbsp;&middot;&nbsp; AI Design-Built for Revenue &nbsp;&middot;&nbsp; www.CenseoAI.ai &nbsp;&middot;&nbsp; July 2026</div>
</div>"""

footer_note = f'<div class="footer-note"><b>CenseoAI</b> &middot; Scale the Proven &middot; www.CenseoAI.ai &nbsp;|&nbsp; Source: {RELDIR}/{pathlib.Path(SRC).name if not SRC.startswith("/tmp") else "censeo-ai-brain repo"} &middot; generated 2026-07-25 &middot; links open on GitHub</div>'

cover_css = css.replace("@page { size: A4; margin: 22mm 18mm; }", "@page { size: A4; margin: 0; }")
(HERE / f"{OUT_BASE}-cover.html").write_text(
    f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>Cover</title><style>{cover_css}</style></head><body>{cover}</body></html>')
content_css = css.replace("@page { size: A4; margin: 22mm 18mm; }", "").replace("@page :first { margin: 0; }", "")
(HERE / f"{OUT_BASE}-content.html").write_text(
    f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>{re.sub("<[^>]+>", " ", TITLE)}</title><style>{content_css}</style></head><body>{body}{footer_note}</body></html>')

subprocess.run(["/opt/pw-browsers/chromium", "--headless", "--no-sandbox", "--disable-gpu",
                "--no-pdf-header-footer", f"--print-to-pdf={HERE}/{OUT_BASE}-cover.pdf",
                str(HERE / f"{OUT_BASE}-cover.html")], check=True, capture_output=True)

from playwright.sync_api import sync_playwright
footer = f'<div style="width:100%; box-sizing:border-box; padding:0 18mm 5mm 0; text-align:right; font-size:8px;"><img src="{footer_logo_uri}" style="height:8mm;"></div>'
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium", args=["--no-sandbox"])
    page = browser.new_page()
    page.goto((HERE / f"{OUT_BASE}-content.html").as_uri())
    page.pdf(path=str(HERE / f"{OUT_BASE}-content.pdf"), format="A4",
             margin={"top": "22mm", "bottom": "26mm", "left": "18mm", "right": "18mm"},
             display_header_footer=True, header_template="<span></span>", footer_template=footer,
             print_background=True, prefer_css_page_size=False)
    browser.close()

subprocess.run(["qpdf", "--empty", "--pages", f"{HERE}/{OUT_BASE}-cover.pdf",
                f"{HERE}/{OUT_BASE}-content.pdf", "--", f"{HERE}/{OUT_BASE}.pdf"], check=True)
print(f"done: {OUT_BASE}.pdf")
