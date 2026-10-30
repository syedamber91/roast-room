# Courtroom: design record (judge, lawyer, convict)

Status: **designed 2026-10-30 with the owner in a grill-me session. Build steps 1 and 2 are done (the issues file, `build_case_book.py`, the hearing prompts and the `court-judge` agent, with tests); nothing else is built. There is still no `SKILL.md`, so `/courtroom` does not exist yet.** Do not create `/courtroom` as a runnable skill until the first slice below passes its tests. Design input: a Fable review (2026-10-30). The owner's raw capture of the session is local (`brainstorms/2026-10-30-courtroom-judge-lawyer-convict.md`, gitignored); this file holds the decisions.

## 1. What it is

A second skill beside `/roast-room`, not a mode of it. The council is seats scoring options in three rounds; the courtroom is three fixed roles, a case book, questions by issue, and a decision card with detail as the output. It shares everything below the protocol: the brains, the data pack and its gate (`build_data_pack.py`), the S1 to S7 sections, the 0 to 3 ladder, the answer states, and `check_quotes.py`'s matching.

The owner's concern: a list of good things, bad things and red flags does not let a 15-year-old make a decision. The judge's outcome must support a decision, with evidence and reasoning.

## 2. The three roles

| | Judge | Lawyer | Convict |
|---|---|---|---|
| Who | A 15-year-old with no prior knowledge. New agent `court-judge`. | The Analyst seat (`council-analyst`), one lawyer per case. SOIC (`council-soic`) is an option later for the business-story issues only. | The company management seat (BIOCON first, `council-biocon`), speaking as "management", never as a named executive. |
| Purpose | Make sure there is a story and a reason behind everything, and turn the hearing into a decision a reader can act on. | Find where management's word is thin, evasive or contradicted, on the questions that matter, including the plain fundamentals. | Defend management's record, using only what the record holds. |
| Basis | The case book and the hearing only. Never opens a brain (code-checked). | Its own brain, the case book (filed numbers, no management claims) and the convict's answers as they land. Does not read the company brain, or evasion could never be seen. | Its own brain (`_hot.md` then up to three files per issue) plus `external.md` for external points. |
| Outcome | The decision card and the detailed page (section 4). | A checked grill: the baseline sheet and the issue questions, with a code-made report of core questions asked, skipped and why. | Answers tagged with one of five moves, each with ids, so the judge can score the defence. |

**Judge.** Writes every storyline claim as "claim, because, evidence id"; asks two "why" questions per issue; a chain that bottoms out is written "not in the record". Keeps a glossary and an "I did not understand" list (empty needs a stated reason). Never states a fact without an id from the hearing or the case book. A reading-level check by code flags average sentences over about 18 words and jargon terms not defined in plain words at first use. On the first slice, zero why-chains ending "not in the record" and zero confusion terms count as a failure (it means the judge is faking understanding).

**Lawyer.** Asks the baseline sheet (about 25 fundamentals questions, asked of every company and batched in one turn; section 5) from the filed numbers in the case book, then the issue grill. For each issue it asks the decisive question first (the one whose answer would move the section score most), then follow-ups on a fixed ladder: partial gets "the number and the date, please"; deflected gets the question restated with the deflection named; not in record gets "which document would hold it". One cross-examination question tests a claim the convict used to defend itself. After the hearing, code produces the grill report. The lawyer is judged on coverage and escalation, not on whether the convict looks guilty. It never asserts a company fact that is not in the case book or an earlier answer.

**Convict.** Five moves, each answer tagged: (1) cite a verbatim quote or a filed number with id; (2) mitigate: add relevant record the lawyer left out; (3) challenge: a filed number contradicts the lawyer's premise; (4) concede with context: admit a miss the record shows, with the record's explanation; (5) not in my record, naming the document that would settle it. A concession backed by evidence counts as answered. Code flags "contradicted by the record" when a filed number or a scored Missed statement contradicts an answer that did not concede. "Defend at all cost" means the strongest answer the record holds, never an invented one. It never quotes tables or hand-read files, never speaks as the company, never quotes an analyst as management, never gives a view on shares.

