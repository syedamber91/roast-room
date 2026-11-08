# PIIND management seat: what BIOCON has, what PIIND has, what is missing

Status: plan only, 2026-11-09. Nothing built. Written from file names, counts and headers. No PIIND document was read by Claude (hard rule: Nemotron reads documents).

## 1. The BIOCON seat, in one line each

Brain folder `.claude/skills/roast-room/brains/biocon-management/` (27 files, ~5,000 lines), agent `.claude/agents/council-biocon.md`, data pack `docs/company-record/biocon/datapack.json` (18 lines D01 to D12 plus sub-lines), checked by `build_data_pack.py`.

| Part | BIOCON file | Built how |
|---|---|---|
| Hot sheet, as-of dates, scorecard | `_hot.md` | code index plus curated lens |
| Source index | `sources.md`, `books.md` (S001 to S038) | code |
| Filed quarters, price, AR tables | `numbers.md` | readers, sum checks |
| Segments | `segments.md` | XBRL + results PDF readers |
| Shareholding, pledge | `shareholding.md`, `promoter-declarations.md` | NSE XBRL; scans by eye |
| Votes, notices, RPT, covenants | `votes.md`, `limits-and-rpt-notice.md`, `rpt-approvals-notices.md`, `debt-covenants.md` | readers + by hand |
| Annual report prose, 5 years | `statements-ar-fy22.md` to `fy26.md` | model copies, code checks quotes |
| What management said, by topic | `positions.md` | model from call text |
| Promises vs outcomes | `record.md` (39 scored) | model + code |
| Analyst questions and answer states | `qa-states.md` (14 calls) | model labels, second model samples |
| Frameworks, stories, principles, voice | 4 curated files | model from sources |
| Changes since refresh | `changes.md` | code |

## 2. PIIND today (all in soic-ladder, not in rr)

| Have | Where | State |
|---|---|---|
| 8 call transcripts, Nov 2024 to Aug 2026 | `docs/idea/case-study/PIIND/data/calls/` | 3 thin (speaker labels); reader fix on branch `piind-roster-intro`, not committed, not merged |
| 8 decks | `.../data/decks/`, `decks-layout/` | text only, not turned into seat rows |
| FY26 and FY25 annual report pages | `.../annual-report/FY26`, `FY25` | FY26 tables: 4,819 claims, verdict ADOPT (30 of 30 blind, 6 of 6 planted caught). No prose statements built. FY22 to FY24 not fetched |
| 50 data-point answers | `.../record/t6-ask-2026-08-30.md` | 48 answered; borrowings and finance cost conflict with Screener (flagged) |
| Document link lists | `.../record/` | links only |

## 3. Gap list (BIOCON item number from `company-seat-onboarding-checklist.md`)

| # | Needed | PIIND | Who does it |
|---|---|---|---|
| 1 | Calls, management turns only | have, 3 need reader fix merged | code (VPS) |
| 2 | Analyst Q&A states | missing | code pairs, Nemotron labels, second Nemotron samples |
| 3 | Decks as rows | text only | code + Nemotron |
| 4 | Quarterly results, price | missing | readers (NSE, cloud) |
| 5 | AR tables | FY26 done, FY25 pages only | code |
| 6 | AR prose, 5 years | missing; FY22 to FY24 not fetched | fetch, then Nemotron per page, code checks quotes |
| 7 | Shareholding pattern | missing | `case_study_shareholding.py --symbol PIIND` |
| 8 | Promoter declarations | missing | by eye (hand) |
| 9 | Segments | missing (PIIND has Agchem, Pharma/CSM, Plant Health: layouts differ) | readers + new tests |
| 10 | Votes | missing | `case_study_votes.py` |
| 11 | Notices, RPT, limits | missing | hand search |
| 12 | Covenants, maturities | missing | by hand from AR notes |
| 13 | RPT amounts | in FY26 tables, not extracted | code |
| Seat | positions, record (scorecard), frameworks, stories, principles, voice | missing | Nemotron drafts, code checks quotes |
| Seat | `_hot.md`, `sources.md`, `books.md`, `changes.md` | missing | code |
| Seat | agent file, roster entry, `seats.md` line, `datapack.json` | missing | copy template, fill counts |

## 4. Things to know first

