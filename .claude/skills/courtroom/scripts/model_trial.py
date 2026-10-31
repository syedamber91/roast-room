#!/usr/bin/env python3
"""Model trial: can a free model write the convict turns? Pre-registered in docs/courtroom-model-trial-prereg.md.

    python model_trial.py run   <model> [--runs 2]     # call the model, save answers
    python model_trial.py score <model>                # swap answers into a hearing copy, run the guard, print the table
    python model_trial.py table                        # all models scored so far

Small steps, one function each. Answers land in <session>/work/model-trial/<model>/run<N>/<issue>-<turn>.md
"""
import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_hearing as ch  # noqa: E402
from extract_handback import plain_labels  # noqa: E402
from nvidia_client import chat  # noqa: E402

ROOT = HERE.parents[3]
SESSION = ROOT / "sessions" / "2026-10-30-court-biocon-live-example"
BRAIN = ROOT / ".claude" / "skills" / "roast-room" / "brains" / "biocon-management"
ISSUES = ["I5", "I6", "I7"]
TURNS = ["A1", "A2", "A3", "WA1", "WA2"]
TRIAL = SESSION / "work" / "model-trial"


def safe(model: str) -> str:
    return model.replace("/", "__")


# ---- step 1: what each turn asks --------------------------------------------------------------------------------------------------------
def convict_files(issue: str) -> list:
    issues = json.loads((HERE.parent / "references" / "issues.json").read_text())
    rows = issues if isinstance(issues, list) else issues.get("issues", issues)
    return next(r["convict_files"] for r in rows if r["id"] == issue)


def question_text(issue: str, turn: str) -> str:
    """A1..A3: the lawyer's Q1..Q3 from the re-heard file. WA1/WA2: the judge's question file."""
    if turn.startswith("WA"):
        text = (SESSION / "work" / "reheard" / f"{issue}-WAQ.md").read_text()
        return re.search(rf"### {turn} Judge question\s+(.+?)(?=\n###|\Z)", text, re.S).group(1).strip()
    n = turn[1]
    text = (SESSION / "work" / "reheard" / f"{issue}-QA.md").read_text()
    return re.search(rf"### Q{n} Lawyer\s+(.+?)(?=\n### )", text, re.S).group(1).strip()


# ---- step 2: the prompt (same for every model) -------------------------------------------------------------------------------------------
def answer_prompt_rules() -> str:
    text = (HERE.parent / "references" / "hearing-prompts.md").read_text()
    block = re.search(r"### Convict answer.+?```\n(.+?)```", text, re.S).group(1)
    shape = re.search(r"## The convict's answer shape.+?```\n(.+?)```", text, re.S).group(1)
    return block.strip() + "\n\nANSWER SHAPE:\n" + shape.strip()


def build_prompt(issue: str, turn: str) -> str:
    files = ["_hot.md"] + convict_files(issue)
    docs = "\n\n".join(f"===== FILE {f} =====\n{(BRAIN / f).read_text()}" for f in files)
    return (f"{answer_prompt_rules()}\n\nYou cannot open files; the files you may use are pasted below. "
            f"Use ONLY them. Reply with the answer only, starting at the ANSWER line, no preface, no headings.\n\n"
            f"{docs}\n\n===== QUESTION ({issue} {turn}) =====\n{question_text(issue, turn)}\n")


# ---- step 3: run -------------------------------------------------------------------------------------------------------------------------
def clean(text: str) -> str:
    text = re.sub(r"^```\w*\n|\n```$", "", text.strip())
    return plain_labels(text)


def run_model(model: str, runs: int) -> None:
    jobs = [(r, i, t) for r in range(1, runs + 1) for i in ISSUES for t in TURNS]

    def one(job):
        r, i, t = job
        out = TRIAL / safe(model) / f"run{r}"
        out.mkdir(parents=True, exist_ok=True)
        res = chat(model, build_prompt(i, t), max_tokens=12000, timeout=900)
        (out / f"{i}-{t}.md").write_text(clean(res["text"]) if res["text"] else "")
        (out / f"{i}-{t}.meta.json").write_text(json.dumps({"seconds": res["seconds"], "error": res["error"]}))
        return job, res

    with ThreadPoolExecutor(4) as ex:
        for job, res in ex.map(one, jobs):
            print(job, res["seconds"], "s", res["error"] or f"{len(res['text'])} chars", flush=True)