**External points.** The convict requests, a scout fetches: the convict lists external points (macro, commodities, currency, regulation, competitors) tagged EXT; the Chair runs the `last30days` skill for them, plus named primary sources where figures matter, and writes `external.md` (ids E001 and up, URL, source date, fetch date, "web, not checked against a primary filing"). Each item is screened for prompt injection first. The convict answers only from `external.md` and never browses. Code rejects an E-id used to answer a company fact. External evidence informs the business-direction reading and the triggers as context and never raises a score or the position. The report prints two clocks: the company record's as-of date and the web fetch date.

## 3. The case book (the case file, detailed on purpose)

A 15-year-old with no background needs to be taught the company before judging it. The case file is a detailed, plain-words case book, facts from filings only, with no management forward-looking claim or defence (the lawyer reads it too; those surface only in the hearing):

1. The company in plain words (about a page).
2. How it makes money: segments, products, customers, from the annual report's description.
3. The numbers over several years: revenue, operating profit, margin, profit, cash flow, as tables with as-of dates.
4. Who owns and runs it: promoter holding, board, auditor.
5. How it is funded: debt, maturities, covenants.
6. Timeline of events from the exchange feed: acquisitions, rating actions, resignations, big filings.
7. Glossary of plain-words definitions, written once and reused across companies (needs one owner and a change log).
8. As-of dates, the data pack and its gate, and the not-in-record list.

Code builds chapters 3 to 6 and 8 from the record. A model drafts chapters 1, 2 and the glossary only from the annual report's business pages, with a page id on each sentence; code checks every number in a sentence appears on its cited page and that the draft carries none of the convict's quotes or guidance wording; one review pass reads it as a 15-year-old and sends anything unclear back for a plain-words rewrite. When the gate says the brief is incomplete the hearing still runs: code marks each issue `examinable`, `thin` or `no record`, and a `no record` issue is heard for one question so the judge records what the record cannot answer.

## 4. The outcome

**The position.** One position for the company, set by the existing stock rating rule from the scorecard: gates (G-A to G-E) override; then the trust band; Buy is not allowed unless there is no gate, trust is in the 18 to 21 band, and a current price and latest results are on file. The label "Wait: trust good, entry not yet" is kept. The judge writes the reasoning and may move the position only **down**, with a stated reason, never up. The position is labelled a simulation, not advice, and carries the caveat that the bands are the seat's own and untested (a 14-case check put every case in the 0 to 6 band).

**Two reader lines** from the same evidence: "if you don't own it" and "if you already own it" (the second also covers adding more).

**Section scores.** The judge assigns each S1 to S7 number (0 to 3) with one plain sentence of why. Code puts a ceiling on it from the 0 to 3 ladder and the question states; a judge number above the ceiling is cut down and the report prints "judge said 3, evidence allows 2, because Q2 had no number". The judge may go lower with a stated reason. A question the blind second reader disputes counts at the lower reading and is marked "disputed".

