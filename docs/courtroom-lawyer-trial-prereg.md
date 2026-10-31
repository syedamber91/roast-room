# Lawyer-turn trial, pre-registration (written 2026-10-31, before any model was run and before any harness code existed)

Question: can a free NVIDIA-hosted model write the LAWYER questions of the courtroom (Q1, Q2, Q3 of an issue) as well as Sonnet, so those turns can leave the paid models? Convict turns are covered by `docs/courtroom-model-trial-prereg.md`; judge turns are out of scope.

## Method
- 9 turns: issues I5, I6, I7, each Q1, Q2, Q3.
- Same prompt text for every model: the lawyer question prompt from `references/hearing-prompts.md` ("Lawyer question (Q1, Q2, Q3)"), with these pasted in, because a hosted model cannot open files: the lawyer brain's `_hot.md`, the `### Q` sections of `questions.md` for the issue's Analyst question ids, `case-book.md`, and the issue's section of the hearing up to the turn before (so Q2 sees Q1 and A1, Q3 sees Q1 to A2). Nothing from any company brain.
- The previous answer is the Sonnet convict answer already in the hearing. A model's own Q1 is NOT fed forward into its Q2: each turn is tested on identical inputs, so a difference between models is a difference in that one turn.
- The ladder row (what the lawyer must do given the convict's last state) is filled by code from the previous answer's STATE I CLAIM, so no model picks its own row.
- Baseline = the Sonnet lawyer questions already in the re-heard files (`work/reheard/I5-QA.md` and the I6, I7 equivalents).
- Each model runs the 9 turns twice.
- Scoring is code: `check_hearing.check()` on a copy of the hearing with the model's questions swapped in. Only FAIL notes on those 9 lawyer turns count.
- Models: the ones the convict trial found answering a chat call. A model that returns nothing or errors is reported, not scored.

## Bars (fixed now)
A model PASSES only if all four hold, in both of its runs unless a bar says otherwise:
1. **Guard:** mean FAIL notes per lawyer turn is no worse than Sonnet's own on the same 9 turns.
2. **No invented numbers:** zero `lawyer-number` notes (a number of three digits or more that is in neither the case book nor an earlier turn) in its 18 runs.
3. **One short question:** every QUESTION is under 60 words. (The guard's own limit is 70; this bar is stricter, as the prompt asks for 60.) Every one of the 18 must hold; one over is a fail.
4. **Stability:** its two runs name the same first Analyst question id in WHY I ASK on at least 7 of 9 turns (80%, rounded up, the convict trial's bar scaled).

Not scored by code, so not claimed: whether a question is a good question, or follows the ladder row in spirit. The guard checks shape, quotes and numbers only. A model that passes still needs a Sonnet spot-check of 5 questions before any real use.

## What a pass allows
Moving LAWYER Q1 to Q3 turns for the passing model to a retry-on-guard-fail loop. Nothing else. Judge turns, cross-examination and closing stay on Claude until tested the same way.
