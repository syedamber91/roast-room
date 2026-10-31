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
