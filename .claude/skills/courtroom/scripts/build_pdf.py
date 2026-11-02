#!/usr/bin/env python3
"""One PDF for two BIOCON hearings: a comparison cover, then each hearing's report page.

    python build_pdf.py <analyst-session> <soic-session> <out.pdf>

The cover is built from each session's dashboard.json and hearing.md (counts come from the files). Each report page is printed from its
report.html with every issue opened, by headless Chromium through Node's playwright. Pages are merged with pypdf.
"""
import html
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_hearing as chk  # noqa: E402
from pypdf import PdfWriter  # noqa: E402

PRINT_JS = """
const {chromium}=require('playwright');
(async()=>{const [,, src, out] = process.argv;
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1100,height:1400}});
await p.goto('file://'+src);await p.waitForTimeout(1500);
await p.evaluate(()=>{document.querySelectorAll('details').forEach(d=>d.open=true);
  const s=document.createElement('style');s.textContent='.strip{display:none!important} .qrow{break-inside:avoid} body{background:var(--bg)}';document.head.appendChild(s);});
await p.waitForTimeout(500);
await p.pdf({path:out,width:'1100px',height:'1560px',printBackground:true,margin:{top:'24px',bottom:'24px',left:'0',right:'0'}});
await b.close();})();
"""


def facts(session: Path) -> dict:
    d = json.loads((session / "dashboard.json").read_text(encoding="utf-8"))["decision"]
    turns = chk.parse_turns((session / "hearing.md").read_text(encoding="utf-8"))
    qs = [t for t in turns if t["role"] == "Lawyer" and re.match(r"^Q\d+ ", t["id"]) and re.match(r"I\d+", t["section"])]
    issues = sorted({re.match(r"I\d+", t["section"]).group() for t in qs}, key=lambda s: int(s[1:]))
    return {"d": d, "questions": len(qs), "issues": issues, "cross": sum(1 for t in turns if t["role"] == "Lawyer" and re.match(r"^X\d+ ", t["id"]))}


def cover(a: dict, s: dict) -> str:
    rows = []
    for ra, rs in zip(a["d"]["scores"], s["d"]["scores"]):
        rows.append("<tr><td>%s %s</td><td>%s</td><td>%s</td></tr>" % (ra["section"], html.escape(ra["name"]), "%s said %s, final %d" % ("judge", ra["judge"], ra["final"]), "%s said %s, final %d" % ("judge", rs["judge"], rs["final"])))
    cut_a = [r for r in a["d"]["scores"] if r["cut"]]
    cut_s = [r for r in s["d"]["scores"] if r["cut"]]
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>BIOCON two courtrooms</title><style>
:root{{--ink:#131d2b;--muted:#566274;--line:#d0d7e0;--accent:#0e5a6b;--bg:#fafbfc}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 "Source Sans 3",system-ui,sans-serif;padding:48px 64px}}
h1{{font:700 34px Georgia,serif;margin:0 0 6px}} h2{{font:700 20px Georgia,serif;margin:30px 0 8px}}
.sub{{color:var(--muted);margin:0 0 22px}} table{{border-collapse:collapse;width:100%;margin:8px 0 14px}}
th,td{{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}} th{{color:var(--muted);font-weight:600;font-size:13px}}
.big{{display:flex;gap:40px;margin:10px 0}} .big div{{flex:1;border:1px solid var(--line);border-radius:8px;padding:14px 18px}} .big b{{font:700 30px Georgia,serif;display:block}}
ul{{margin:6px 0 6px 20px}} li{{margin:3px 0}} .note{{border-left:3px solid var(--accent);padding:4px 14px;color:var(--muted);margin:14px 0}}
</style></head><body>
<h1>BIOCON: two hearings, two lawyers</h1>
<p class="sub">The same case book, the same BIOCON record seat as convict and the same judge. Only the lawyer changes: the Indian market analyst seat, then the SOIC course seat. A simulation built from public filings; not advice and not a SEBI-registered adviser.</p>
<div class="big"><div><b>{a['d']['position']['label']}, trust {a['d']['total']} of 21</b>Analyst as lawyer ({len(a['issues'])} issues, {a['questions']} questions, {a['cross']} cross questions)</div>
<div><b>{s['d']['position']['label']}, trust {s['d']['total']} of 21</b>SOIC seat as lawyer ({len(s['issues'])} issues, {s['questions']} questions, {s['cross']} cross questions)</div></div>
<h2>Scores by section</h2>
<table><tr><th>Section</th><th>Analyst as lawyer</th><th>SOIC seat as lawyer</th></tr>{''.join(rows)}</table>
<p>Code caps each score by the states of the deciding question. Analyst hearing: {len(cut_a)} score(s) cut by code ({', '.join(r['section'] for r in cut_a) or 'none'}). SOIC hearing: {len(cut_s)} cut ({', '.join(r['section'] for r in cut_s) or 'none'}).</p>
<h2>Read this before comparing the two</h2>
<ul>
<li>This is not a controlled test. The Analyst hearing heard {len(a['issues'])} issues ({a['issues'][0]} to {a['issues'][-1]}) with a fixed three questions each; the SOIC hearing heard all ten issues with four each. Sections with no questions heard score 0, so the totals are not like for like.</li>
<li>Both hearings end at Wait. Neither lifts BIOCON above the trust bar of 12 for "trust good" or 18 for Buy; the main cause in both is the same: the decisive questions on debt, cash and related parties had no figure in the record.</li>
<li>The SOIC lawyer cited course sources (23 different ids) for every question; the guard checks the ids exist in its own brain, not that they fit the question.</li>
<li>The SOIC lawyer's freedom to ask 2 to 5 questions per issue was not used: every issue ended at 4.</li>
<li>The first SOIC closings were rewritten after they labelled two points answered that the judge scored no data. The judge's final was not re-run afterwards.</li>
<li>The trust bands (0 to 6, 7 to 11, 12 to 17, 18 to 21) are the seat's own, uncalibrated.</li>
</ul>
<div class="note">Pages that follow: (1) the Analyst-as-lawyer hearing report, (2) the SOIC-as-lawyer hearing report, each with every issue opened.</div>
</body></html>"""


def to_pdf(src: Path, out: Path) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(PRINT_JS)
    subprocess.run(["node", f.name, str(src.resolve()), str(out)], check=True, env={**__import__("os").environ, "NODE_PATH": subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()})


def main(analyst: Path, soic: Path, out: Path) -> None:
    tmp = Path(tempfile.mkdtemp())
    cover_html = tmp / "cover.html"
    cover_html.write_text(cover(facts(analyst), facts(soic)), encoding="utf-8")
    parts = [("cover", cover_html), ("analyst", analyst / "report.html"), ("soic", soic / "report.html")]
    w = PdfWriter()
    for name, src in parts:
        pdf = tmp / f"{name}.pdf"
        to_pdf(src, pdf)
        w.append(str(pdf), outline_item={"cover": "Comparison", "analyst": "Analyst as lawyer", "soic": "SOIC seat as lawyer"}[name])
    w.write(str(out))


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
