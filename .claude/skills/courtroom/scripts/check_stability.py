#!/usr/bin/env python3
"""Test 2 of docs/courtroom-design.md: is one company's decision stable across repeat hearings?

    python check_stability.py runA/dashboard.json runB/dashboard.json runC/dashboard.json

The bar was written before any run: across all repeat runs the position must be identical, and for
every pair of runs the seven section scores may differ in at most ONE section and by at most ONE
point. Anything else prints NOT STABLE and the position must not be printed as a finding.
"""

import itertools
import json
import sys
from pathlib import Path

MAX_SECTIONS_DIFFERING = 1
MAX_POINTS = 1


def summary(dashboard: dict) -> tuple:
    d = dashboard["decision"]
    return d["position"]["key"], {r["section"]: r["final"] for r in d["scores"]}


def compare(runs: list) -> dict:
    """runs: list of dashboard dicts. Returns {stable, reasons, positions, pairs}."""
    parsed = [summary(r) for r in runs]
    reasons = []
    if len(parsed) < 2:
        return {"stable": False, "reasons": ["need at least two runs, the design asks for three"], "positions": [p for p, _ in parsed], "pairs": []}
    positions = [p for p, _ in parsed]
    if len(set(positions)) > 1:
        reasons.append("positions differ: " + ", ".join(positions))
    pairs = []
    for (i, (_, a)), (j, (_, b)) in itertools.combinations(enumerate(parsed), 2):
        diffs = {s: abs(a[s] - b[s]) for s in a if a[s] != b[s]}
        pairs.append({"runs": (i + 1, j + 1), "sections_differing": len(diffs), "largest_gap": max(diffs.values(), default=0), "diffs": diffs})
        if len(diffs) > MAX_SECTIONS_DIFFERING:
            reasons.append("runs %d and %d differ in %d sections (%s), limit %d" % (i + 1, j + 1, len(diffs), ", ".join(sorted(diffs)), MAX_SECTIONS_DIFFERING))
        elif diffs and max(diffs.values()) > MAX_POINTS:
            reasons.append("runs %d and %d differ by %d points in %s, limit %d" % (i + 1, j + 1, max(diffs.values()), ", ".join(sorted(diffs)), MAX_POINTS))
    return {"stable": not reasons, "reasons": reasons, "positions": positions, "pairs": pairs}


def main() -> int:
    runs = [json.loads(Path(p).read_text(encoding="utf-8")) for p in sys.argv[1:]]
    result = compare(runs)
    print("positions:", ", ".join(result["positions"]))
    for pair in result["pairs"]:
        print("runs %d and %d: %d section(s) differ, largest gap %d" % (pair["runs"][0], pair["runs"][1], pair["sections_differing"], pair["largest_gap"]))
    print("STABLE" if result["stable"] else "NOT STABLE: " + "; ".join(result["reasons"]))
    return 0 if result["stable"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