1. **Rule clash.** Hard rule says Nemotron reads every document. Items 6, 8, 11, 12 and the curated files were done by Sonnet/Opus and by hand for BIOCON. For PIIND they need Nemotron, or you lift the rule for those steps.
2. **Where it runs.** Readers and data live in soic-ladder. NSE reads work from a cloud session. Nemotron runs only on the VPS (the only place with the key).
3. **Seat is not a verdict.** BIOCON's seat is a record holder with no view on shares. Same for PIIND. The lite courtroom stays a scorecard; the seat adds `what was said`.
4. **Bars first.** Per the 2026-11-08 brainstorm: success bars fixed before any run (100% quotes verbatim in a management turn; blind Sonnet check of 40 rows at 90% or better).
5. **Unknowns.** Whether FY22 to FY24 PIIND reports are fetchable (not checked). Whether PIIND segment layout reads with the existing reader (not checked). Cost not tracked for BIOCON, so no estimate.

## 5. Suggested order (small, checkable steps)

1. Merge the speaker fix; count management turns on all 8 calls.
2. Cloud-side readers: results, price, shareholding, votes (no model).
3. Sources, numbers, datapack skeleton with honest `partial` marks.
4. Nemotron: Q&A states and call positions, bars set before the run.
5. AR prose FY26 only first; then FY25, then fetch FY22 to FY24.
6. Curated files, agent file, roster entry last, after the data exists.

A seat built through step 3 is already usable as `partial` (the Chair says "brief incomplete").

## 6. Progress, 2026-11-09

- Speaker fix merged: soic-ladder PR 1384 (calls: Q2 FY25 0 to 37 management turns, Q3 FY25 4 to 46, Q3 FY26 11 to 41, Q4 FY26 42 to 52).
- Shareholding (item 7): `case_study_shareholding.py --symbol PIIND` works unchanged. 21 filings, 2021-09-30 to 2026-09-30, promoter 46.09% since Sep 2022 (46.74% before), pledge false in all. Matches the 46.09% in the data-point answers. File: soic-ladder `docs/idea/case-study/PIIND/record/shareholding-pattern-2026-11-09.csv`, branch `piind-seat-data`, not merged.
- Segments (item 9): `case_study_segments.py --symbol PIIND` works for 8 quarters, 2023-06-30 to 2024-12-31 (XBRL). Sums tie to filing totals. Trap: PIIND prints "Other Income" as a segment row (not a business segment; must not count as revenue). Segment names seen: Agro Chemicals, Pharma, one more in some quarters (not checked). Later quarters need the results-PDF reader (`case_study_segments_pdf.py`, needs an announcements list), not run yet. File: `segments-quarterly-xbrl-2026-11-09.csv`.
- Not yet: results and price (item 4), votes (10), notices, promoter declarations, covenants, AR FY22 to FY24 fetch, all Nemotron steps.
- Segments PDF reader extended for PIIND's layout (heading on two lines, serial numbers, ordinal dates, scan marks): 8 results filings, Mar 2025 to Sep 2026. Revenue adds up in 6 of 8; the rest are scans, marked, not repaired. `segments-quarterly-pdf-2026-11-09.csv`.
- Results (item 4): new `scripts/case_study_results.py`. XBRL: 10 quarters, Sep 2022 to Dec 2024, income, expenses, profit and tax all tie. PDF: 7 quarters (Mar 2025 to Sep 2026), 5 with lines read (Mar 2025, Jun 2025, Dec 2025, Jun 2026, Sep 2026; several lines inside them are blank because the scan broke them), 2 not read (Sep 2025, Mar 2026: scan damage), Mar 2026 is available from the Jun 2026 filing's preceding column. Traps found: (a) the "profit attributable to owners" tag in Jun, Sep and Dec 2024 filings does not match profit for the period (flagged, kept); (b) from FY26 the share of associates sits before profit before tax; (c) scan text like "3,21 8" shifts columns: any line with the wrong number of cells is skipped; (d) Jun 2026 and Sep 2026 revenue are 17,023 and 17,018, so the Screener "1,702 both" oddity is Screener rounding. Files `results-quarterly-xbrl-2026-11-09.csv`, `results-quarterly-pdf-2026-11-09.csv`, soic-ladder branch `piind-seat-data`.
- Still no price reader (needs frozen weekly bars on the VPS).
