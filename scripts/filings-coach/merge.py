"""Put every verified check in one file and tag how much weight it may carry.

Tiers (how a check may be used in the framework):
  soic       SOIC course check: the main support (India-first)
  book       Berkshire, Marks, Damodaran, Bakshi, Safal, SEBI: backs or adds to a step
  us-guide   investor.gov guides: used only where they add a check India lacks
  classic    pre-1931 public-domain books: "Lessons from market history" box only, never sole support
  +reader-inference   suffix for lines listed in merge/inference-ids.json: never support

Also writes merge/L<level>-compact.tsv, one short line per check, for the Opus drafters.

    python3 merge.py
"""
import json
from collections import defaultdict

from paths import EXTRACT, MERGE

CLASSIC_PREFIXES = {"mackay", "lefevre", "clews", "hamilton", "nelson", "harper", "van", "selden",
                    "bagehot", "butler", "crump", "smith", "duguid"}
COMPACT_FIELDS = ("id", "tier", "source", "cite", "document", "section", "signal", "check", "threshold")


def tier_of(row):
    if row.get("source_kind") != "book":
        return "soic"
    prefix = row["source"].split("-")[0]
    if prefix in CLASSIC_PREFIXES:
        return "classic"
    if prefix == "investorgov":
        return "us-guide"
    return "book"


def read_all():
    verified = json.loads((MERGE / "verified.json").read_text())
    # Lines a reader agent flagged as its own inference (not stated by the source) never count as support.
    inference_file = MERGE / "inference-ids.json"
    inference = set(json.loads(inference_file.read_text())) if inference_file.exists() else set()
    rows = []
    for folder in (EXTRACT, EXTRACT / "books"):
        for f in sorted(folder.glob("*.jsonl")):
            for raw in f.read_text().splitlines():
                if raw.strip():
                    row = json.loads(raw)
                    if verified.get(row["id"]):          # failed lines never enter the merge
                        row["tier"] = tier_of(row) + ("+reader-inference" if row["id"] in inference else "")
                        rows.append(row)
    return rows


def write_compact(rows):
    by_level = defaultdict(list)
    for row in rows:
        level = row.get("level_hint") if row.get("level_hint") in range(1, 8) else 2
        by_level[level].append(row)
    for level, items in sorted(by_level.items()):
        lines = ["\t".join(COMPACT_FIELDS)]
        for row in items:
            cells = [str(row.get(k) or "").replace("\t", " ").replace("\n", " ") for k in COMPACT_FIELDS]
            lines.append("\t".join(cells))
        (MERGE / f"L{level}-compact.tsv").write_text("\n".join(lines) + "\n")
        print(f"level {level}: {len(items)} checks")


def main():
    rows = read_all()
    (MERGE / "all-checks.json").write_text(json.dumps(rows))
    print(f"merged {len(rows)} verified checks")
    write_compact(rows)


if __name__ == "__main__":
    main()
