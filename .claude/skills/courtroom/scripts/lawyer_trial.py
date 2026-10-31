#!/usr/bin/env python3
"""Lawyer-turn trial: can a free model write the lawyer's Q1-Q3? Pre-registered in docs/courtroom-lawyer-trial-prereg.md.

    python lawyer_trial.py run   <model> [--runs 2]   # call the model, save questions
    python lawyer_trial.py score <model>              # swap questions into a hearing copy, run the guard, print the table
    python lawyer_trial.py table                      # all models scored so far

Sibling of model_trial.py (the convict trial) and reuses its client, cleaning and guard wrapper.
Questions land in <session>/work/lawyer-trial/<model>/run<N>/<issue>-Q<n>.md
Every turn is tested on identical inputs: the history is Sonnet's own earlier turns, never the model's.
"""
import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import model_trial as mt  # noqa: E402
from nvidia_client import chat  # noqa: E402

SESSION = mt.SESSION
LAWYER_BRAIN = mt.BRAIN.parent / "india-market-analyst"
ISSUES = mt.ISSUES
QUESTIONS = (1, 2, 3)
TRIAL = SESSION / "work" / "lawyer-trial"
PROMPTS = HERE.parent / "references" / "hearing-prompts.md"
MAX_QUESTION_WORDS = 60   # prereg bar 3: under 60
MIN_SELF_AGREEMENT = 7    # prereg bar 4: 7 of 9


# ---- step 1: what the lawyer sees --------------------------------------------------------------------------------------------------------
def issue_section(hearing: str, issue: str) -> str:
    return re.search(rf"(?ms)^## {issue} .*?(?=^## |\Z)", hearing).group(0)


def history_before(section: str, n: int) -> str:
    """The issue section up to (not including) lawyer turn Qn: what the real lawyer had read when it asked."""
    return section[:re.search(rf"(?m)^### Q{n} Lawyer", section).start()]


def normalise_state(raw: str) -> str:
    return re.split(r"[.:(]", raw)[0].strip().lower().strip("* ")


def last_state(history: str) -> str:
    states = re.findall(r"STATE I CLAIM:\s*(.+)", history)
    return normalise_state(states[-1]) if states else ""


def ladder_rows(prompts_md: str) -> dict:
    """The escalation table, read from hearing-prompts.md so the trial and the real hearing use one ladder."""
    rows = re.findall(r"^\| (answered|partial[^|]*|deflected|not in my record) \| ([^|]+) \|$", prompts_md, re.M)
    return {normalise_state(state): row.strip() for state, row in rows}


def ladder_instruction(n: int, state: str, ladder: dict) -> str:
    if n == 1:
        return "Ask the decisive question, in your own words, with the number and date you want back."
    return f"The convict's last state was {state}. Apply the ladder: {ladder[state]}."


def question_sections(questions_md: str, ids: list) -> str:
    """The '### Q' sections for the given Analyst question ids; an id that is not there is named, never skipped."""
    out = []
    for qid in ids:
        m = re.search(rf"(?ms)^### {re.escape(qid)} .*?(?=^### |\Z)", questions_md)
        out.append(m.group(0).strip() if m else f"### {qid}\n(NOT FOUND in questions.md)")
    return "\n\n".join(out)


# ---- step 2: the prompt (same for every model) -------------------------------------------------------------------------------------------
def lawyer_rules(prompts_md: str) -> str:
    """The lawyer question prompt from hearing-prompts.md, with the file-reading line removed (the files are pasted instead)."""
    block = re.search(r"### Lawyer question \(Q1, Q2, Q3\)\s+```\n(.+?)```", prompts_md, re.S).group(1)
    return "\n".join(l for l in block.splitlines() if not l.startswith("Repo root:")).strip()


def fill_rules(rules: str, issue: dict, n: int, instruction: str) -> str:
    """Fill the template's placeholders; keep the line for this question number and drop the other."""
    text = "\n".join(l for l in rules.splitlines() if not l.startswith("[For Q"))
    head, found, tail = text.partition("Answer in exactly this shape")
    text = f"{head.rstrip()}\n{instruction}\n\n{found}{tail}" if found else f"{text}\n{instruction}"
    state = f"{issue.get('state', 'unknown')}" + (f" ({'; '.join(issue['reasons'])})" if issue.get("reasons") else "")
    for key, value in {"[issue id and name]": f"{issue['id']} {issue['name']}", "[n]": str(n),
                       "[analyst_questions]": ", ".join(issue["analyst_questions"]), "[decisive]": issue["decisive"],
                       "[state and reasons from case.json]": state, "[known_gaps]": "; ".join(issue["known_gaps"])}.items():
        text = text.replace(key, value)
    return text


def build_prompt_from_parts(rules: str, issue: dict, n: int, state: str, ladder: dict, hot: str, questions: str,
                            case_book: str, history: str) -> str:
    filled = fill_rules(rules, issue, n, ladder_instruction(n, state, ladder))
    return (f"{filled}\n\nYou cannot open files; everything you may use is pasted below. Use ONLY it. "
            f"Reply with the four labelled lines only, starting at TO, no preface, no headings.\n\n"
            f"===== FILE _hot.md (your brain) =====\n{hot}\n\n===== YOUR QUESTIONS (Analyst ids) =====\n{questions}\n\n"
            f"===== FILE case-book.md =====\n{case_book}\n\n===== HEARING SO FAR ({issue['id']}) =====\n{history}\n")


