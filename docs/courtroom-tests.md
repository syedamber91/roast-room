# Courtroom tests: what each one is, what passes, and where it stands

Written 2026-10-30, before any real hearing was run. The bars below are fixed. A result is written beside its test with its date and is never used to move a bar. Design reference: `docs/courtroom-design.md` section 8.

## Test 1. Planted failures by code (built and passing)

Each guard must catch its plant. The six plants from the design:

| Plant | Guard | Test |
|---|---|---|
| an invented quote | `quote-source` | `test_check_hearing.py::test_each_guard_catches_its_planted_failure` |
| a number with no date | `number-date` | same test |
| a lawyer number not in the case book | `lawyer-number` | same test |
| a storyline line with no id | `judge-story` | same test |
| an E-id used for a company fact | `external-id` | same test, and `test_scout_external.py::test_a_company_fact_answer_resting_on_an_e_id_is_caught_by_the_hearing_guard` |
| a judge score above its ceiling | `judge-ceiling` | `test_build_report.py::test_planted_failure_judge_score_above_its_ceiling_is_cut_and_reported` |

Also planted and caught: a drafted chapter line with no page id, a number not on the cited page, a forward-looking word, six words copied from the call record (`test_check_chapters.py`); injected instructions in an outside item (`test_scout_external.py`); a judge position above the rule, a reader line saying Buy when the position is Wait, a storyline that is not ten lines (`test_build_report.py`).

Run: `python3 -m pytest .claude/skills/courtroom/scripts -q`. Pass bar: all pass.

## Test 2. Stability (harness built; needs three real hearings)

Run the same company's hearing three times. `scripts/check_stability.py run1/dashboard.json run2/dashboard.json run3/dashboard.json`.

Bar, fixed now: the position is identical in all three runs; for every pair of runs the seven section scores differ in at most one section, by at most one point. Otherwise the output says NOT STABLE and the position is not printed as a finding. The harness has its own tests (`test_check_stability.py`). It has not been run on real hearings.

## Test 3. Old cases on paper (protocol fixed; not run, and not runnable from this repo today)

Why it cannot run yet: it needs full-length case books for several companies built only from filings dated before the trouble became public, and this repo holds only the BIOCON record. The earlier 14-case check (`stock-rating.md`, run 2026-10-29) used a few lines per case and showed that thin text puts every case in the 0 to 6 band, so it cannot separate good from bad. This test is the fuller version that note asks for.

Cases, fixed now from `brains/india-market-analyst/stories.md`: three trouble cases whose earlier warning signs were public in filings and calls: story 1 Gensol Engineering (cutoff 2024-08-13, before the March 2025 events), story 3 IndusInd Bank (cutoff 2025-03-09, the day before the derivatives disclosure), and one more governance case chosen by the owner from stories A2 to A10 that has full filings available. Plus two comparison companies chosen by the owner that had no enforcement outcome in the same period, in the same industries.

Build rule: a case book for each, with a cutoff date. Nothing after the cutoff may appear in the case book, the hearing or the report. The builder is run with `--run-date` set to the cutoff; a reader checks the exchange feed and every cited filing date against it.

Bar, fixed now. A trouble case counts as noticed if the court's position is not Buy AND either a gate stands or the section that the later order concerned scores 1 or less. Pass: at least 2 of the 3 trouble cases are noticed, AND no more than 1 of the 2 comparison companies is noticed on the same test. Also reported, never used to pass: the trust totals of all five, so that "everything lands in 0 to 6" is visible if it happens.

Limits to print with any result: the trouble cases were chosen because they went wrong, so a pass shows trouble is noticed, not how often a clean company is wrongly flagged; five cases cannot show the bands work.

## Test 4. A real reader (sheet built; needs a reader)

