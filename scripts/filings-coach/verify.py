"""Check every extracted line against its source, mechanically. No model is involved.

SOIC lines: every timestamp and REF code in `cite` must appear in the note the line came from.
            (SOIC text is licensed, so these lines carry no quote; the cite is what we can check.)
Book lines: the `quote` (at most 25 words) must appear, whitespace-normalised, on the cited page file.

Writes merge/verified.json: {line_id: true/false} plus a printed summary.
A line that fails is never used as support for a framework step.

    python3 verify.py
"""
import json
import re
from collections import Counter

from paths import BOOKS_MD, EXTRACT, MERGE, SOIC

TIMESTAMP = re.compile(r"\d{2}:\d{2}:\d{2}")
REF_CODE = re.compile(r"\b[A-Z][A-Z0-9]{2,}\b")


def squash(text):
    """Collapse every run of whitespace to one space, so line breaks in a PDF don't break a match."""
    return re.sub(r"\s+", " ", text).strip()


def read_lines(folder):
    for f in sorted(folder.glob("*.jsonl")):
        for raw in f.read_text().splitlines():
            if raw.strip():
                yield json.loads(raw)


def soic_note_text(slug):
    for folder in ("concepts", "topics"):
        path = SOIC / folder / f"{slug}.md"
        if path.exists():
            return path.read_text()
    return None


def check_soic(row):
    cite = str(row.get("cite") or "")
    if cite in ("", "no-ref", "None"):
        return "no-ref"            # allowed, but can never be the only support for a step
    text = soic_note_text(row.get("source", ""))
    if text is None:
        return "no-source"
    stamps = TIMESTAMP.findall(cite)
    if not stamps:
        return "no-timestamp"
    codes = REF_CODE.findall(cite)
    ok = all(s in text for s in stamps) and all(c in text for c in codes)
    return "ok" if ok else "FAIL"


_page_cache = {}


def page_text(source, number):
    key = (source, number)
    if key not in _page_cache:
        path = BOOKS_MD / source / f"p{number:03d}.txt"
        _page_cache[key] = squash(path.read_text(errors="replace")) if path.exists() else None
    return _page_cache[key]


def check_book(row):
    quote = squash(row.get("quote") or "")
    match = re.match(r"p\.(\d+)", str(row.get("cite") or ""))
    if not quote:
        return "no-quote"
    if len(quote.split()) > 25:
        return "quote-too-long"
    if not match:
        return "bad-cite"
    page = page_text(row.get("source", ""), int(match.group(1)))
    if page is None:
        return "no-page"
    return "ok" if quote in page else "FAIL"


def main():
    results, tally = {}, Counter()
    for row in read_lines(EXTRACT):
        outcome = check_soic(row)
        results[row["id"]] = outcome in ("ok", "no-ref", "no-timestamp")
        tally["soic:" + outcome] += 1
    for row in read_lines(EXTRACT / "books"):
        outcome = check_book(row)
        results[row["id"]] = outcome == "ok"
        tally["book:" + outcome] += 1
    MERGE.mkdir(parents=True, exist_ok=True)
    (MERGE / "verified.json").write_text(json.dumps(results))
    for key, count in sorted(tally.items()):
        print(f"{key:24s} {count}")
    failed = [i for i, ok in results.items() if not ok]
    print(f"lines {len(results)}  usable {len(results) - len(failed)}  failed {len(failed)}")
    for line_id in failed[:15]:
        print("  failed:", line_id)


if __name__ == "__main__":
    main()
