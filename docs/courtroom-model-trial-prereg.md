# Model trial, pre-registration (written 2026-10-31, before any trial answer was read)

Question: can a free NVIDIA-hosted model do the CONVICT turns of the courtroom as well as Sonnet, so those turns can leave the paid models? Judge turns are out of scope (nothing checks a judge's reasoning).

## Method
- 15 turns: issues I5, I6, I7, each A1, A2, A3 (question only, as Sonnet saw it) and WA1, WA2.
- Same prompt text and same brain files for every model: the convict answer prompt from `references/hearing-prompts.md`, `_hot.md`, the issue's `convict_files`, the question. Files are pasted into the prompt, because a hosted model cannot open files.
- Baseline = the Sonnet convict answers already in `hearing.md` (the re-heard ones, S039 pages included).
- Each model runs the 15 turns twice (temperature 0, but runs still differ).
- Scoring is code: `check_hearing.check()` on a copy of the hearing with the model's answers swapped in. Only FAIL notes for those 15 turns count.
- Models: every one in the build.nvidia.com catalog that answers a chat call and has a context window for the prompt. Catalog entries that return 404 or time out are reported, not scored.

## Bars (fixed now)
A model PASSES only if all four hold:
1. **Guard:** mean FAIL notes per turn is no worse than Sonnet's own on the same 15 turns.
2. **Fabrication:** zero `quote not found in the convict's brain` notes in its 30 runs (a quote the brain does not hold is an invented quote).
3. **States:** its STATE I CLAIM equals Sonnet's on at least 12 of 15 turns (80%, the D11 bar scaled).
4. **Stability:** its two runs agree on STATE I CLAIM on at least 12 of 15 turns.

Not scored by code, so not claimed: whether the figures in an answer are right beyond the guard's checks (dates present, quotes verbatim, ids exist). A model that passes still needs a human or Sonnet spot-check of 5 answers before any real use.

## What a pass allows
Moving CONVICT turns for the passing model to a retry-on-guard-fail loop. Nothing else. Judge turns, lawyer turns and the final stay on Claude until tested the same way.
