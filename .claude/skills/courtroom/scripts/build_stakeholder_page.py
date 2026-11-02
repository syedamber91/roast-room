#!/usr/bin/env python3
"""Build the stakeholder 'Receipts' page and its one-sheet from the checked data.

    python build_stakeholder_page.py <stakeholder-dir> <appendix-url>

Reads data.json, flags-merged.json, rows-plain.json (all checked by verify_plain.py) and writes receipts.html (the interactive page with a
Kid / Teen / Expert switch) and sheet.html (the one-sheet for printing). Every sentence on the page is either copied from the hearings
or is a plain-words line that verify_plain.py checked against its source.
"""
import html
import json
import sys
from pathlib import Path

ISSUES = [f"I{n}" for n in range(1, 11)]
FONTS = "https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Young+Serif&display=swap"

CSS = """
:root{--bg:#f4f1f7;--surface:#ffffff;--ink:#1c1530;--muted:#5d5673;--line:#dcd5e8;--accent:#5b2a86;--accent-soft:#ece2f6;
--full:#1f7a4d;--full-bg:#dff3e8;--torn:#a86400;--torn-bg:#fbeccc;--empty:#6b6880;--empty-bg:#e9e7ef;
--f-body:"Atkinson Hyperlegible",system-ui,sans-serif;--f-head:"Young Serif",Georgia,serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#14101c;--surface:#1e1829;--ink:#efeaf8;--muted:#a79fbd;--line:#352d47;--accent:#c9a2ee;--accent-soft:#2b2040;
--full:#6fd6a0;--full-bg:#173a2a;--torn:#f0b45a;--torn-bg:#3d2c10;--empty:#a9a5bd;--empty-bg:#2a2638;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#14101c;--surface:#1e1829;--ink:#efeaf8;--muted:#a79fbd;--line:#352d47;--accent:#c9a2ee;--accent-soft:#2b2040;
--full:#6fd6a0;--full-bg:#173a2a;--torn:#f0b45a;--torn-bg:#3d2c10;--empty:#a9a5bd;--empty-bg:#2a2638;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 var(--f-body);padding-block:0}
.wrap{max-width:1080px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-bottom:48px}
h1,h2,h3{font-family:var(--f-head);font-weight:400;margin:0;text-wrap:balance}
h1{font-size:clamp(1.8rem,4vw,2.6rem);line-height:1.15} h2{font-size:1.5rem;margin:34px 0 6px} h3{font-size:1.1rem}
.sub{color:var(--muted);margin:6px 0 14px;max-width:62ch}
.banner{background:var(--accent-soft);border-radius:8px;padding:10px 14px;font-size:.92rem}
.bar{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);padding:10px 0;display:flex;gap:10px;align-items:center;flex-wrap:wrap;border-bottom:1px solid var(--line)}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden}
.seg button{font:inherit;background:var(--surface);color:var(--ink);border:0;padding:8px 16px;cursor:pointer}
.seg button[aria-pressed="true"]{background:var(--accent);color:var(--bg);font-weight:700}
.seg button:focus-visible,.exp:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.lead{font-size:1.05rem;max-width:62ch}
.lamps{display:grid;gap:8px;margin:12px 0}
.lrow{display:grid;grid-template-columns:7.5rem repeat(7,minmax(0,1fr));gap:6px;align-items:end}
.lrow .who{font-weight:700;font-size:.9rem}
.lamp{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:8px 4px;text-align:center;font-size:.72rem;color:var(--muted);min-width:0}
.lamp i{display:block;width:22px;height:22px;border-radius:50%;margin:0 auto 4px;border:3px solid var(--empty);background:var(--empty-bg)}
.lamp.l1 i{border-color:var(--torn);background:var(--torn-bg)} .lamp.l2 i,.lamp.l3 i{border-color:var(--full);background:var(--full-bg)}
.lamp.l3 i{box-shadow:0 0 0 3px var(--full-bg)}
.lamp b{display:block;color:var(--ink);font-size:.78rem}
.total{display:flex;flex-wrap:wrap;gap:16px;margin:8px 0}
.total div{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:10px 16px}
.total b{font:400 1.7rem var(--f-head);display:block}
.legend{display:flex;flex-wrap:wrap;gap:14px;margin:10px 0}
.stamp{display:inline-flex;align-items:center;gap:8px;border-radius:8px;padding:4px 10px 4px 6px;font-weight:700;font-size:.9rem}
.stamp svg{width:26px;height:30px;flex:none}
.stamp.full{background:var(--full-bg);color:var(--full)} .stamp.torn{background:var(--torn-bg);color:var(--torn)} .stamp.empty{background:var(--empty-bg);color:var(--empty)}
.row{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:12px 0}
.row h3{margin-bottom:10px}
.pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.side{border-top:3px solid var(--line);padding-top:8px;min-width:0}
.side .tag{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.q{font-weight:700;margin:4px 0} .a{margin:6px 0} .settle{color:var(--muted);font-size:.92rem;margin-top:6px}
.nask{color:var(--muted);font-style:italic}
.src{font-size:.8rem;color:var(--muted)}
.exp{font:inherit;color:var(--accent);background:none;border:0;padding:6px 0;cursor:pointer;text-decoration:underline}
.more{border-top:1px dashed var(--line);margin-top:8px;padding-top:8px;font-size:.92rem}
.more div{margin:8px 0}
.flag{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:10px 0;display:grid;gap:4px}
.found{display:inline-block;border-radius:999px;padding:1px 10px;font-size:.78rem;font-weight:700;background:var(--accent-soft);color:var(--accent)}
.found.both{background:var(--accent);color:var(--bg)}
.foot{margin-top:34px;color:var(--muted);font-size:.9rem}
@media (max-width:760px){.pair{grid-template-columns:1fr}.lrow{grid-template-columns:repeat(7,minmax(0,1fr))}.lrow .who{grid-column:1/-1}.lamp{font-size:.62rem}}
@media print{.bar,.exp{display:none}.more{display:block!important}body{background:#fff}}
"""

