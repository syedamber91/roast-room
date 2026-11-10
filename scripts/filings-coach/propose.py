"""Find what is new since the framework was last built, and set up a proposed change for review.

The framework never changes on its own. This script only lists:
  - new checks: verified checks that no framework step cites yet
  - retired checks: checks a step cites whose source was removed (they no longer hold)
  - re-check: checks a step cites whose source text changed since it was read (they may no longer hold)
and writes them to merge/proposal-input.tsv plus merge/retired.json.

A Sonnet router (brief: PROPOSE.md) then routes each new check to an existing step id, a new step, or
"no step", and an Opus reviewer turns that into docs/filings-coach/proposals/<date>.md. The owner approves
it before docs/filings-coach/framework.md and framework-map.json change.

    python3 propose.py
"""
import json

from paths import FRAMEWORK_MAP, MERGE, PENDING
from merge import COMPACT_FIELDS


def cited_ids(framework_map):
    ids = set()
    for step in framework_map.get("steps", {}).values():
        ids.update(step.get("ids", []))
    return ids


def main():
    if not FRAMEWORK_MAP.exists():
        raise SystemExit(f"no {FRAMEWORK_MAP} yet: build and approve the first framework before proposing changes")
    framework_map = json.loads(FRAMEWORK_MAP.read_text())
    already = cited_ids(framework_map) | set(framework_map.get("unused", [])) | set(framework_map.get("misfits_resolved", []))
    rows = json.loads((MERGE / "all-checks.json").read_text())
    new_rows = [r for r in rows if r["id"] not in already]

    removed_path = PENDING / "removed.json"
    removed_sources = set(json.loads(removed_path.read_text())) if removed_path.exists() else set()
    changed_path = PENDING / "changed.json"
    changed_sources = set(json.loads(changed_path.read_text())) if changed_path.exists() else set()
    by_id = {r["id"]: r for r in rows}
    cited = cited_ids(framework_map)
    # Retired: the check is gone, or its source was removed. Re-check: its source text changed since.
    retired = sorted(i for i in cited if i not in by_id or by_id[i].get("source") in removed_sources)
    recheck = sorted(i for i in cited if i in by_id and by_id[i].get("source") in changed_sources)

    lines = ["\t".join(COMPACT_FIELDS + ("level_hint",))]
    for r in new_rows:
        cells = [str(r.get(k) or "").replace("\t", " ").replace("\n", " ") for k in COMPACT_FIELDS + ("level_hint",)]
        lines.append("\t".join(cells))
    (MERGE / "proposal-input.tsv").write_text("\n".join(lines) + "\n")
    (MERGE / "retired.json").write_text(json.dumps({"retired": retired, "recheck": recheck}, indent=1))
    print(f"new checks to route: {len(new_rows)}  retired support: {len(retired)}  "
          f"support to re-check (source changed): {len(recheck)}")
    print("next: run the Sonnet router with scripts/filings-coach/PROPOSE.md, then the Opus review")


if __name__ == "__main__":
    main()
