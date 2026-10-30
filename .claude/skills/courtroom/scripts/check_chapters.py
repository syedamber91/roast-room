#!/usr/bin/env python3
"""Check the drafted case book chapters (1 company in plain words, 2 how it makes money, 7 company terms) against the annual report pages.

    python check_chapters.py chapters-1-2-7.md --ar-config ar-pages.json --brain biocon-management

A drafted line must be a fact about what the company is or does, in plain short words, with a page id.
The checks, all by code:
- every line ends with a page id like (AR p13) or (AR p13, p14), and the page is one of the business pages;
- every number in a line is printed on a page it cites;
- a line is one sentence of at most 25 words;
- no line carries a forward-looking or guidance word, or a management claim;
- no run of six words matches the convict's call and deck quotes (positions.md, record.md, qa-states.md);
- a line that praises (leading, best, world-class, strong) is flagged as a warning.
Exit code 1 if any check fails.
"""

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BRAINS = HERE.parents[1] / "roast-room" / "brains"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gov = _load("governance_facts")
bcb = _load("build_case_book")

PAGE_ID = re.compile(r"\(AR (p\d+(?:,\s*p\d+)*)\)\s*$")
FUTURE_RE = re.compile(r"\b(?:will|would|expects?|expected|aims?|plans? to|intends?|targets?|outlook|guidance|forecast|poised|vision|aspires?|going forward)\b", re.I)
PRAISE_RE = re.compile(r"\b(?:leading|best|world-class|strong|robust|premier|unmatched|exceptional|landmark)\b", re.I)
MAX_WORDS = 25
SHINGLE = 6


def norm_words(text: str) -> list:
    return re.sub(r"[^a-z0-9' ]+", " ", text.lower().replace("’", "'")).split()


def numbers_in(text: str) -> list:
    """Number tokens such as 31,681 or 13 or 1.96, with commas removed. Page numbers in brackets are taken out first."""
    text = PAGE_ID.sub("", text)
    return [n.replace(",", "") for n in re.findall(r"\d[\d,]*(?:\.\d+)?", text)]


def parse(text: str) -> dict:
    """{chapter number: [lines]} for the '## N. title' sections; a line is a '- ' bullet."""
    out, current = {}, None
    for line in text.splitlines():
        m = re.match(r"^##\s+(\d+)\.", line)
        if m:
            current = int(m.group(1))
            out[current] = []
        elif current is not None and line.startswith("- "):
            out[current].append(line[2:].strip())
    return out


def shingles(words: list) -> set:
    return {" ".join(words[i:i + SHINGLE]) for i in range(len(words) - SHINGLE + 1)}


def call_text_shingles(brain: Path) -> set:
    found = set()
    for name in ("positions.md", "record.md", "qa-states.md"):
        f = brain / name
        if f.exists():
            found |= shingles(norm_words(f.read_text(encoding="utf-8", errors="replace")))
    return found


def check(text: str, ar_dir: Path, business_pages: list, brain: Path) -> list:
    """Return [(severity, chapter, line start, message)]."""
    problems, chapters, banned = [], parse(text), call_text_shingles(brain)
    if not chapters:
        return [("FAIL", 0, "", "no '## N. title' chapter heading found")]
    for n, lines in chapters.items():
        if n not in (1, 2, 7):
            problems.append(("FAIL", n, "", "only chapters 1, 2 and 7 may be drafted"))
        if not lines:
            problems.append(("FAIL", n, "", "chapter has no lines"))
        for line in lines:
            head = line[:60]
            m = PAGE_ID.search(line)
            if not m:
                problems.append(("FAIL", n, head, "no page id at the end, write (AR p13)"))
                continue
            pages = [int(p.strip(" p")) for p in m.group(1).split(",")]
            body = PAGE_ID.sub("", line).strip()
            for p in pages:
                if p not in business_pages:
                    problems.append(("FAIL", n, head, "page %d is not one of the business pages %s" % (p, business_pages)))
            cited = {x.replace(",", "") for p in pages if p in business_pages for x in re.findall(r"\d[\d,]*(?:\.\d+)?", gov.page_text(ar_dir, p))}
            for num in numbers_in(body):
                if num not in cited:
                    problems.append(("FAIL", n, head, "number %s is not on the cited page(s)" % num))
            if len(body.split()) > MAX_WORDS:
                problems.append(("FAIL", n, head, "%d words, limit %d" % (len(body.split()), MAX_WORDS)))
            if len(re.findall(r"[.!?](?:\s|$)", body)) > 1:
                problems.append(("FAIL", n, head, "more than one sentence on a line"))
            if FUTURE_RE.search(body) or bcb.MANAGEMENT_RE.search(body):
                problems.append(("FAIL", n, head, "forward-looking or management-claim wording"))
            if shingles(norm_words(body)) & banned:
                problems.append(("FAIL", n, head, "six words in a row match the convict's call or deck record"))
            if PRAISE_RE.search(body):
                problems.append(("warn", n, head, "praise word: say what the company does, not how good it is"))
    for needed in (1, 2, 7):
        if needed not in chapters:
            problems.append(("FAIL", needed, "", "chapter missing"))
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("chapters", type=Path)
    ap.add_argument("--ar-config", required=True, type=Path)
    ap.add_argument("--brain", required=True)
    a = ap.parse_args()
    cfg = json.loads(a.ar_config.read_text(encoding="utf-8"))
    problems = check(a.chapters.read_text(encoding="utf-8"), gov.DEFAULT_LADDER / cfg["annual_report_dir"], cfg["business_pages"], BRAINS / a.brain)
    for sev, n, head, msg in problems:
        print("%-4s ch%d  %s: %s" % (sev, n, head, msg))
    fails = sum(1 for p in problems if p[0] == "FAIL")
    print("%d problem(s) to fix, %d warning(s)" % (fails, len(problems) - fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
