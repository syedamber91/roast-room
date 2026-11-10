"""Stitch the final level files into the framework, its id map, and its appendices.

Inputs  (build/filings-coach/merge/): final-L1.md ... final-L<N>.md and their .json, cite-lookup.json
Outputs (docs/filings-coach/):
  framework.md        the readable framework (intro, levels, sector packs, citation table, changelog)
  framework-map.json  every stable step id -> the check ids that support it (what propose.py reads)
It also checks that no check id is placed twice across levels, and prints what is left unplaced.

    python3 assemble.py --version 0.1.0 --status "draft for owner review"
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import date

from paths import DOCS, FRAMEWORK_MAP, MERGE

INTRO = """# Filings-reading coach: the leveled framework

Version {version} ({status}), built {today}.

This framework teaches how to read an Indian listed company's own documents to find signals: the annual
report, quarterly results, earnings-call (concall) transcripts, investor presentations, exchange filings,
the shareholding pattern, credit-rating reports and the price chart. It climbs from Level 1 (no prior
knowledge) to Level {top} (deciding, monitoring and knowing when a case is broken).

**What it is not.** It is a reading method, not advice. It never says buy, sell or hold. Where a number
appears, a source states it (cited), or it comes from the soic-ladder rulebook (cited, and marked as a
GATE or a REFERENCE BAND). Where sources disagree, both views are shown. Where no source covers
something a reader needs, it is listed under Gaps rather than filled in from memory.

**Where it comes from.** {n_checks} checks, each verified against its source: SOIC course notes (cited by
note and timestamp; course text is paraphrased, never quoted) and {n_books} free, legal books and documents
(Berkshire Hathaway letters, Howard Marks memos, Damodaran papers, Sanjay Bakshi, Safal Niveshak, SEBI,
investor.gov, and pre-1931 public-domain classics, which appear only in "Lessons from market history").
Every step has a permanent id such as `FC-L3-T2-S4`; new sources attach to these ids through a proposed
change the owner approves (see `scripts/filings-coach/README.md`). Decisions: `DECISIONS.md`.

## The levels
{toc}
"""


def load_levels():
    levels = []
    for path in sorted(MERGE.glob("final-L*.json"), key=lambda p: int(re.search(r"L(\d+)", p.name).group(1))):
        data = json.loads(path.read_text())
        data["_md"] = (MERGE / path.name.replace(".json", ".md")).read_text()
        levels.append(data)
    return levels


def placements(level):
    """Yield (check_id, where) for every place this level puts a check."""
    for task in level.get("tasks", []):
        for sub in task.get("subtasks", []):
            for i in sub.get("ids", []):
                yield i, sub["id"]
    for deep in level.get("deeper", []):
        for i in deep.get("ids", []):
            yield i, deep["id"]
    for sector, ids in (level.get("sector_packs") or {}).items():
        for i in ids:
            yield i, f"sector:{sector}"
    for i in level.get("classics_box", []):
        yield i, f"FC-L{level['level']}-history"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="0.1.0")
    parser.add_argument("--status", default="draft for owner review")
    args = parser.parse_args()

    levels = load_levels()
    rows = json.loads((MERGE / "all-checks.json").read_text())
    all_checks = {r["id"] for r in rows}
    n_books = len({r["source"] for r in rows if not r["tier"].startswith("soic")})
    cite = json.loads((MERGE / "cite-lookup.json").read_text())

    where = defaultdict(list)
    for level in levels:
        for check_id, place in placements(level):
            where[check_id].append(place)
    unused = set()
    for level in levels:
        unused |= set(level.get("unused", []))
    twice = {i: p for i, p in where.items() if len(set(p)) > 1}
    unknown = [i for i in where if i not in all_checks]
    # "Parked": a writer left a check unused with a note that it belongs at another level. If no level then
    # took it, it is not really unused: it waits, with the never-placed ones, for the first proposal round.
    parked_file = MERGE / "parked.json"
    parked = set(json.loads(parked_file.read_text())) if parked_file.exists() else set()
    pending = sorted((all_checks - set(where) - unused) | (parked - set(where)))
    unused -= set(pending)

    # framework-map.json: what the incremental loop reads
    steps, sectors = {}, defaultdict(list)
    for level in levels:
        for task in level.get("tasks", []):
            for sub in task.get("subtasks", []):
                steps[sub["id"]] = {"level": level["level"], "task": task["id"], "title": sub["title"],
                                    "ids": sub.get("ids", []), "lenders": bool(sub.get("lenders"))}
        for deep in level.get("deeper", []):
            steps[deep["id"]] = {"level": level["level"], "title": deep["title"], "ids": deep.get("ids", []),
                                 "deeper": True}
        for sector, ids in (level.get("sector_packs") or {}).items():
            sectors[sector] += ids
    framework_map = {"version": args.version, "status": args.status, "built": date.today().isoformat(),
                     "steps": steps, "sector_packs": {k: sorted(set(v)) for k, v in sectors.items()},
                     "unused": sorted(unused), "placed_twice": twice, "pending": pending}
    DOCS.mkdir(parents=True, exist_ok=True)
    FRAMEWORK_MAP.write_text(json.dumps(framework_map, indent=1, ensure_ascii=False))

    # framework.md
    def plain_title(level):
        # Some writers put "Level N:" inside the title itself; strip it so the contents list reads once.
        return re.sub(r"^Level \d+:\s*", "", level["title"])

    toc = "\n".join(f"- [Level {lv['level']}: {plain_title(lv)}](#level-{lv['level']})" for lv in levels)
    parts = [INTRO.format(version=args.version, status=args.status, today=date.today().isoformat(),
                          top=levels[-1]["level"] if levels else "?", n_checks=len(all_checks),
                          n_books=n_books, toc=toc)]
    for level in levels:
        parts.append(f'<a id="level-{level["level"]}"></a>\n\n' + level["_md"].strip())
    parts.append("## Appendices (separate files, to keep this one readable)\n\n"
                 "- `sector-packs.md`: checks that apply to one NSE sector only, to read alongside the general step.\n"
                 "- `citations.md`: internal check id -> source, for every check the framework uses.\n"
                 f"- `framework-map.json`: every step id -> its check ids; {len(pending)} checks are still pending "
                 "routing and go through the first proposal round.")
    parts.append(f"## Changelog\n\n- {date.today().isoformat()} v{args.version}: first assembly from "
                 f"{len(levels)} levels and {len(where)} placed checks ({args.status}).")
    (DOCS / "framework.md").write_text("\n\n".join(parts) + "\n")

    packs = ["# Sector packs\n\nChecks that apply to one sector only, grouped by NSE sector. The groupings were made "
             "by the level writers and still need a human pass before a pack is used on its own.\n"]
    for sector in sorted(sectors):
        packs.append(f"## {sector}\n\n" + "\n".join(f"- {cite.get(i, i)}" for i in sorted(set(sectors[sector]))))
    (DOCS / "sector-packs.md").write_text("\n\n".join(packs) + "\n")
    (DOCS / "citations.md").write_text(
        "# Citation lookup\n\nInternal check id -> source, for every check the framework places.\n\n| id | source |\n|---|---|\n"
        + "\n".join(f"| {i} | {cite.get(i, '?')} |" for i in sorted(set(where))) + "\n")

    print(f"levels {len(levels)}  steps {len(steps)}  placed {len(where)}  unused {len(unused)}  "
          f"pending {len(pending)}  placed twice {len(twice)}  unknown ids {len(unknown)}")
    print("by level:", dict(Counter(s["level"] for s in steps.values())))


if __name__ == "__main__":
    main()