`build_report.py` writes `reader-card.html` (the decision card alone) and `reader-test-sheet.md` (five questions with a scorer's key) into the session folder. A real 15-year-old, or an adult with no markets background, reads only the card and answers: the position, why, what would change it, what is not decided, what to check next. Bar, fixed now: 4 of 5 answers match the key in meaning, in 5 minutes or less. One reader per company is the minimum; the owner may be the first reader. A reader who scores under the bar, or names something unclear, sends the card back for a plain-words rewrite.

## Standing statement on the page

Nothing here proves a position right. The bands remain untested and every printed decision says so.

## Prompt check: the date rule (2026-10-31)

Question: does stating the date rule the way the guard counts it (within 80 characters of each figure, with the three shapes that failed) cut the undated-figure notes?

Setup: the three convict answers on I5 (A1 to A3) were run again from the same questions with the new prompt wording. The original turns stay in `hearing.md`; the re-runs sit in `sessions/2026-10-30-court-biocon-live-example/work/rerun-I5/`.

Result: `number-date` notes on those three turns went from **21 to 0**, no other guard fired, and the three question states did not change (A1 partial, A2 answered, A3 not in my record).

Limits: one issue, three turns, one run each, and one re-run (A3) reported seeing the earlier answers when it read the file, though it said it did not use them. One run per cell is noise-prone (see the provenance repo's note); a count this large is unlikely to be noise, but it is not a repeated measure. Not tested: the other six issues.

### Date-rule re-run on I6 to I9 (2026-10-31)

Same test on the other four issues, 20 convict turns (A1 to A3, WA1, WA2 each), every agent given only its own question file so none could read the earlier answers. Measured with `scripts/measure_rerun.py`; the re-runs are in `sessions/2026-10-30-court-biocon-live-example/work/rerun-I6` to `rerun-I9`. The recorded turns were not touched.

| Issue | Notes before | Notes after | Of which date notes |
|---|---|---|---|
| I5 (earlier test) | 21 | 0 | 21 to 0 |
| I6 | 9 | 1 | 9 to 1 |
| I7 | 15 | 2 | 14 to 1 |
| I8 | 8 | 0 | 8 to 0 |
| I9 | 2 | 3 | 1 to 0 (and two quote-without-id notes appeared) |
| Total | 55 | 6 | 53 to 2 |

Question states: 21 of 23 re-run turns kept the same state. Two moved up: I6 A2 and I8 A3 went from "not in my record" to "partial" because the re-run found a figure the first run did not. So a re-run is not only a date fix; it can change what the convict says.

Limits: one run per turn, so the movement in content (not the date count) could be noise. A re-run turn that reads a figure the first run missed would also change the judge's notes that rest on the original turns (for example the I7 re-run found a cash figure of 36,242 within the 73,560 price that the recorded I7 turns do not have). The re-runs have not been swapped into `hearing.md`.

### Are the new dates right? A random check (2026-10-31)

177 figure-and-date pairs were found in the 23 re-run convict turns (I5 to I9). A seeded draw (seed 42) took 20; the list is in `sessions/2026-10-30-court-biocon-live-example/work/date-sample.json`. Each was checked by searching the figure in `case-book.md` and the convict's brain files and reading which column, row or sentence carried it.

Result: **20 of 20 carried the period the re-run gave it** (for example 21,366 is the year to 2025-03-31, the second column of the cash-flow table; 728,081,295 is the 30-SEP-2026 shareholding row; 36,242 sits in a sentence that begins "During the year ended March 31, 2026"). One caveat: for 36,242 the note prints "Rs. 36,242" with no unit, and the unit (million) is the convict's inference, which it flagged; it ties (73,560 less 36,242 is 37,318 = 91,967,019 shares at 405.78).

Limits: 18 distinct pairs (21,366 and 40,612 each came up twice); the check is against the case book and the convict's own brain files, so it tests transcription, not the filings themselves; and only pairs that already had a date nearby could be drawn, so it says nothing about figures that still have none.

### Date rule in the baseline and cross-examination prompts (2026-10-31)

The baseline prompt had no date rule, and the baseline why-answers (WA1 to WA3) and cross answers (XA1 to XA4) were written without the 80-character rule. `hearing-prompts.md` now carries both (a B-line with a figure must hold a date word; the why and cross answers use the Convict answer prompt with its date rule). Eight turns were re-run in `sessions/2026-10-30-court-biocon-live-example/work/rerun-BLX/`, each agent seeing only its own question; the recorded turns were not touched.

| Turn | Notes before | Notes after |
|---|---|---|
| Baseline group 1 (B01 to B10) | 7 | 0 |
| Baseline WA1 | 7 | 2 |
| Baseline WA2 | 2 | 0 |
| Baseline WA3 | 6 | 0 |
| XA1 | 6 | 1 |
| XA2 | 3 | 2 |
| XA3 | 6 | 0 |
| XA4 | 8 | 0 |
| Total | 45 | 5 |

Date notes alone: 37 before, 5 after. Five undated figures remain (WA1 two, XA1 one, XA2 two); no other guard fired on the re-runs. One run per turn. Not checked here: whether the question states changed, and whether the new dates are right (the 20-date random check covered I5 to I9 only). Not changed: the lawyer cross prompt still has no word limit on QUESTION, which is why X1 and X3 failed the 70-word turn-shape check.

### Closing the leftovers from the baseline and cross test (2026-10-31)

Five undated figures were left on XA1, XA2 and baseline WA1; all were back-references ("the 3,830", "the 24,692 from I6 WA1"). The prompt now says a figure mentioned again must repeat its date. Those three turns were run again (`work/rerun-BLX2/`): date notes **5 to 1** (WA1 still has one, 148,246 undated). The lawyer cross prompt now limits QUESTION to 60 words and bans quotation marks round case book text; two lawyer questions were run again: 58 and 52 words, no turn-shape or quote notes (before: 83 and 116 words, with 2 quote notes). One new note appeared: the first re-run asked about 86,500, a sum of two case book figures that appears nowhere, so the prompt now also bans worked-out sums (not yet re-tested).

Dates: a second random draw of 20 (seed 7, from 143 pairs on the final baseline and cross re-runs, `work/date-sample-2.json`): **20 of 20** carried the right period. Two notes: 8,786,362 is in the case book's timeline row (no commas, so a comma search misses it), and 5,121 sits in a case book line that prints "5,121 and 18,954" without column labels, so its 2026-03-31 date rests on the other tables listing the current year first.

Question states: they are NOT stable. Across the 18 baseline and cross re-run answers that can be compared (10 B-lines, WA1 to WA3, XA1 to XA4) **7 changed state, all toward less claimed** (B01, B02, B09 partial to not in my record; B07 answered to partial; XA1, XA2, XA3 partial to not in my record). One run per cell, so this may be noise (the provenance repo measured a half-scale spread on repeat runs), or the new "do not print a figure you cannot date" wording may make the convict claim less. Not separated here. It means a re-run swapped into the record could lower scores, which is a reason the record was kept as it is.

## Haiku and Sonnet together, on the open items (2026-10-31)

Page extraction (Haiku reads, Sonnet verifies): 3 of 3 Haiku extractions returned useful, quoted pages, and a Sonnet check found 8 of 8 claim groups correct. Result in `sessions/2026-10-30-court-biocon-live-example/missing-documents-found-2026-10-31.md`. It answers the cash-flow, work-in-progress and borrowings-note gaps the convict listed as "not in my record", and shows which gaps stay open.

Judge stability (same hearing, scores only): four Sonnet readings (the original final plus three repeats) gave trust 7, 5, 7 and 7 and Wait every time. Two sections moved: S1 (1 or 2: whether the no-guidance ceiling of 2 applies when the decisive question is only partial) and S5 (0 or 1: whether the decisive related-party question has "no data" or "partial"). Every other section score was identical in all four. The three Haiku judges all stopped at their 8-turn limit with no scores, so Haiku was not usable for the judge task at this hearing size. Independence caveat: one repeat said it saw another judge's score lines by accident; none of the repeats used a separate copy of the hearing without the earlier final at its end.

Reading: the position does not move; the total moves by up to 2 points, from two rule ambiguities rather than random drift.
