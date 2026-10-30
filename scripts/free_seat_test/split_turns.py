"""Step 2 of the free-model seat build: cut each call into speaker turns IN CODE, keep management only.

The model never decides who spoke. A turn's speaker is the label printed in the transcript, and a speaker
counts as management only if the call's own "Speakers and Participants" block lists them with a title.
Output: corpus/<id>.txt (management turns only, as "Name: text") and corpus/<id>.json (one record per turn).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADER_RE = re.compile(r"(?m)^\s*(?:Dr\.|Mr\.|Ms\.|Mrs\.)\s+(.+?)\s+[–-]\s+([^\n]+)")
LABEL_RE = re.compile(r"(?m)^[ \t]*([A-Z][A-Za-z\.\-' ]{2,40}?):[ \t]*(?=\S|\n)")
# investor-relations hosts read the agenda; they are not decision makers (the existing brain leaves them out)
NOT_MANAGEMENT_TITLES = re.compile(r"investor relations|moderator", re.I)
NOISE_LINE = re.compile(r"^\s*(Biocon Limited .*(Earnings|Conference Call)|Page \d+ of \d+|\d+)\s*$", re.I)


def name_tokens(name: str) -> set:
    return {p.lower() for p in re.sub(r"[^A-Za-z ]", " ", name).split() if len(p) >= 4}


def management_roster(text: str) -> dict:
    head = text[:12000]
    roster = {}
    for m in HEADER_RE.finditer(head):
        name, title = m.group(1).strip(), m.group(2).strip()
        if NOT_MANAGEMENT_TITLES.search(title):
            continue
        roster[name] = name_tokens(name)
    return roster


def split_call(text: str):
    roster = management_roster(text)
    body_start = max(text.find("Conference Call Transcript"), 0)
    marks = [(m.start(), m.end(), m.group(1).strip()) for m in LABEL_RE.finditer(text, body_start)]
    turns = []
    for i, (s, e, label) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        raw = text[e:end]
        lines = [l for l in raw.splitlines() if not NOISE_LINE.match(l)]
        said = re.sub(r"\s+", " ", " ".join(lines)).strip()
        last = re.sub(r"[^A-Za-z ]", " ", label).split()
        last = last[-1].lower() if last else ""
        turns.append({"label": label, "management": any(last in toks for toks in roster.values()), "text": said})
    return roster, turns


def main():
    meta = {l.split("\t")[0]: l.split("\t") for l in (ROOT / "urls.tsv").read_text().splitlines()}
    out = ROOT / "corpus"; out.mkdir(exist_ok=True)
    report = []
    for i in range(1, 26):
        sid = f"S{i:03d}"
        text = (ROOT / "txt" / f"{sid}.txt").read_text(encoding="utf8")
        title, date = meta[sid][1], meta[sid][3]
        if i <= 14:
            roster, turns = split_call(text)
            mgmt = [t for t in turns if t["management"]]
            body = "\n\n".join(f'{t["label"]}: {t["text"]}' for t in mgmt)
        else:  # decks: the company's own slides, one block of text
            roster, turns, mgmt = {}, [], [{"label": "company deck", "management": True, "text": re.sub(r"\s+", " ", text).strip()}]
            body = mgmt[0]["text"]
        (out / f"{sid}.txt").write_text(f"{title}\nSource: {sid} | {meta[sid][2]} | {date}\n\n{body}\n", encoding="utf8")
        (out / f"{sid}.json").write_text(json.dumps({"id": sid, "title": title, "date": date, "turns": mgmt}, ensure_ascii=False))
        words = len(body.split())
        report.append((sid, date, len(roster), len(turns), len(mgmt), words, int(meta[sid][4])))
    print("id date roster turns mgmt_turns my_words existing_words ratio")
    for r in report:
        print(*r, f"{r[5]/r[6]:.2f}")
    print("total my words", sum(r[5] for r in report), "existing", sum(r[6] for r in report[:25]))


main()
