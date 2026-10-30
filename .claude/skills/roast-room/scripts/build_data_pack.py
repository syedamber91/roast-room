#!/usr/bin/env python3
"""Build the Chair's data pack for a stock rating run, and the brief-completeness gate.

The pack is read from a company's seat brain (markdown tables and sections) and a small JSON spec that names each line, where it
comes from, how old it may be and whether a rating can start without it. Derived figures are computed here, by code, from the
table cells, and a stated figure that disagrees with its own inputs is flagged. Nothing is fetched and nothing is invented: a line
with no source is written as missing.

  python build_data_pack.py --spec docs/company-record/biocon/datapack.json --run-date 2026-10-30 [--session sessions/<folder>]

With --session the pack replaces the block between the markers in <session>/brief.md (created if absent); otherwise it is printed.
"""
import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

START, END = "<!-- data-pack START -->", "<!-- data-pack END -->"
ROOT = Path(__file__).resolve().parents[1]


def read_section(text: str, heading: str) -> str:
    """The text under a '## ' heading up to the next heading of the same or higher level; empty if the heading is absent."""
    level = len(heading) - len(heading.lstrip("#"))
    lines, out, on = text.splitlines(), [], False
    for line in lines:
        if line.strip() == heading.strip():
            on = True
            continue
        if on and re.match(r"^#{1,%d} " % level, line):
            break
        if on:
            out.append(line)
    return "\n".join(out).strip()


def parse_table(block: str):
    """(header cells, rows of cells) of the first markdown table in the block."""
    rows = [[c.strip() for c in line.strip().strip("|").split("|")] for line in block.splitlines() if line.strip().startswith("|")]
    rows = [r for r in rows if not all(re.fullmatch(r"-+:?|:?-+:?", c or "-") for c in r)]
    return (rows[0], rows[1:]) if rows else ([], [])


def number(cell: str):
    cleaned = cell.replace(",", "").replace("%", "").strip()
    try:
        return float(cleaned)
    except ValueError:
        return None


def derive(header: list, rows: list, rules: list) -> list:
    """Derived figures from table cells. Each result says how it was computed; a stated figure that disagrees is flagged."""
    out = []
    for rule in rules:
        if rule["op"] == "pct_change":
            col, lag = header.index(rule["col"]), rule["lag"]
            if len(rows) > lag:
                new, old = number(rows[-1][col]), number(rows[-1 - lag][col])
                if new is not None and old:
                    out.append(f"{rule['name']}: {100 * (new - old) / old:.1f}% (computed from {rows[-1][0]} {rows[-1][col]} and "
                               f"{rows[-1 - lag][0]} {rows[-1 - lag][col]})")
        elif rule["op"] == "ratio_pct":
            num, den, stated = header.index(rule["num"]), header.index(rule["den"]), header.index(rule["check_against"])
            bad = []
            for r in rows:
                n, d, s = number(r[num]), number(r[den]), number(r[stated])
                if n is not None and d and s is not None and abs(100 * n / d - s) > rule.get("tolerance", 0.2):
                    bad.append(f"{r[0]}: stated {s}, computed {100 * n / d:.1f}")
            out.append(f"{rule['name']}: " + ("all rows agree within the tolerance" if not bad else "DISAGREES " + "; ".join(bad)))
    return out


def age_days(as_of: str, run: date):
    try:
        return (run - date.fromisoformat(as_of)).days
    except (TypeError, ValueError):
        return None