JS = """
const D=JSON.parse(document.getElementById('data').textContent);
const LV={kid:'Kid',teen:'Teen',expert:'Expert'};
let level=(location.hash||'#teen').slice(1); if(!LV[level])level='teen';
const STAMP={answered:['full','Full receipt','shown a number and a date'],partial:['torn','Torn receipt','words, but no number'],'no data':['empty','No receipt','nothing on record'],deflected:['empty','Turned aside','the question was turned aside'],unverified:['torn','Unchecked receipt','a figure that could not be checked']};
const SVG={full:'<svg viewBox="0 0 26 30" aria-hidden="true"><path d="M3 2h20v26l-3-2-3 2-4-2-4 2-3-2-3 2z" fill="currentColor" opacity=".18" stroke="currentColor" stroke-width="1.6"/><path d="M8 11l3 3 7-7" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M8 19h10M8 23h7" stroke="currentColor" stroke-width="1.6"/></svg>',
torn:'<svg viewBox="0 0 26 30" aria-hidden="true"><path d="M3 2h20v14l-4 3 4 3v6l-3-2-3 2-4-2-4 2-3-2-3 2z" fill="currentColor" opacity=".18" stroke="currentColor" stroke-width="1.6" stroke-dasharray="0"/><path d="M8 9h10M8 13h6" stroke="currentColor" stroke-width="1.6"/></svg>',
empty:'<svg viewBox="0 0 26 30" aria-hidden="true"><path d="M3 2h20v26l-3-2-3 2-4-2-4 2-3-2-3 2z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="3 3"/></svg>'};
function el(t,c,x){const e=document.createElement(t);if(c)e.className=c;if(x!==undefined)e.textContent=x;return e}
function stamp(state){const s=STAMP[state]||STAMP['no data'];const e=el('span','stamp '+s[0]);e.innerHTML=SVG[s[0]];e.append(el('span','',level==='kid'?s[1]:s[1]+' ('+s[2]+')'));return e}
function pick(r,k,e){return level==='expert'?e:(r.plain?r.plain[level+'_'+k]:e)}
function render(){
 document.querySelectorAll('.seg button').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.l===level)));
 const L=document.getElementById('lamps');L.textContent='';
 for(const k of ['analyst','soic']){const d=D[k];const row=el('div','lrow');row.append(el('div','who',k==='analyst'?'Analyst as lawyer':'SOIC seat as lawyer'));
  for(const x of d.lamps){const l=el('div','lamp l'+x.final);l.append(el('i'));l.append(el('b','',x.section));l.append(el('span','',level==='kid'?'':x.name));row.append(l)}L.append(row)}
 const T=document.getElementById('total');T.textContent='';
 for(const k of ['analyst','soic']){const d=D[k];const t=el('div');t.append(el('b','',d.total+' of 21'));
  t.append(el('span','',(k==='analyst'?'Analyst: ':'SOIC: ')+(level==='kid'?'not enough proof yet':'position '+d.position)));T.append(t)}
 const R=document.getElementById('rows');R.textContent='';
 for(const it of D.issues){const row=el('div','row');row.append(el('h3','',it.id+' '+it.name));const pair=el('div','pair');
  for(const k of ['analyst','soic']){const s=it[k];const side=el('div','side');side.append(el('div','tag',k==='analyst'?'Analyst asked':'SOIC asked'));
   if(!s){side.append(el('p','nask','Not asked in this hearing.'));pair.append(side);continue}
   side.append(el('div','q',pick(s,'q',s.question)));side.append(stamp(s.state));
   const a=el('p','a',pick(s,'a',s.answer));side.append(a);
   if(level==='expert'&&s.answer_turn)side.append(el('div','src','BIOCON, '+s.answer_turn+' (first sentence, word for word)'));
   if(s.watch)side.append(el('div','settle',(level==='kid'?'What would help: ':'What would settle it: ')+pick(s,'settle',s.watch)));
   pair.append(side)}
  row.append(pair);
  const more=el('div','more');more.hidden=true;
  for(const k of ['analyst','soic']){const s=it[k];if(!s||!s.others.length)continue;more.append(el('b','',(k==='analyst'?'Analyst':'SOIC')+' follow-up questions, full wording'));
   for(const o of s.others){const d=el('div');d.append(el('div','',o.question));d.append(stamp(o.state));if(o.answer)d.append(el('div','src','BIOCON: '+o.answer));more.append(d)}}
  const b=el('button','exp','Show every question and answer');b.setAttribute('aria-expanded','false');
  b.onclick=()=>{more.hidden=!more.hidden;b.setAttribute('aria-expanded',String(!more.hidden));b.textContent=more.hidden?'Show every question and answer':'Hide the other questions'};
  row.append(b,more);R.append(row)}
 const F=document.getElementById('flags');F.textContent='';
 for(const f of D.flags){const c=el('div','flag');const tag=el('span','found '+(f.found_by==='both'?'both':''),f.found_by==='both'?'Found by both lawyers':(f.found_by==='analyst'?'Found by the Analyst only':'Found by the SOIC seat only'));
  c.append(tag);c.append(el('b','',f.topic));c.append(el('div','',level==='kid'?f.kid:(level==='teen'?f.teen:f.text)));
  if(level!=='kid')c.append(el('div','settle','What would settle it: '+f.settles_with));
  if(level==='expert')c.append(el('div','src','Judge lines: '+f.members.join(', ')));F.append(c)}
 const G=document.getElementById('legend');G.textContent='';for(const st of ['answered','partial','no data'])G.append(stamp(st));
 const L2=document.getElementById('lead');L2.textContent=level==='kid'?D.lead.kid:(level==='teen'?D.lead.teen:D.lead.expert);
 history.replaceState(null,'','#'+level)}
document.querySelectorAll('.seg button').forEach(b=>b.onclick=()=>{level=b.dataset.l;render()});
render();
"""


