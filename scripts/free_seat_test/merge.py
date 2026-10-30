"""Step 4: merge runs, group topics, and write a test brain. All prose is built by code from verified quotes.

The only model call here is a closed-vocabulary label sorter: it assigns each short topic label to one of a fixed list
of categories. It never writes a sentence that is shown. Output goes to build/biocon-free/brain/, never to the live brains.
usage: python3 merge.py out_dir run1.jsonl [run2.jsonl ...]
"""
import json, os, re, sys, collections, importlib.util
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("ex", ROOT / "pipeline/extract.py")
src = (ROOT / "pipeline/extract.py").read_text().replace("\nmain()\n", "\n")
ex = type(sys)("ex"); ex.__dict__["__file__"] = str(ROOT / "pipeline/extract.py"); exec(compile(src, "extract.py", "exec"), ex.__dict__)
norm, call = ex.norm, ex.call
MODEL = "nvidia/nemotron-3.5-lightning-30b-a3b"
CATS = ["Debt and balance sheet", "Capex and capacity", "R&D and pipeline", "Biosimilar launches and approvals", "Generics and peptides (GLP-1)",
        "Insulin", "Pricing and competition", "Margins and EBITDA", "US market, tariffs and policy", "Emerging markets and Europe",
        "Syngene and research services", "Viatris deal and integration", "Leadership, structure and governance", "Cash, working capital and capital allocation",
        "Guidance and outlook", "Other"]

out = ROOT / sys.argv[1]; out.mkdir(exist_ok=True)
items, seen = [], set()
for rf in sys.argv[2:]:
    for l in (ROOT / rf).read_text().splitlines():
        r = json.loads(l); k = (r["id"], norm(r["quote"]))
        if k in seen: continue
        seen.add(k); items.append(r)
meta = {l.split("\t")[0]: l.split("\t") for l in (ROOT / "urls.tsv").read_text().splitlines()}

labels = sorted({norm(r["topic"]) for r in items if r["topic"]})
cat_of, calls = {}, 0
for i in range(0, len(labels), 120):
    chunk = labels[i:i + 120]
    prompt = ("Sort each topic label into exactly one category from this list: " + json.dumps(CATS) +
              '\nReturn ONLY JSON like {"label text": "category"} covering every label.\nLABELS:\n' + json.dumps(chunk))
    txt, usage, _ = call(MODEL, prompt); calls += 1
    m = re.search(r"\{.*\}", txt, re.S)
    try: d = json.loads(m.group(0))
    except Exception: d = {}
    for lab in chunk:
        c = d.get(lab)
        cat_of[lab] = c if c in CATS else "Other"
for r in items: r["cat"] = cat_of.get(norm(r["topic"]), "Other")

def line(r):
    w = f" Window: {r['window']}." if r.get("window") else ""
    return f'- ({r["date"]}, {r["speaker"]}, {r["id"]}) "{r["quote"]}"{w}'

def write(name, head, body): (out / name).write_text(head + "\n\n" + body + "\n", encoding="utf8")
kinds = collections.defaultdict(list)
for r in items: kinds[r["kind"]].append(r)
for k in kinds: kinds[k].sort(key=lambda r: (r["date"], r["id"]))
pos = [r for k in ("position", "rule") for r in kinds[k]]
byc = collections.defaultdict(list)
for r in pos: byc[r["cat"]].append(r)
write("positions.md", "# positions: BIOCON management (free-model build)\n\nVerbatim management statements by topic, oldest first. Built by code from quotes a model proposed and a script checked.",
      "\n\n".join(f"## {c} ({len(v)})\n" + "\n".join(line(r) for r in sorted(v, key=lambda r: (r['date'], r['id']))) for c, v in sorted(byc.items(), key=lambda x: -len(x[1]))))
byc2 = collections.defaultdict(list)
for r in kinds["commitment"]: byc2[r["date"]].append(r)
write("commitments.md", "# commitments: forward-looking statements, by held date\n\nNo outcome is scored here: that needs filed numbers, which this build did not fetch.",
      "\n\n".join(f"## Held {d} ({len(v)})\n" + "\n".join(line(r) for r in v) for d, v in sorted(byc2.items())))
write("figures.md", "# figures: numbers management stated (as said, not as filed)", "\n".join(line(r) for r in kinds["figure"]))
write("frameworks.md", "# frameworks: named measures and methods", "\n".join(line(r) for r in kinds["framework"]))
write("stories.md", "# stories: examples and analogies", "\n".join(line(r) for r in kinds["story"]))
write("voice.md", "# voice: repeated phrases and hedges", "\n".join(line(r) for r in kinds["voice"]))
write("sources.md", "# sources", "\n".join(f"- {s[0]} | {s[1]} | {s[2]} | {s[3]}" for s in meta.values()))
latest = max(r["date"] for r in items)
rules = sorted(kinds["rule"], key=lambda r: r["date"], reverse=True)[:8]
hot = (f"# Hot sheet: BIOCON management, on the record (free-model build, test only)\n\nCalls run to {latest}. Built from {len(set(r['id'] for r in items))} sources; "
       f"{len(items)} verified items: " + ", ".join(f"{len(v)} {k}" for k, v in sorted(kinds.items())) + ".\n\nFiles: positions.md (by topic), commitments.md (by held date), figures.md, frameworks.md, stories.md, voice.md, sources.md.\n"
       "No filed quarters, no price and no scorecard are in this build. Say so whenever a question needs them.\n\n## Eight most recent stated rules (code-selected, newest first)\n\n" + "\n".join(f"{i+1}. {line(r)[2:]}" for i, r in enumerate(rules)) +
       "\n\n## Topic counts\n\n" + "\n".join(f"- {c}: {len(v)}" for c, v in sorted(byc.items(), key=lambda x: -len(x[1]))))
(out / "_hot.md").write_text(hot + "\n", encoding="utf8")
print("items", len(items), "label-sorter calls", calls, "files:", sorted(p.name for p in out.iterdir()))