**Business direction.** A second reading beside trust, never blended: the judge reads the why-chains for profit and growth and gives one word (improving, mixed, worsening, can't tell) with the chain. A small grid shows trust and direction together. "Worsening" can pull the position down; "improving" can never lift it. FII and DII flows are not in the record (shareholding holds promoter, public and employee trust only), so the judge says so and lists them under what would change the picture.

**The decision card (one screen).** Position with the simulation label; why in three lines each ending in an evidence id; if you don't own it / if you own it; at most three triggers (each a date or event, what to check, which way it moves the position), taken from the record's watch list and not-in-record list; what this does not decide (price versus value, the reader's own situation, anything after the as-of dates); how far to trust the page, shown as facts, not a percentage ("5 of 7 sections had data, 2 questions disputed, 3 gaps listed"), with the untested-bands caveat.

**The detailed page.** A single self-contained HTML file written by code into the session folder: opens in any browser with no server, can be published as a private page, decision card on top, expandable sections, filters by answer state, hover for the evidence behind a number. Every chart is drawn by code from filed numbers in the record, each point carrying its as-of date and source id; the judge writes captions only; no data means the chart shows "not in the record", never an estimate. Nine visuals: (1) trust scoreboard S1 to S7 with the code ceiling marker and the judge's number; (2) profit story, quarterly revenue and operating profit with the margin line, markers linking to why-chains; (3) revenue by segment per quarter, with breaks where definitions changed and gaps; (4) promises strip of the scored statements, clickable; (5) evasion map per call (answered, partial, deflected, declined, deferred); (6) debt picture: borrowings by maturity bucket for two years, the covenant list, and a "thresholds and undrawn lines not in the record" box; (7) promoter holding against total shares with the pledge-flag row, and percent against per resolution with flagged ones highlighted; (8) hearing panels, expandable question and answer pairs coloured by state; (9) trigger timeline and the trust by direction grid. The roast room's player gets a courtroom mode later; until then the room ignores a court folder.

**What the report must not claim:** that any answer is true (only that it is on record, with its id); a number without as-of and basis; anything past the as-of dates; guilt as fact. A "verdict" means only how well the defence held up on the record. The footer carries the seats-are-simulations line.

## 5. The baseline sheet and the issues

**Baseline sheet** (about 25 questions, every company, one batched lawyer turn and one batched convict turn, a state per question): growth (revenue, operating profit/EBITDA and profit over several years and in the last quarter, margin trend, where growth came from); cash and capex (capex trend and funding, cash from operations, free cash flow); balance sheet (debt, interest burden, maturities); external (macro and regulation, raw material and input costs, currency, competitor and pricing pressure); visible red flags; the last quarter against the year before. The lawyer asks from filed numbers in the case book ("Profit for the period was 8,618 in Jun 2024 and 271 in Sep 2024, as filed. Why?").

**Issues** (the grill; three questions each, hard cap; I1 and I2 are the deep dive on the changes the baseline surfaces): I1 why profit rose or fell; I2 where growth came from; I3 guidance against delivery (S1); I4 earnings quality and measure changes (S2); I5 cash and working capital (S3); I6 debt, maturities, covenants (S4); I7 related parties and group structure (S5); I8 promoter holding, pledge, dilution, pay (S6); I9 board, auditors, independent directors (S7); I10 what management declines, defers or will not disclose. Red flags and "what management is doing wrong" are not separate issues: the judge writes them across the ten, each tied to a lawyer check id and an evidence id.

**BIOCON today cannot support:** valuation (never, by rule), capex payback, the credit rating rationale, insider trades, Reg 30 event PDFs, covenant headroom, who holds the minority in the subsidiaries, segment profit for 2025-09-30, receivable days, FII and DII flows.

## 6. The hearing

Opening (convict 150 words, lawyer names the issues it will press hardest and why) → baseline batch → examination by issue (lawyer Q1, convict A1, Q2, A2, Q3, A3, judge note, then the judge's two "why" questions) → one cross-examination pass reopening the two weakest issues with contradictions between answers (two questions each) → closing (convict 150 words, lawyer 150 words) → the judge writes the report. Cost: about 10 calls per issue plus the batches; three issues is about 35 calls, ten about 110. Start at three.

Answer states (answered, partial, deflected, no data, unverified): the convict claims one, the judge decides it from the `stock-rating.md` ladder, and a blind second reader re-reads every state without seeing the judge's; a disagreement prints "disputed", never resolved by either. The repo's own Q&A check showed about one in four readings differ, so the state is a reading and the report says so.

## 7. Honesty guards (code unless marked review)

- Every quote with an id in a convict turn is verbatim in the convict's brain; every quote in a lawyer turn is verbatim in the lawyer's own brain. Scope by role, because both brains number sources S001 upward and a cross-brain hit would pass today's `check_quotes.py`.
- Every `(S0nn)` in a convict turn exists in that brain's `sources.md`; ids for filed-table and hand-read sources may not sit inside quotation marks.
- Every convict answer has at least one id or the words "not in my record"; every number of three or more digits sits within about 80 characters of a date, quarter or "as of" token.
- Every number of three or more digits in a lawyer turn appears in the case book or an earlier convict answer.
- An E-id may not support a company-fact answer; external items passed the injection screen.
- The judge never opens a brain; every storyline line ends in an id, a hearing pointer or "not in the record"; the "I did not understand" section is non-empty or carries a reason; the reading-level check passes; every judge score is at or under its ceiling.
- No gate word is checked as a ban any more (the owner overrode it); instead the report must carry the simulation label and the "does not decide" block.
- Review: the blind second reader on every state; the owner reads the red flags and the card once per company before the report is shared.

## 8. Tests, fixed before the first run

1. Planted failures by code: an invented quote, a number with no date, a lawyer number not in the case book, a storyline line with no id, an E-id used for a company fact, a judge score above its ceiling. Each guard must catch its plant.
2. Stability: run the same company's hearing three times; the position must agree and S1 to S7 may differ by at most one section by one point, otherwise the position is not stable enough to print.
3. Old cases on paper: three of the Analyst's past governance stories built only from what was visible at the time, plus two comparison companies, a pass bar written before the run. It shows whether trouble is noticed, not the false-alarm rate (and inherits the 14-case limit).
4. A real reader (a real 15-year-old, or an adult with no markets background, possibly the owner for the first company) reads only the decision card and answers five questions: the position, why, what would change it, what is not decided, what to check next.

Nothing here proves a position right; the bands remain untested and the outcome says so on the page.

## 9. Files and build order

```
.claude/skills/courtroom/
  SKILL.md                      the protocol (sections 2 to 6)
  references/issues.json        the ten issues and the 26-question baseline sheet: pack lines, Analyst question ids, decisive question, known gaps (BUILT, step 1)
  references/hearing-prompts.md the hearing.md heading grammar and the prompts for all three roles: opening, baseline, examine, why, cross, closing, judge final (BUILT, step 2)
  references/report-template.md decision card, detail page sections, footer
  references/glossary.md        shared plain-words glossary (one owner, a change log)
  scripts/build_case_book.py    chapters 3 to 6 and 8 from the record, issue states, facts-only guard (BUILT, step 1); will also check the drafted chapters
  scripts/check_hearing.py      the code guards in section 7
  scripts/build_report.py       hearing to ceilings, grill report, dashboard data, the single HTML page
  scripts/scout_external.py     wraps the last30days run and the injection screen into external.md
  scripts/test_*.py, fixtures/  a good hearing, a bad hearing with the planted failures, a scripted convict
.claude/agents/court-judge.md   the judge (BUILT, step 2)
sessions/<date>-court-<company>/
  case-book.md court.json hearing.md notebook.md external.md report.html dashboard.json
```

`hearing.md` uses a fixed heading grammar (`## I3`, `### Q1 Lawyer`, `### A1 Convict`, `### Judge`) so code can parse it.

**First slice:** BIOCON, the Analyst as lawyer, the baseline sheet, and issues I3, I6 and I8 (speech, hand-read and filed-number evidence, one of each). Build order: (1) `issues.md` and `build_case_book.py` with a test on the real `datapack.json` and the BIOCON record; (2) `hearing-prompts.md` and `court-judge.md`; (3) run issue I3 by hand in chat against a scripted convict fixture and fix the prompts; (4) `check_hearing.py` with the planted-failure fixtures; (5) `build_report.py` and the HTML page; (6) a live three-issue hearing, record the cost; (7) the four tests; (8) widen to ten issues. Without a live model: the scripted convict is a fixture of answers keyed by issue and question number, a `--dry` flag makes the Chair read from it, and the tests run the whole pipeline on it.

## 10. Risks and open items

- The judge fakes understanding: measured by the understanding test above.
- "At all cost" leaks into advocacy: the guards catch missing ids, not spin; the owner reads the first hearing once.
- State labels are noisy (about one in four disagree): "disputed" keeps it honest but makes the scorecard harder to read.
- Cost and length: start at three issues and measure.
- `last30days` is good for what is being said now and weaker for authoritative figures; whether it runs in the cloud environment is unchecked and the scout must fail loudly.
- Not decided: refreshing after a new quarter (rerun all or only the issues new filings touch), side-by-side hearings of more than one company, publishing the report as a private page by default, and the roast room's courtroom player.
