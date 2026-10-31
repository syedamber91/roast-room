#!/usr/bin/env python3
"""Retry-loop trial: does the guard's feedback fix a free model's answers? Uses convict_loop.run_turn on the 15 trial turns.

    python loop_trial.py <model> [--threads 2]

Answers land in <session>/work/model-trial/<model>-loop/run1/ so `model_trial.py score <model>-loop` scores them.
The escalation log (one line per turn) lands beside them as escalations.jsonl.
"""
import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from convict_loop import run_turn  # noqa: E402
from model_trial import ISSUES, SESSION, TRIAL, TURNS, safe  # noqa: E402


def run_loop(model: str, threads: int) -> dict:
    hearing = (SESSION / "hearing.md").read_text()
    out = TRIAL / (safe(model) + "-loop")
    (out / "run1").mkdir(parents=True, exist_ok=True)
    log = out / "escalations.jsonl"
    log.write_text("")

    def one(job):
        issue, turn = job
        res = run_turn(model, issue, turn, hearing, log)
        (out / "run1" / f"{issue}-{turn}.md").write_text(res["text"])
        print(job, "tries", res["tries"], "ESCALATE" if res["escalate"] else "ok", res["seconds"], "s", flush=True)
        return res

    with ThreadPoolExecutor(threads) as ex:
        results = list(ex.map(one, [(i, t) for i in ISSUES for t in TURNS]))
    summary = {"model": model, "turns": len(results), "escalated": sum(r["escalate"] for r in results),
               "tries": [r["tries"] for r in results]}
    (out / "loop-summary.json").write_text(json.dumps(summary))
    return summary


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("model")
    ap.add_argument("--threads", type=int, default=2)
    a = ap.parse_args()
    print(json.dumps(run_loop(a.model, a.threads)))