# ---- step 4: score -----------------------------------------------------------------------------------------------------------------------
def swap_turn(hearing: str, issue: str, turn: str, body: str) -> str:
    sec = re.search(rf"(?ms)^## {issue} .*?(?=^## |\Z)", hearing)
    new = re.sub(rf"(?ms)(^### {turn} Convict\n).*?(?=^### |\Z)", lambda m: m.group(1) + "\n" + body.strip() + "\n\n", sec.group(0), count=1)
    return hearing[:sec.start()] + new + hearing[sec.end():]


def state_of(body: str) -> str:
    m = re.search(r"STATE I CLAIM:\s*(.+)", body)
    return m.group(1).strip().lower().strip("*. ") if m else "missing"


def guard_notes(hearing: str) -> list:
    case_book = (SESSION / "case-book.md").read_text()
    external = (SESSION / "external.md").read_text() if (SESSION / "external.md").exists() else ""
    return [p for p in ch.check(hearing, case_book, ch.BRAINS / "biocon-management", ch.BRAINS / "india-market-analyst", external)
            if p.severity == "FAIL"]


def count_for(problems: list, labels: set) -> tuple:
    mine = [p for p in problems if p.turn in labels]
    return len(mine), sum("not found in the convict's brain" in p.message for p in mine)


def score(model: str) -> dict:
    base = (SESSION / "hearing.md").read_text()
    labels = {f"{i} {t} Convict" for i in ISSUES for t in TURNS}
    sonnet_states = {}
    for i in ISSUES:
        sec = re.search(rf"(?ms)^## {i} .*?(?=^## |\Z)", base).group(0)
        for t in TURNS:
            sonnet_states[(i, t)] = state_of(re.search(rf"(?ms)^### {t} Convict\n(.*?)(?=^### |\Z)", sec).group(1))
    sonnet_fails, _ = count_for(guard_notes(base), labels)
    result = {"model": model, "sonnet_fail_notes": sonnet_fails, "runs": {}}
    states = {}
    for run_dir in sorted((TRIAL / safe(model)).glob("run*")):
        h, st = base, {}
        for i in ISSUES:
            for t in TURNS:
                body = (run_dir / f"{i}-{t}.md").read_text() if (run_dir / f"{i}-{t}.md").exists() else ""
                st[(i, t)] = state_of(body) if body else "missing"
                h = swap_turn(h, i, t, body or "ANSWER: (no answer)")
        fails, fab = count_for(guard_notes(h), labels)
        match = sum(st[k] == sonnet_states[k] for k in st)
        result["runs"][run_dir.name] = {"fail_notes": fails, "fabricated_quotes": fab, "state_matches_sonnet": match,
                                        "empty": sum(v == "missing" for v in st.values())}
        states[run_dir.name] = st
    names = list(states)
    if len(names) >= 2:
        result["self_agreement"] = sum(states[names[0]][k] == states[names[1]][k] for k in states[names[0]])
    return result


def verdict(r: dict) -> str:
    runs = r["runs"].values()
    ok = (all(x["fail_notes"] / 15 <= r["sonnet_fail_notes"] / 15 for x in runs) and all(x["fabricated_quotes"] == 0 for x in runs)
          and all(x["state_matches_sonnet"] >= 12 for x in runs) and r.get("self_agreement", 0) >= 12)
    return "PASS" if ok else "FAIL"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["run", "score", "table"])
    ap.add_argument("model", nargs="?")
    ap.add_argument("--runs", type=int, default=2)
    a = ap.parse_args()
    if a.cmd == "run":
        run_model(a.model, a.runs)
    elif a.cmd == "score":
        r = score(a.model)
        r["verdict"] = verdict(r)
        (TRIAL / safe(a.model) / "score.json").write_text(json.dumps(r, indent=1))
        print(json.dumps(r, indent=1))
    else:
        for p in sorted(TRIAL.glob("*/score.json")):
            r = json.loads(p.read_text())
            print(r["model"], r["verdict"], r["runs"], "self", r.get("self_agreement"), "sonnet_fails", r["sonnet_fail_notes"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
