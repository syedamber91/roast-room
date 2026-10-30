"""Step 3: a free NVIDIA model reads each batch of management turns and proposes items.

CODE decides who spoke (the turn), the model only picks verbatim words. Every quote is checked against the
turn text; anything not found is thrown away and counted. Speaker, source id and held date come from the turn.

usage: python3 extract.py <model> <out.jsonl> [--only S001,S002] [--max-words 3000]
"""
import json, os, re, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = "https://integrate.api.nvidia.com/v1/chat/completions"
KEY = os.environ["NVIDIA_API_KEY"]
EXTRA = {m: {"chat_template_kwargs": {"enable_thinking": False}} for m in ("nvidia/nemotron-3.5-lightning-30b-a3b", "nvidia/nemotron-3.5-super-vl-120b-a12b")}

RULES = """Rules for every quote: copy it character for character from the text, under 40 words, no edits, no joining
of separate sentences, no summary inside the quotation. If you cannot copy exact words, leave the item out.
Pick the turn number ("turn") the quote comes from. Return ONLY valid JSON, no commentary."""

PROMPT_A = """You read part of a company's investor material. Only management's own words are shown. Each block starts
with [T<n>] and a speaker name (a slide deck is one block, [T1]).
Extract:
1. "commitments": forward-looking promises, targets, launch dates, guidance or plans, with the time window management gave.
2. "figures": numbers management states about the company itself (debt, margins, revenue, capex, R&D, launches counted) with the period or basis.
""" + RULES + """
Shape: {"commitments":[{"turn":1,"topic":"2-5 words","window":"the time window in management's words, or empty","quote":"..."}],"figures":[{"turn":1,"topic":"2-5 words","quote":"..."}]}

TEXT:
"""

PROMPT_B = """You read part of a company's investor material. Only management's own words are shown. Each block starts
with [T<n>] and a speaker name (a slide deck is one block, [T1]).
Extract how management thinks and talks:
- "position": a stance on a topic (debt, pricing, capex, R&D, biosimilars, generics, China, tariffs, partners, hiring, margins, competition).
- "rule": a decision rule or priority they state, in a sentence that says what comes first or what they will not do.
- "framework": a named method, metric or way of measuring that they define or reuse.
- "story": a specific example, case or analogy they use.
- "voice": a short phrase or hedge that they use again and again.
""" + RULES + """
Shape: {"items":[{"kind":"position|rule|framework|story|voice","turn":1,"topic":"2-5 words","quote":"..."}]}

TEXT:
"""


def norm(s):
    s = s.lower().replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9' ]+", " ", s)).strip()


def batches(doc, max_words):
    out, cur, n = [], [], 0
    for i, t in enumerate(doc["turns"], 1):
        w = len(t["text"].split())
        if cur and n + w > max_words:
            out.append(cur); cur, n = [], 0
        cur.append((len(cur) + 1, t)); n += w
    if cur: out.append(cur)
    return out


def call(model, prompt, retries=4):
    body = {"model": model, "messages": [{"role": "user", "content": prompt}], "max_tokens": 8000, "temperature": 0, **EXTRA.get(model, {})}
    for a in range(retries):
        try:
            req = urllib.request.Request(URL, json.dumps(body).encode(), {"Authorization": "Bearer " + KEY, "Content-Type": "application/json"})
            d = json.load(urllib.request.urlopen(req, timeout=300))
            return d["choices"][0]["message"].get("content") or "", d.get("usage", {}), a
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504): time.sleep(5 * 2 ** a); continue
            raise
        except Exception:
            time.sleep(5 * 2 ** a)
    return "", {}, retries


def parse(txt):
    m = re.search(r"\{.*\}", txt, re.S)
    try: return json.loads(m.group(0)) if m else {}
    except Exception: return {}


def run_batch(job):
    model, doc, bi, batch = job
    text = "\n\n".join(f"[T{n}] {t['label']}: {t['text']}" for n, t in batch)
    recs, calls = [], []
    for pname, prompt in (("A", PROMPT_A), ("B", PROMPT_B)):
        txt, usage, retries = call(model, prompt + text)
        data = parse(txt)
        rows = []
        if pname == "A":
            rows += [dict(r, kind="commitment") for r in data.get("commitments", []) if isinstance(r, dict)]
            rows += [dict(r, kind="figure") for r in data.get("figures", []) if isinstance(r, dict)]
        else:
            rows += [r for r in data.get("items", []) if isinstance(r, dict)]
        kept = dropped = 0
        for r in rows:
            q = str(r.get("quote", "")).strip()
            parts = [norm(p) for p in re.split(r"\.\.\.|…", q) if len(norm(p).split()) >= 3]
            if not parts or len(q.split()) > 45 or len(norm(q).split()) < 6: dropped += 1; continue
            hit = None
            try: want = int(r.get("turn"))
            except Exception: want = None
            order = [x for x in batch if x[0] == want] + [x for x in batch if x[0] != want]
            for n, t in order:
                hay = norm(t["text"])
                if all(p in hay for p in parts): hit = t; break
            if not hit: dropped += 1; continue
            kept += 1
            recs.append({"id": doc["id"], "date": doc["date"], "speaker": hit["label"], "kind": r.get("kind", ""),
                         "topic": str(r.get("topic", ""))[:80], "window": str(r.get("window", ""))[:80], "quote": q})
        calls.append({"id": doc["id"], "batch": bi, "prompt": pname, "proposed": len(rows), "kept": kept, "dropped": dropped,
                      "retries": retries, "tokens": usage.get("total_tokens"), "completion": usage.get("completion_tokens")})
    return recs, calls


def main():
    model, out = sys.argv[1], Path(sys.argv[2])
    only = set(sys.argv[sys.argv.index("--only") + 1].split(",")) if "--only" in sys.argv else None
    mw = int(sys.argv[sys.argv.index("--max-words") + 1]) if "--max-words" in sys.argv else 3000
    jobs = []
    for f in sorted((ROOT / "corpus").glob("S*.json")):
        doc = json.loads(f.read_text())
        if only and doc["id"] not in only: continue
        for bi, b in enumerate(batches(doc, mw), 1): jobs.append((model, doc, bi, b))
    print(len(jobs), "batches ->", 2 * len(jobs), "calls", flush=True)
    t0 = time.time(); allrecs, allcalls = [], []
    with ThreadPoolExecutor(3) as ex:
        for k, (recs, calls) in enumerate(ex.map(run_batch, jobs), 1):
            allrecs += recs; allcalls += calls
            if k % 5 == 0: print(f"{k}/{len(jobs)} batches, {len(allrecs)} verbatim items, {time.time()-t0:.0f}s", flush=True)
    out.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in allrecs))
    out.with_suffix(".calls.jsonl").write_text("\n".join(json.dumps(c) for c in allcalls))
    P = sum(c["proposed"] for c in allcalls); K = sum(c["kept"] for c in allcalls)
    print(f"DONE {len(allcalls)} calls, proposed {P}, verbatim {K} ({K/max(P,1):.0%}), tokens {sum(c['tokens'] or 0 for c in allcalls)}, {time.time()-t0:.0f}s")


main()
