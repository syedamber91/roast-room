#!/usr/bin/env python3
"""Build the courtroom's case book for one company: the facts the judge and the lawyer learn the company from, before the hearing.

The case book is FACTS ONLY (docs/courtroom-design.md section 3). It holds filed numbers, ownership, funding and a timeline of exchange
events. It never holds a management claim, a management quote or a defence: those surface only in the hearing. Everything here is read
by code from the company's seat brain and its data pack spec; chapters 1, 2 and 7 (plain words and the glossary) are drafted later by a
model from the annual report's business pages and are written here as "not yet drafted". Nothing is fetched and nothing is invented.

  python build_case_book.py --company BIOCON \
      --spec docs/company-record/biocon/datapack.json \
      --events docs/company-record/biocon/announcements-2022-2026-2026-10-30.json \
      --run-date 2026-10-30 --out sessions/2026-10-30-court-biocon

Writes <out>/case-book.md (for the judge and the lawyer) and <out>/case.json (issue states, the baseline sheet and the gaps, for the code).
"""
import argparse
import importlib.util
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOM_SCRIPTS = HERE.parents[1] / "roast-room" / "scripts"          # .claude/skills/roast-room/scripts
ISSUES_FILE = HERE.parent / "references" / "issues.json"
LAWYER_BRAIN = "india-market-analyst"                                 # the Analyst seat is the default lawyer (docs/courtroom-design.md section 2)

# exchange announcement categories that make a useful timeline (the others are routine filings)
EVENT_CATEGORIES = [
    "Acquisition", "Agreements", "Appointment", "Resignation", "Cessation", "Change in Director(s)", "Change in Auditors", "Credit Rating",
    "Allotment of Securities", "Issue of Securities", "Redemption", "Dividend", "Rumour Verification - Regulation 30(11)", "News Verification",
]

# marks of management's own words or claims. A prose line (not a table row) with any of them is dropped from the facts chapters and listed in
# case.json; after that, any facts chapter that still carries one stops the build. A source id on a filed number, like (S026), is fine.
MANAGEMENT_RE = re.compile(
    r"\bguid(?:ance|ed|es)\b"                                                                          # a guide
    r"|\bmanagement(?:'s|\u2019s)?\s+(?:\d|guid|net debt|said|says|stated|expects?|believes?|answers?|figures?|view|call|target|aim)"  # management's claim
    r"|\bwe (?:expect|believe)\b|\(S0\d\d, (?:management|analyst)", re.IGNORECASE)             # first person, or a speaker tag
# a job title such as "Senior Management Personnel" and a source line saying a figure is "not management's words" are not claims
DROPPED = []   # (chapter, line) pairs removed by strip_management_lines, written to case.json so nothing disappears silently


def load_pack_module():
    spec = importlib.util.spec_from_file_location("build_data_pack", ROOM_SCRIPTS / "build_data_pack.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def strip_management_lines(block: str, chapter: str) -> str:
    """Remove prose lines that carry a management claim; table rows are kept (a row that carries one fails the guard instead)."""
    kept = []
    for line in block.splitlines():
        if not line.strip().startswith("|") and MANAGEMENT_RE.search(line):
            DROPPED.append({"chapter": chapter, "line": line.strip()[:300]})
        else:
            kept.append(line)
    return "\n".join(kept)


def md_table(header: list, rows: list) -> str:
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(str(c).replace("|", "/") for c in r) + " |" for r in rows]
    return "\n".join(lines)


def pct(new, old):
    try:
        return f"{100 * (new / old - 1):+.1f}"
    except (TypeError, ZeroDivisionError):
        return "n/a"


# ---- issue states ---------------------------------------------------------------------------------------------------------------------

def issue_state(pack_lines: list, lines_by_id: dict) -> tuple:
    """(state, reasons). no record: a required line of the issue is missing. thin: nothing in the issue is complete (every line is partial,
    stale or unverified). examinable: at least one complete line and none missing. Partial lines are listed either way."""
    reasons, full = [], 0
    missing = False
    for line_id in pack_lines:
        line = lines_by_id.get(line_id)
        if line is None:
            reasons.append(f"{line_id}: not in the data pack spec")
            missing = True
        elif line["state"] == "missing":
            reasons.append(f"{line_id} missing: {line.get('gap', '')}")
            missing = missing or line["required"]
        elif line["state"] != "ok":
            reasons.append(f"{line_id} {line['state']}: {line.get('gap', '')}")
        elif line.get("partial"):
            reasons.append(f"{line_id} partial: {line['partial']}")
        else:
            full += 1
    if missing:
        return "no record", reasons
    return ("examinable" if full else "thin"), reasons


# ---- chapters -------------------------------------------------------------------------------------------------------------------------