def case_issue(issue: str) -> dict:
    case = json.loads((SESSION / "case.json").read_text())
    return next(i for i in case["issues"] if i["id"] == issue)


def build_prompt(issue: str, n: int) -> str:
    row = case_issue(issue)
    history = history_before(issue_section((SESSION / "hearing.md").read_text(), issue), n)
    return build_prompt_from_parts(
        rules=lawyer_rules(PROMPTS.read_text()), issue=row, n=n, state=last_state(history), ladder=ladder_rows(PROMPTS.read_text()),
        hot=(LAWYER_BRAIN / "_hot.md").read_text(), questions=question_sections((LAWYER_BRAIN / "questions.md").read_text(), row["analyst_questions"]),
        case_book=(SESSION / "case-book.md").read_text(), history=history)


# ---- step 3: run -------------------------------------------------------------------------------------------------------------------------
def run_model(model: str, runs: int) -> None:
    jobs = [(r, i, n) for r in range(1, runs + 1) for i in ISSUES for n in QUESTIONS]

    def one(job):
        r, i, n = job
        out = TRIAL / mt.safe(model) / f"run{r}"
        out.mkdir(parents=True, exist_ok=True)
        res = chat(model, build_prompt(i, n), max_tokens=12000, timeout=900)
        (out / f"{i}-Q{n}.md").write_text(mt.clean(res["text"]) if res["text"] else "")
        (out / f"{i}-Q{n}.meta.json").write_text(json.dumps({"seconds": res["seconds"], "error": res["error"]}))
        return job, res

    with ThreadPoolExecutor(4) as ex:
        for job, res in ex.map(one, jobs):
            print(job, res["seconds"], "s", res["error"] or f"{len(res['text'])} chars", flush=True)


# ---- step 4: score -----------------------------------------------------------------------------------------------------------------------
def swap_lawyer_turn(hearing: str, issue: str, n: int, body: str) -> str:
    sec = issue_section(hearing, issue)
    new = re.sub(rf"(?ms)(^### Q{n} Lawyer\n).*?(?=^### |\Z)", lambda m: m.group(1) + "\n" + body.strip() + "\n\n", sec, count=1)
    return hearing.replace(sec, new, 1)


def field(body: str, name: str) -> str:
    m = re.search(rf"(?ms)^{name}:\s*(.+?)(?=^[A-Z][A-Z ]+:|\Z)", body)
    return m.group(1).strip() if m else ""


def first_question_id(body: str) -> str:
    m = re.search(r"\bQ\d+\.\d+\b", field(body, "WHY I ASK"))
    return m.group(0) if m else "missing"


def question_words(body: str) -> int:
    return len(field(body, "QUESTION").split())


def sonnet_questions() -> dict:
    hearing = (SESSION / "hearing.md").read_text()
    return {(i, n): re.search(rf"(?ms)^### Q{n} Lawyer\n(.*?)(?=^### |\Z)", issue_section(hearing, i)).group(1).strip()
            for i in ISSUES for n in QUESTIONS}


def count_for(problems: list, labels: set) -> tuple:
    """(FAIL notes on these lawyer turns, of which lawyer-number notes)."""
    mine = [p for p in problems if p.turn in labels and p.severity == "FAIL"]
    return len(mine), sum(p.guard == "lawyer-number" for p in mine)


def score(model: str) -> dict:
    base = (SESSION / "hearing.md").read_text()
    labels = {f"{i} Q{n} Lawyer" for i in ISSUES for n in QUESTIONS}
    result = {"model": model, "sonnet_fail_notes": count_for(mt.guard_notes(base), labels)[0], "runs": {}}
    ids = {}
    for run_dir in sorted((TRIAL / mt.safe(model)).glob("run*")):
        hearing, bodies = base, {}
        for i in ISSUES:
            for n in QUESTIONS:
                path = run_dir / f"{i}-Q{n}.md"
                bodies[(i, n)] = path.read_text() if path.exists() else ""
                hearing = swap_lawyer_turn(hearing, i, n, bodies[(i, n)] or "QUESTION: (no question)")
        fails, numbers = count_for(mt.guard_notes(hearing), labels)
        result["runs"][run_dir.name] = {"fail_notes": fails, "number_notes": numbers,
                                        "max_question_words": max(question_words(b) for b in bodies.values()),
                                        "empty": sum(not b for b in bodies.values())}
        ids[run_dir.name] = {k: first_question_id(b) if b else "missing" for k, b in bodies.items()}
    names = list(ids)
    if len(names) >= 2:
        result["self_agreement"] = sum(ids[names[0]][k] == ids[names[1]][k] for k in ids[names[0]])
    return result


def verdict(r: dict) -> str:
    runs = r["runs"].values()
    ok = (all(x["fail_notes"] <= r["sonnet_fail_notes"] for x in runs) and all(x["number_notes"] == 0 for x in runs)
          and all(x["max_question_words"] < MAX_QUESTION_WORDS for x in runs) and r.get("self_agreement", 0) >= MIN_SELF_AGREEMENT)
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
        (TRIAL / mt.safe(a.model) / "score.json").write_text(json.dumps(r, indent=1))
        print(json.dumps(r, indent=1))
    else:
        for p in sorted(TRIAL.glob("*/score.json")):
            r = json.loads(p.read_text())
            print(r["model"], r["verdict"], r["runs"], "self", r.get("self_agreement"), "sonnet_fails", r["sonnet_fail_notes"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
