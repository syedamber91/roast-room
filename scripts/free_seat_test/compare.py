"""Compare the free-model extraction against the quotes the existing (Claude-built) BIOCON brain holds. Read-only."""
import json, re, sys, collections
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
run = sys.argv[1] if len(sys.argv) > 1 else "run-lightning.jsonl"

def norm(s):
    s = s.lower().replace("’", "'").replace("‘", "'")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9' ]+", " ", s)).strip()

corp = {}
for f in sorted((ROOT / "corpus").glob("S*.txt")):
    corp[f.stem] = norm(f.read_text(encoding="utf8"))

def spans(q, sid):
    hay = corp.get(sid, ""); out = []
    for p in re.split(r"\.\.\.|…", q):
        p = norm(p)
        if len(p.split()) < 3: continue
        i = hay.find(p)
        if i >= 0: out.append((i, i + len(p)))
    return out

base = json.loads((ROOT / "baseline-quotes.json").read_text())
seen, B = set(), []
for r in base:
    k = (r["sid"], norm(r["quote"]))
    if k in seen: continue
    seen.add(k); B.append(r)
for r in B: r["spans"] = spans(r["quote"], r["sid"])
found_in_my_corpus = [r for r in B if r["spans"]]
print(f"existing brain: {len(B)} distinct quotes; verbatim in my freshly fetched corpus: {len(found_in_my_corpus)} ({len(found_in_my_corpus)/len(B):.0%})")

F = [json.loads(l) for l in (ROOT / run).read_text().splitlines()]
seenf, Fu = set(), []
for r in F:
    k = (r["id"], norm(r["quote"]))
    if k in seenf: continue
    seenf.add(k); Fu.append(r)
for r in Fu: r["spans"] = spans(r["quote"], r["id"])
print(f"free run {run}: {len(F)} verbatim items, {len(Fu)} distinct quotes")

def overlap(a, b):
    return sum(max(0, min(x1, y1) - max(x0, y0)) for x0, x1 in a for y0, y1 in b)

def covered(r, pool):
    L = sum(e - s for s, e in r["spans"])
    if not L: return None
    best = None
    for p in pool:
        if p["id"] != r["sid"] if "sid" in r else False: continue
    for p in pool:
        if p["id"] != r["sid"]: continue
        if overlap(r["spans"], p["spans"]) >= 0.5 * L: return p
    return False

by_sid = collections.defaultdict(list)
for p in Fu: by_sid[p["id"]].append(p)
tot = hit = spk_ok = spk_n = 0
per_file = collections.defaultdict(lambda: [0, 0]); per_sid = collections.defaultdict(lambda: [0, 0])
missed = []
for r in found_in_my_corpus:
    c = covered(r, by_sid[r["sid"]])
    tot += 1; per_file[r["file"]][1] += 1; per_sid[r["sid"]][1] += 1
    if c:
        hit += 1; per_file[r["file"]][0] += 1; per_sid[r["sid"]][0] += 1
        if r["speaker"]:
            spk_n += 1
            a = set(re.sub(r"[^a-z ]", " ", r["speaker"].lower()).split()); b = set(re.sub(r"[^a-z ]", " ", c["speaker"].lower()).split())
            spk_ok += bool(a & b)
    else: missed.append(r)
print(f"\nRECALL: of the existing brain's {tot} checkable quotes, the free run covers {hit} ({hit/tot:.0%}) (>=50% of the quote's words inside a free-run quote)")
print("by existing file:", {k: f"{v[0]}/{v[1]}" for k, v in sorted(per_file.items())})
print(f"speaker agreement on covered quotes where the existing brain names one: {spk_ok}/{spk_n}")
dec = {s: v for s, v in per_sid.items() if int(s[1:]) > 14}; call = {s: v for s, v in per_sid.items() if int(s[1:]) <= 14}
print("per source:", {k: f"{v[0]}/{v[1]}" for k, v in sorted(per_sid.items())})
print("calls: %d/%d  decks: %d/%d" % (sum(v[0] for v in call.values()), sum(v[1] for v in call.values()), sum(v[0] for v in dec.values()), sum(v[1] for v in dec.values())))

def near(r, pool, gap=300):
    return any(r["sid"] == p["id"] and any(not (e + gap < s2 or s + gap > e2 and False) and (s - gap) < e2 and (e + gap) > s2 for s, e in r["spans"] for s2, e2 in p["spans"]) for p in pool)
nr = sum(1 for r in found_in_my_corpus if near(r, by_sid[r["sid"]]))
print(f"LOOSE recall (a free-run quote sits within ~300 characters of the existing quote, same source): {nr}/{tot} ({nr/tot:.0%})")
rec = [r for r in found_in_my_corpus if r["file"] == "record.md"]
print(f"record.md loose: {sum(1 for r in rec if near(r, by_sid[r['sid']]))}/{len(rec)}")
rh = [r for r in rec if covered(r, by_sid[r["sid"]])]
print(f"\nrecord.md scored statements ('Said:' quotes): free run covers {len(rh)} of {len(rec)}")
json.dump([{"file": r["file"], "sid": r["sid"], "quote": r["quote"]} for r in missed], open(ROOT / "missed.json", "w"), indent=0)

# free-only items: quotes that overlap NO existing quote
bsid = collections.defaultdict(list)
for r in found_in_my_corpus: bsid[r["sid"]].append(r)
fonly = [p for p in Fu if p["spans"] and not any(overlap(p["spans"], b["spans"]) >= 0.5 * sum(e - s for s, e in p["spans"]) for b in bsid[p["id"]])]
print(f"\nfree-only distinct quotes (no overlap with any existing-brain quote): {len(fonly)} of {len(Fu)}")
print("kinds of all free items:", dict(collections.Counter(r["kind"] for r in Fu)))
json.dump(fonly, open(ROOT / "free-only.json", "w"), ensure_ascii=False, indent=0)