def build_line(spec_line: dict, brain: Path, run: date) -> dict:
    result = {"id": spec_line["id"], "label": spec_line["label"], "required": bool(spec_line.get("required")),
              "as_of": spec_line.get("as_of"), "state": "ok", "content": [], "derived": [], "source": spec_line.get("source", "")}
    if not spec_line.get("file"):
        result.update(state="missing", gap=spec_line.get("gap", "no source"))
        return result
    path = brain / spec_line["file"]
    block = read_section(path.read_text(encoding="utf-8"), spec_line["heading"]) if path.exists() else ""
    if not block:
        result.update(state="missing", gap=f"{spec_line['file']} has no section '{spec_line['heading']}'")
        return result
    result["source"] = f"{spec_line['file']} {spec_line['heading']}"
    if spec_line.get("kind") == "table":
        header, rows = parse_table(block)
        keep = rows[-spec_line.get("last_rows", len(rows)):]
        result["content"] = ["| " + " | ".join(header) + " |"] + ["| " + " | ".join(r) + " |" for r in keep]
        result["derived"] = derive(header, rows, spec_line.get("derive", []))
    else:
        lines = [l for l in block.splitlines() if l.strip()]
        result["content"] = lines[: spec_line.get("max_lines", 8)]
    age = age_days(spec_line.get("as_of"), run)
    limit = spec_line.get("max_age_days")
    if age is not None and limit is not None and age > limit:
        result.update(state="stale", gap=f"as of {spec_line['as_of']}, {age} days old, limit {limit}")
    if spec_line.get("partial"):
        result["partial"] = spec_line["partial"]
    if spec_line.get("web_source"):
        result["state"] = "unverified"
        result["gap"] = f"web source ({spec_line['web_source']}) not read against the filing"
    return result


def build_pack(spec: dict, brain: Path, run: date) -> str:
    lines = [build_line(l, brain, run) for l in spec["lines"]]
    missing = [l for l in lines if l["state"] == "missing" and l["required"]]
    stale = [l for l in lines if l["state"] == "stale"]
    unverified = [l for l in lines if l["state"] == "unverified"]
    partial = [l for l in lines if l.get("partial") and l["state"] != "missing"]
    holes = missing + [l for l in unverified if l["required"]]
    gate = "BRIEF COMPLETE" if not (holes or stale or partial) else (
        "BRIEF INCOMPLETE: " + "; ".join(filter(None, [
            "missing " + ", ".join(l["id"] for l in missing) if missing else "",
            "unverified " + ", ".join(l["id"] for l in unverified if l["required"]) if any(l["required"] for l in unverified) else "",
            "stale " + ", ".join(l["id"] for l in stale) if stale else "",
            "partial " + ", ".join(l["id"] for l in partial) + " (see each Partial note)" if partial else ""])))
    out = [START, f"## Data pack: {spec['company']}, built {run.isoformat()} by build_data_pack.py", "",
           f"**{gate}**", ""]
    if holes or stale or partial:
        out += ["The Chair tells the user before Round 1 and asks: fetch first, or run knowing the holes. If S5, S6 or S7 lines are missing the "
                "Analyst writes \"brief incomplete\" before scoring and those sections score 0 `no data`. Nobody fills a hole.", ""]
    for l in lines:
        tag = {"ok": "ok", "missing": "MISSING", "stale": "STALE", "unverified": "UNVERIFIED"}[l["state"]]
        req = " (required)" if l["required"] else ""
        asof = f", as of {l['as_of']}" if l.get("as_of") else ""
        out.append(f"### {l['id']} {l['label']}{req}: {tag}{asof}")
        if l.get("source"):
            out.append(f"Source: {l['source']}")
        if l.get("gap"):
            out.append(f"Gap: {l['gap']}")
        if l.get("partial"):
            out.append(f"Partial: {l['partial']}")
        out += l["content"] + [f"Derived by code: {d}" for d in l["derived"]] + [""]
    out.append(END)
    return "\n".join(out)


def write_into_brief(session: Path, pack: str) -> None:
    brief = session / "brief.md"
    text = brief.read_text(encoding="utf-8") if brief.exists() else ""
    if START in text and END in text:
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
        text = head + pack + tail
    else:
        text = pack + "\n\n" + text
    session.mkdir(parents=True, exist_ok=True)
    brief.write_text(text, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spec", required=True, type=Path)
    ap.add_argument("--run-date", default=date.today().isoformat())
    ap.add_argument("--session", type=Path)
    args = ap.parse_args()
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    brain = (ROOT / "brains" / spec["brain"]) if not Path(spec["brain"]).is_absolute() else Path(spec["brain"])
    pack = build_pack(spec, brain, date.fromisoformat(args.run_date))
    if args.session:
        write_into_brief(args.session, pack)
        print(pack.splitlines()[3])
    else:
        print(pack)
    return 0


if __name__ == "__main__":
    sys.exit(main())
