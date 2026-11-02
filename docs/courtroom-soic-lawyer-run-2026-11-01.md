# BIOCON hearing with the SOIC seat as lawyer (2026-11-01)

Session folder: `sessions/2026-11-01-court-biocon-soic-lawyer/`. Artifact: https://claude.ai/artifact/N1JgtiJxJdJDqCVE3nnowD (private).

## What was run
Same case book, same BIOCON convict seat (`council-biocon`) and same judge (`court-judge`) as the first hearing. The lawyer was the SOIC seat (`council-soic`, brain `brains/soic-analyst/`) instead of the Analyst. All ten issues, no baseline sheet.
- Models: Sonnet (high effort) asked each lawyer question and wrote each convict answer. Opus (high effort) wrote the lawyer's issue review for each issue, the cross-examination (4 questions), the lawyer's closing, and every judge turn (ten notes, ten closes, the final).
- Questions: 40 in the ten issues, 4 on every issue, plus 4 cross-examination questions on I4 and I9 (the two weakest by count of no-data states). 23 different SOIC source ids cited in WHY I ASK.
- Code guards, all on: the old ones plus `lawyer-method` (every lawyer question names a source id found in the lawyer's own brain) and `question-count` (2 to 5 per issue). Final state: 0 failures.
- Result by the unchanged code rules: trust 5 of 21, position Wait. The Analyst-lawyer hearing gave 6 of 21, Wait. S1 2, S2 0, S3 0, S4 0, S5 1, S6 2, S7 0.

## What did not work as intended (read before quoting)
- **The 2-to-5 freedom was not used.** Every issue ended at exactly 4 questions. The lawyer's rule allowed stopping early only once the decisive question was answered, and on no issue was it. So this run does not show the SOIC lawyer choosing fewer or more questions.
- **Opus review's extra questions were not asked.** The review step proposed an EXTRA question on several issues (I2, I5, I9 and others); none was run, to hold the cost. The judge lists each as a watch item.
- **One lawyer draft opened a BIOCON company brain file** (I10 Q1, `qa-states.md`). That draft was deleted and re-run with an explicit ban. A transcript check of the other ten lawyer runs found no such read. One convict cross answer (XA3) reports reading more brain files than its three-file limit allowed; it says it used only the allowed ones. Not machine-checked.
- **The first closings were rewritten.** The first lawyer's closing listed I5 and I9 points as answered while the judge scored both decisive questions no data (the agents had read only parts of the 397 KB hearing). Both closings were re-run from `work/state-table.md` (the judge's states per issue) and the artifact republished as version 2. The convict's closing now states that its cross answer and case book chapter 9 differ on borrowing cost capitalised for the year to 2025-03-31 (5,884 vs 1,782 million) and does not settle it. That difference is still not reconciled by a human. The judge's final was written before the rewrite and was not re-run; the scores come from the issue states, which did not change.
- **Rewrites forced by the code checks:** an invented quote (I4 Q1), undated figures (I7 A2, I1 A3, I6 A3, I7 A3, I1 A4, I7 WA2, I10 A3, I1 WA, I6 WA1, I2 WA2, XA2 twice), a 373-word answer (XA2), a quote with no id (I10 A2, XA4), a number not in the case book (I5 review), a quote not in the hearing (I5 judge note). Every one was re-run until the guard passed. A rewrite fixes the form, not whether the answer is right.
- **Question-id clash.** The judge final reuses the ids Q2.91 to Q2.93 for I4 (S2) and I10 (S1). The judge listed them once under S2, so S1 lists only Q2.6 for I10. S1's ceiling is fixed at 2 by the no-guidance rule, so the score does not change.
- **The S1 no-guidance case ("numeric")** was carried over from the first hearing by the Chair, not re-derived.
- **A usage limit** stopped about 20 agents mid-run once; they were re-sent.

## Cost shape
About 300 agent calls, roughly 40 on Opus. Not measured in tokens.

## Tests
`test_check_hearing.py` (3 new), `test_assemble_hearing.py`, `test_next_steps.py`, `test_add_method_panel.py`. `make_cards.py` and `stage_cards.py` have no tests of their own.