def blob(folder: Path, appendix: str) -> dict:
    d = json.loads((folder / "data.json").read_text(encoding="utf-8"))
    flags = json.loads((folder / "flags-merged.json").read_text(encoding="utf-8"))
    plain = {p["key"]: p for p in json.loads((folder / "rows-plain.json").read_text(encoding="utf-8"))}
    issues = []
    for iid in ISSUES:
        item = {"id": iid, "name": (d["soic"]["issues"].get(iid) or d["analyst"]["issues"].get(iid))["name"]}
        for side in ("analyst", "soic"):
            r = d[side]["issues"].get(iid)
            if not r or "1" not in r["qa"]:
                item[side] = None
                continue
            q1 = r["qa"]["1"]
            item[side] = {"question": q1.get("question", ""), "answer": q1.get("answer", ""), "answer_turn": f"{iid} {q1.get('answer_turn', '')}".strip(), "state": q1.get("state", ""),
                          "watch": r["watch"], "plain": {k: v for k, v in plain.get(f"{iid}-{side}", {}).items() if k != "key"},
                          "others": [{"question": v.get("question", ""), "answer": v.get("answer", ""), "state": v.get("state", "")} for n, v in sorted(r["qa"].items(), key=lambda x: int(x[0])) if int(n) > 1]}
        issues.append(item)
    t_a, t_s = d["analyst"], d["soic"]
    lead = {"kid": "A company has to show its receipts, a number and a date. Here is who showed theirs.",
            "teen": f"Two lawyers questioned BIOCON's management in a mock court. A claim counts only with a receipt: a number and a date. Both hearings ended at {t_a['position']}, trust {t_a['total']} and {t_s['total']} of 21.",
            "expert": f"Two hearings, one record: Analyst-as-lawyer (7 issues, {t_a['total']}/21) and SOIC-as-lawyer (10 issues, {t_s['total']}/21), both {t_s['position']}. Rows show each lawyer's decisive question, the convict's first sentence verbatim, the judge's state, and the document that would settle it."}
    return {"analyst": {k: t_a[k] for k in ("lamps", "total", "position")}, "soic": {k: t_s[k] for k in ("lamps", "total", "position")}, "issues": issues, "flags": flags, "lead": lead, "appendix": appendix}


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="claude:viewport-fit-sides" content="cover"><title>BIOCON Receipts</title>
<link rel="stylesheet" href="%(fonts)s"><style>%(css)s</style></head><body><div class="wrap">
<header style="padding-top:24px"><h1>BIOCON: did management show its receipts?</h1>
<p class="lead" id="lead"></p>
<div class="banner">A simulation built from public filings. It is not advice and not a SEBI-registered adviser. It says how well the defence held up on the record, never whether to buy, sell or hold.</div></header>
<div class="bar"><span>Read it as</span><span class="seg" role="group" aria-label="Reading level"><button data-l="kid" aria-pressed="false">Kid</button><button data-l="teen" aria-pressed="true">Teen</button><button data-l="expert" aria-pressed="false">Expert</button></span></div>
<h2>Seven lamps</h2><p class="sub">Each lamp is one kind of trust. Dark means the deciding question had no receipt.</p>
<div class="lamps" id="lamps"></div><div class="total" id="total"></div>
<div class="legend" id="legend"></div>
<h2>Red flags</h2><p class="sub">One list from both hearings. The tag says which lawyer found each one.</p><div id="flags"></div>
<h2>The ten questions that matter</h2><p class="sub">Left: the Analyst's question. Right: the SOIC seat's question. Under each: what BIOCON's management said, and the receipt.</p><div id="rows"></div>
<div class="foot"><p>Appendix: the full hearings, every question and answer, are in the long report: <a href="%(appendix)s">open the full report</a>. The one-sheet and the 124-page PDF carry the same record.</p>
<p>Plain-words lines for Kid and Teen are written by a model and checked by code against their source: no figure may appear that is not in the source, and none may use a buy, sell or hold word. A person should read them before sharing.</p></div>
</div><script type="application/json" id="data">%(data)s</script><script>%(js)s</script></body></html>"""

SHEET_CSS = """body{font:11px/1.4 var(--f-body);padding:18px 24px;max-width:none}.sheet h1{font-size:20px}.sheet h2{font-size:14px;margin:12px 0 4px}
.r{display:grid;grid-template-columns:2.2rem 1fr 1fr;gap:8px;border-top:1px solid var(--line);padding:4px 0}.r b{font-size:11px}.st{font-weight:700}
.st.answered{color:var(--full)}.st.partial{color:var(--torn)}.st.no{color:var(--empty)}.fl{border-top:1px solid var(--line);padding:3px 0}"""


def sheet(b: dict) -> str:
    stm = {"answered": "full receipt", "partial": "torn receipt", "no data": "no receipt", "deflected": "turned aside", "unverified": "unchecked"}

    def cell(s):
        if not s:
            return "<i>not asked</i>"
        q = html.escape(s["plain"].get("teen_q") or s["question"])
        a = html.escape(s["plain"].get("teen_a") or s["answer"])
        return f'<b>{q}</b><br><span class="st {s["state"].split()[0]}">{stm.get(s["state"], s["state"])}</span> {a}'
    rows = "".join(f'<div class="r"><b>{i["id"]}</b><div>{cell(i["analyst"])}</div><div>{cell(i["soic"])}</div></div>' for i in b["issues"])
    flags = "".join(f'<div class="fl"><b>{html.escape(f["topic"])}</b> ({f["found_by"]}): {html.escape(f["teen"])}</div>' for f in b["flags"])
    lamps = "".join(f'<p><b>{n}</b>: ' + " ".join(f'{x["section"]} {x["final"]}/3' for x in b[k]["lamps"]) + f' = {b[k]["total"]} of 21, {b[k]["position"]}</p>' for k, n in (("analyst", "Analyst as lawyer"), ("soic", "SOIC seat as lawyer")))
    return f'<!doctype html><html><head><meta charset="utf-8"><title>BIOCON one-sheet</title><link rel="stylesheet" href="{FONTS}"><style>{CSS}{SHEET_CSS}</style></head><body><div class="sheet"><h1>BIOCON: did management show its receipts?</h1><p>A simulation built from public filings; not advice. Receipt = a number and a date.</p><h2>Lamps</h2>{lamps}<h2>Red flags (both hearings)</h2>{flags}<h2>The ten questions: Analyst | SOIC seat</h2>{rows}</div></body></html>'


def main(folder: Path, appendix: str) -> None:
    b = blob(folder, appendix)
    page = PAGE % {"fonts": FONTS, "css": CSS, "appendix": appendix, "data": json.dumps(b).replace("</", "<\\/"), "js": JS}
    (folder / "receipts.html").write_text(page, encoding="utf-8")
    (folder / "sheet.html").write_text(sheet(b), encoding="utf-8")
    print("wrote receipts.html and sheet.html")


if __name__ == "__main__":
    main(Path(sys.argv[1]), sys.argv[2])