def chapter_numbers(bdp, brain: Path) -> str:
    text = (brain / "numbers.md").read_text(encoding="utf-8")
    header, rows = bdp.parse_table(bdp.read_section(text, "## Filed quarters, consolidated"))
    col = {name: header.index(name) for name in ("Revenue from operations", "Operating profit", "Operating margin %")}
    by_date = {r[0]: r for r in rows}
    out_rows = []
    for r in rows:
        year_ago = by_date.get(f"{int(r[0][:4]) - 1}{r[0][4:]}")
        if year_ago:
            rev = pct(bdp.number(r[col["Revenue from operations"]]), bdp.number(year_ago[col["Revenue from operations"]]))
            op = pct(bdp.number(r[col["Operating profit"]]), bdp.number(year_ago[col["Operating profit"]]))
            m_new, m_old = bdp.number(r[col["Operating margin %"]]), bdp.number(year_ago[col["Operating margin %"]])
            margin = f"{m_new - m_old:+.1f}" if m_new is not None and m_old is not None else "n/a"
        else:
            rev = op = margin = "n/a"
        out_rows.append(r[:-1] + [rev, op, margin, r[-1]])
    quarter_header = header[:-1] + ["Revenue vs year-ago quarter %", "Operating profit vs year-ago quarter %", "Operating margin vs year-ago (points)", header[-1]]
    parts = ["## 3. The numbers over several years", "",
             "Rs million, consolidated, as filed. The three change columns are worked out here by code from the filed cells (a quarter against the same quarter a year earlier); "
             "they are blank (n/a) where the year-ago quarter is not in the table. The Source column says which filing each row was read from.", "",
             "### Filed quarters", "", md_table(quarter_header, out_rows), "",
             "### Full year, from the annual report", "", strip_management_lines(bdp.read_section(text, "## Annual report FY2025-26, consolidated, as filed (S026)"), "3"), "",
             "### Segments", "", strip_management_lines(bdp.read_section(text, "## Segments"), "3"), ""]
    return "\n".join(parts)


def chapter_ownership(bdp, brain: Path) -> str:
    share = (brain / "shareholding.md").read_text(encoding="utf-8")
    decl = (brain / "promoter-declarations.md").read_text(encoding="utf-8")
    header, rows = bdp.parse_table(bdp.read_section(share, "## Filed patterns"))
    parts = ["## 4. Who owns and runs it", "",
             "### Promoter and public shareholding, every filing", "", md_table(header, rows), "",
             strip_management_lines(bdp.read_section(share, "## Derived by code"), "4"), "",
             "### The promoter group's annual declaration about encumbrance", "", strip_management_lines(bdp.read_section(decl, "## Annual declarations under Regulation 31(4)"), "4"), "",
             "Board and auditor facts are not yet in the case book (to be added from the annual report in a later step).", ""]
    return "\n".join(parts)


def chapter_funding(bdp, brain: Path) -> str:
    text = (brain / "debt-covenants.md").read_text(encoding="utf-8")
    return "\n".join(["## 5. How it is funded", "",
                      strip_management_lines(bdp.read_section(text, "## Covenants and the maturity table (annual report FY2025-26)"), "5"), "",
                      strip_management_lines(bdp.read_section(text, "## What the report does not state"), "5"), ""])


def chapter_timeline(events_path: Path) -> tuple:
    """(markdown, newest announcement date) from the exchange announcement feed, filtered to EVENT_CATEGORIES."""
    feed = json.loads(events_path.read_text(encoding="utf-8"))
    when = lambda e: datetime.strptime(e["an_dt"], "%d-%b-%Y %H:%M:%S")  # noqa: E731
    newest = max(when(e) for e in feed).date().isoformat()
    rows = []
    for e in sorted(feed, key=when):
        if e["desc"] in EVENT_CATEGORIES:
            headline = " ".join((e.get("attchmntText") or "").split())
            rows.append([when(e).date().isoformat(), e["desc"], headline[:160]])
    return "\n".join(["## 6. Timeline of events from the exchange feed", "",
                      f"Filtered to {len(EVENT_CATEGORIES)} event categories ({len(rows)} of {len(feed)} announcements from {min(when(e) for e in feed).date()} to {newest}). "
                      "The text is the exchange's own one-line summary; the document behind each line is not read here.", "",
                      md_table(["Date", "Category", "Exchange summary"], rows), ""]), newest


def not_in_record(bdp, brain: Path, lines: list) -> list:
    items = []
    for line in lines:
        if line["state"] == "missing":
            items.append(f"{line['id']} {line['label']}: missing. {line.get('gap', '')}")
        elif line.get("partial"):
            items.append(f"{line['id']} {line['label']}: {line['partial']}")
    positions = (brain / "positions.md").read_text(encoding="utf-8")
    for bullet in bdp.read_section(positions, "## Subjects with no recorded position").splitlines():
        m = re.match(r"- \*\*(.+?):\*\*", bullet)
        if m:
            items.append(f"Subject with no recorded position in the convict's record: {m.group(1)}")
    return items


def chapter_record_status(lines: list, gate: str, issues: list, gaps: list, run_date: date, newest_announcement: str) -> str:
    as_of_rows = [[l["id"], l["label"], l.get("as_of") or "", l["state"]] for l in lines]
    issue_rows = [[i["id"], i["name"], i["state"], "; ".join(i["reasons"]) or "none", "; ".join(i["known_gaps"]) or "none"] for i in issues]
    return "\n".join(["## 8. As-of dates and what is not in the record", "",
                      f"Case book built {run_date.isoformat()}. Nothing after these dates exists for the hearing. Exchange announcements run to {newest_announcement}.", "",
                      f"**{gate}**", "",
                      md_table(["Pack line", "What it holds", "As of", "State"], as_of_rows), "",
                      "### Which issues the record can support", "",
                      "examinable: at least one complete data pack line and none missing. thin: every line is partial. no record: a required line is missing. "
                      "Partial lines and the hand-written known gaps are listed so the judge never writes a story over them.", "",
                      md_table(["Issue", "Name", "State", "Data pack notes", "Known gaps"], issue_rows), "",
                      "### Not in the record", ""] + [f"- {g}" for g in gaps] + [""])


PLACEHOLDERS = {
    1: ("The company in plain words", "Not yet drafted. To be drafted in plain words from the annual report's business pages, one page id on every sentence, then checked by code."),
    2: ("How it makes money", "Not yet drafted. To be drafted in plain words from the annual report's business pages (segments, products, customers), page ids on every sentence."),
    7: ("Glossary", "Not yet drafted. A shared plain-words glossary, written once and reused for every company (references/glossary.md, to be created)."),
}


def check_facts_only(text: str) -> list:
    """Lines in the facts chapters that still carry a management claim. Empty when clean."""
    return [line.strip()[:200] for line in text.splitlines() if MANAGEMENT_RE.search(line)]


def build(company: str, spec_path: Path, events_path: Path, run: date) -> tuple:
    bdp = load_pack_module()
    DROPPED.clear()
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    brain = HERE.parents[1] / "roast-room" / "brains" / spec["brain"]
    lines = [bdp.build_line(l, brain, run) for l in spec["lines"]]
    by_id = {l["id"]: l for l in lines}
    pack = bdp.build_pack(spec, brain, run)
    gate = next(l.strip("* ") for l in pack.splitlines() if l.startswith("**BRIEF"))
    config = json.loads(ISSUES_FILE.read_text(encoding="utf-8"))
    issues = []
    for issue in config["issues"]:
        state, reasons = issue_state(issue["pack_lines"], by_id)
        issues.append({**issue, "state": state, "reasons": reasons})
    timeline, newest = chapter_timeline(events_path)
    gaps = not_in_record(bdp, brain, lines)
    chapters = [f"# Case book: {company}", "",
                f"Facts only, from filings and the exchange feed, built {run.isoformat()}. It holds no management claim and no management quote; those come out only in the hearing. "
                "Money is in Rs million as filed unless a line says otherwise. A derived figure is worked out by code and says so. This is a simulation aid, not advice.", ""]
    for n in (1, 2):
        chapters += [f"## {n}. {PLACEHOLDERS[n][0]}", "", PLACEHOLDERS[n][1], ""]
    chapter_numbers_text, chapter_ownership_text, chapter_funding_text = chapter_numbers(bdp, brain), chapter_ownership(bdp, brain), chapter_funding(bdp, brain)
    chapters += [chapter_numbers_text, chapter_ownership_text, chapter_funding_text, timeline,
                 f"## 7. {PLACEHOLDERS[7][0]}", "", PLACEHOLDERS[7][1], "",
                 chapter_record_status(lines, gate, issues, gaps, run, newest)]
    text = "\n".join(chapters)
    facts_text = "\n".join([chapter_numbers_text, chapter_ownership_text, chapter_funding_text, timeline])
    case = {"company": company, "run_date": run.isoformat(), "gate": gate, "convict_brain": spec["brain"], "lawyer_brain": LAWYER_BRAIN, "issues": issues, "baseline": config["baseline"], "not_in_record": gaps,
            "chapters": {str(n): {"title": PLACEHOLDERS[n][0], "drafted": False} for n in PLACEHOLDERS} | {str(n): {"drafted": True} for n in (3, 4, 5, 6, 8)},
            "facts_only_problems": check_facts_only(facts_text), "dropped_management_lines": list(DROPPED), "announcements_to": newest}
    return text, case


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--company", required=True)
    ap.add_argument("--spec", required=True, type=Path)
    ap.add_argument("--events", required=True, type=Path)
    ap.add_argument("--run-date", required=True)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    text, case = build(args.company, args.spec, args.events, date.fromisoformat(args.run_date))
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "case-book.md").write_text(text, encoding="utf-8")
    (args.out / "case.json").write_text(json.dumps(case, indent=1), encoding="utf-8")
    print(f"{case['gate']}")
    for i in case["issues"]:
        print(f"  {i['id']} {i['state']:<11} {i['name']}")
    if case["facts_only_problems"]:
        print("FACTS-ONLY PROBLEM: the case book contains", case["facts_only_problems"], file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
