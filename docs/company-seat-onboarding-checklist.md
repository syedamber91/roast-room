# Onboarding a new company management seat: every document to read, and how

Started 2026-10-30 from the BIOCON seat. **Keep this file current: whenever a new document type is read for any company, add a row here in the same commit, with where it came from, how it was read, its source id, its data pack line and the trap it taught.** The structure the documents fill is in `docs/company-seat-spec.md`; the Chair's gate that reads the result is `build_data_pack.py` with the company's `docs/company-record/<company>/datapack.json`.

How to use it: for a new company, go down section 1 in order. Each document gets (a) one source id in `sources.md`, (b) one generated or hand-read file in the brain, (c) a line in the company's `datapack.json` with an as-of date and a Partial note if it is incomplete, (d) a dated paragraph in `changes.md`, (e) a pointer in `_hot.md`. A document that cannot be read is written down as "not read" with the reason, never skipped.

## 1. The documents, in the order to read them

"Soic-ladder" below means the sibling repo `syedamber91/soic-ladder`, where the readers live (branch `claude/company-record` for the BIOCON work). "Cloud" means it can be done from a claude.ai/code session; "VPS" means it needs the frozen artifacts or the self-hosted runner.

| # | Document | Where it comes from | How it is read | Reader (soic-ladder) | Source id and seat file (BIOCON) | Data pack | BIOCON result |
|---|---|---|---|---|---|---|---|
| 1 | **Earnings call transcripts** (CALL) | NSE announcements, category `Transcript of Analysts/Institutional Investor Meet/Con. Call` (also `...Con. Call Updates`); frozen on the VPS | Code keeps management turns only (analysts and moderators dropped before any model reads), `pdftotext` text | `scripts/case_study_management_text.py` (VPS); held dates from `data/call-dates.csv` | S001 to S014, `books.md`, `positions.md`, `record.md` | D12 scorecard | 14 calls, 2022-11-15 to 2026-08-06 |
| 2 | **Analyst questions and how each was answered** | The same transcripts, analyst turns this time | Code pairs each question with the next management answer; a model labels the answer state (answered, partial, deflected, declined, deferred); a second model re-reads a sample | `scripts/case_study_qa_pairs.py`, `case_study_qa_states.py` (VPS job `qa-pairs`) | `qa-states.md` (sources S001 to S014) | D11 | 306 of 659 question items not fully answered; second-model agreement 23 of 30 against a bar of 24, so the states are one model's reading |
| 3 | **Investor presentations** (DECK) | NSE category `Investor Presentation`; frozen on the VPS | Text per slide; segment and margin lines as management's own measures, never as filed numbers | the deck lane in soic-ladder (`docs/idea/deck-lane/`) | S015 to S025, `numbers.md` | D03 | 11 decks |
| 4 | **Quarterly results** (RES) and price | The company's quarterly results filings (consolidated), each row naming the filing it was read from; the price section of `numbers.md` names its own source | Read from the filings; the file is a dated snapshot of the record, nothing live | readers in soic-ladder `scripts/`; see the `numbers.md` header and Source lines | `numbers.md` "Filed quarters", "Segments", "Price" | D01, D02, D03 | 11 filed quarters to 2026-06-30; last weekly close in the week to 2026-10-23; the segment note's third segment is named Research services, then CRDMO, then Services |
| 5 | **Annual report, tables** (AR) | BSE/NSE annual report PDF (the link is in the results announcement or the AGM intimation) | `pymupdf4llm` markdown, one file per PDF page, plus `pdftotext`; no OCR. Figures checked by a second reader or by the table's own sums | `scripts/case_study_annual_report_pages.py` | S026, `numbers.md` "Annual report" | D04 | FY2025-26 tables |
| 6 | **Annual report, prose statements** | The same report, five years | A model copies verbatim statements per page packet; code checks each quote is on the page in two text readers (High) or one (Medium), the type fits the section of the report, planted wrong statements are all rejected, a foreign company's sentences all fail; blind grader samples | `src/soic_ladder/annual_report_prose.py`, `scripts/annual_report_prose*.py`; bars and prompts in `docs/idea/case-study/BIOCON/annual-report-prose/` | S027 to S031, `statements-ar-fy22.md` to `fy26.md` | D05, D06, D07, D08, D09 | FY26 record missed its own bars (P1 and P2 both REJECT) and was accepted by the owner as a record; FY22 to FY25 graded 26, 29, 30, 30 of 30 |
| 7 | **Shareholding pattern** (SHP) | NSE `api/corporate-share-holdings-master?index=equities&symbol=<SYMBOL>` lists every pattern with an XBRL link | Tags read from each XBRL: promoter shares, percentages, pledge, non-disposal and other encumbrance flags | `scripts/case_study_shareholding.py --symbol` (cloud) | S032, `shareholding.md` via `build_shareholding_file.py` | D05a | 25 filings, 2021-09-30 to 2026-09-30; pledge flag false in all |
| 8 | **Promoter annual declarations** (Regulation 31(4)) | NSE announcements, category `Disclosure under SEBI Takeover Regulations`, once a year in April | Scanned letters: render with `pdftoppm` and read by eye | none (by hand) | S037, `promoter-declarations.md` | D05b | FY23 to FY26 say no encumbrance; FY22 is only a list of six declarants |
| 9 | **Segment tables** (SEG) | NSE `api/corporates-financial-results?index=equities&symbol=<SYMBOL>&period=Quarterly` (XBRL up to the quarter NSE's list reaches) and the results PDF for later quarters (announcement categories `Financial Result Updates` and `Outcome of Board Meeting`) | XBRL tags by context name; PDF table by `pdftotext -layout`; every table checked that segments add to its own total | `scripts/case_study_segments.py`, `case_study_segments_pdf.py` (cloud); `build_segments_file.py` | S033, `segments.md` | D10 | 10 quarters from XBRL (to 2024-12-31), 6 results PDFs (2025-03 to 2026-06); 2025-09-30 has no clean source |
| 10 | **Voting results** (VOTE) | NSE announcements, category `Shareholders meeting`, the voting-results or scrutiniser annex of each AGM, EGM and postal ballot | `pdftotext -layout`; three annex layouts exist; categories must add to the printed total | `scripts/case_study_votes.py` (cloud); `build_votes_file.py` | S034, `votes.md` | D06a | 83 resolutions at 9 meetings, 2024-04-23 to 2026-08-06; 0 failed checks |
| 11 | **General meeting and postal ballot notices** (NOT) | The same category: the notice is in the intimation file (an AGM notice file is the whole annual report plus the notice, about 30,000 lines) | By hand: search for `Value of the transaction`, `Tenure`, `not exceeding`; read the explanatory statement for related party, limits and borrowing items | none (by hand) | S035, S036, `limits-and-rpt-notice.md`, `rpt-approvals-notices.md` | D06b, D06c | EGM 2025-12 plus five earlier notices; ceilings, parties, validity |
| 12 | **Debt covenants, maturities, facilities** | The annual report's borrowings note and the liquidity risk note | By hand, from the page files, with PDF page numbers | none (by hand) | S038, `debt-covenants.md` | D09a | Three covenant ratios (company), six (group), no thresholds, no undrawn lines stated |
| 13 | **Related party transactions: amounts** | The annual report's related party notes (standalone and consolidated) | Table pages from item 5 | as item 5 | S026, S027 | D06 | Notes 32 and 33; no separate half-yearly filing after 2023-11-10 in the feed |

## 2. Documents not yet read for BIOCON (read these for the next company if the council will lean on them)

| Document | Why it matters | Where | Note |
|---|---|---|---|
| Credit rating rationale | Debt and funding (S4): the agency's view, outlook and triggers | NSE category `Credit Rating` | In the feed (17 entries 2022 to 2026); not read |
| Reg 30 event announcements (acquisitions, litigation, resignations, appointments, auditor changes, fraud or default) | Board, auditors and events after the year end (S7) | NSE categories `Acquisition`, `Resignation`, `Change in Auditors`, `Appointment`, `Change in Director(s)`; 892 announcements in 2022 to 2026 for BIOCON | Headlines are in the feed; the PDFs are not read |
| Insider trading and takeover disclosures (Regulation 29, SEBI PIT) | Promoter selling and large holders | NSE category `Disclosure under SEBI Takeover Regulations` | Only the Regulation 31(4) letters are read |
| Business responsibility report (BRSR) and the corporate governance report | Board attendance, remuneration, whistle-blower | Inside the annual report | Partly covered by item 6 |
| Auditor's report and key audit matters | Earnings quality (S2) | Inside the annual report | Covered by item 6 (D07), words are the auditor's |
| Bulk and block deals, delivery data | Float and positioning | NSE | Not frozen anywhere in this project; stated as a gap in soic-ladder |
| Peer set and sector context | Comparison for S2 and S5 | soic-ladder peer sets | Not part of a management seat; the Chair brings it |

## 3. Rules that hold for every document

1. **Read the primary source, not a summary of it.** A summary or a headline in the feed is a pointer.
2. **Every number comes from a file, and every file is pinned** (sha256 in the list or the CSV; the CSV's sha256 is printed into the brain file). A derived figure is computed by code and labelled "derived".
3. **Hand-read files carry no tier and say so.** A scan read by eye, or a notice read by hand, is written as such in its first paragraph, with what was and was not read. No quote is taken from a filing that is not speech.
4. **Every table gets a sum check.** Segments add to the total; voting categories add to the printed total; maturity buckets add to the total. A table that fails is kept and marked, never repaired. A text layer that has lost brackets or digits is not used for a number.
5. **Mark what is not read, in the same file.** "Not read" lists beat silence. Each such list names the document and the reason.
6. **The data pack carries the limit.** Every line has an `as_of` and a `max_age_days`; any limit goes in its `partial` note, so the Chair says "brief incomplete" with the reason.

## 4. Traps found on the way (each cost real time)

- **NSE access.** The archive host `nsearchives.nseindia.com` and the API both work from a cloud session, but the API needs a Chrome-like User-Agent and a Referer of `https://www.nseindia.com/`, and the archive downloads need `curl --http1.1` (HTTP/2 fails with a stream error). The homepage returns 403 even when the API answers.
- **Label trap.** NSE category labels change: the related party category stops in the feed after 2023-11-10, and half-yearly related party filings afterwards are not a separate item. Count a label in the company's own feed, in window, before relying on it.
- **XBRL year-to-date columns carry the quarter's dates.** In the results XBRL the `Four...` (year to date) contexts have the same start and end as the quarter, so a date filter reads nine-month figures as the quarter's. Select the quarter by the context name and check it against the next filing's year-to-date figures.
- **XBRL schemas differ by year.** The shareholding XBRL has two schemas (contexts and tag names differ), and the percentage tag is a fraction in some years and a percent in others; an implied total share count came out 100 times too small until normalised.
- **Definitions change.** Segments were renamed, merged and restated across filings (Novel Biologics and Research Services became Services, printed as CRDMO in between), and the result measure changed (before tax and finance costs, then profit before tax). Every row names the filing it is printed in; never compare across filings without reading the definition note.
- **Scans.** A results PDF can be a scan with a corrupted text layer (lost opening brackets turn a loss into a profit). A lost bracket makes the line unreadable. Use another filing's comparative column for that quarter instead of repairing it.
- **Unicode hyphens.** A date written `09‐08‐2024` with a Unicode hyphen failed a plain pattern and the filing date was used as the meeting date until fixed.
- **Three voting annex layouts.** One has category totals with Indian digit grouping; one has category totals without the shares held; one has one row per voting mode and no totals, with the category label on the third row. Detect the layout from the numbers (votes for plus against equal votes polled), not from fixed positions.
- **A promoter group interested in a resolution does not vote on it.** Votes polled by the promoter read 0, so the percentage against is the public's alone.
- **Notices.** An AGM notice file on NSE is the whole annual report plus the notice. Search it, never read it end to end. Filenames are copied exactly from the feed; a mistyped one returns not-found.
- **VPS limits.** A dated results folder can be newer and smaller than an older one; check counts before reading the newest. Heavy jobs take the host lock and refuse to start when the host is busy.
- **Tests.** Make a test for each reader on a real excerpt of the real document, including the case that bit (the Four column, the lost bracket, the Unicode hyphen). Do not commit with a failing test.

## 5. What to do when a company has no transcripts, or a different layout

- No call transcripts (a company that does not hold calls): the seat is built from items 4 to 13 and the Q&A rows read "no calls"; the gate says so.
- A company with no segments (one segment): item 9 reads the single total and says so.
- A lender: the sections S3 and S4 change (asset quality; funding), and the segment reader's `Sales` assumptions do not hold; see the section map in `references/stock-rating.md`.
- A different XBRL schema or a different results PDF layout: write the test for the new layout first, then extend the reader. A table that cannot be read is listed as not read.

## 6. Cannot say yet

- Whether items 7 to 10 behave the same on the VPS runner as from a cloud session (they were run from the cloud session; no VPS job exists for them).
- How long a full onboarding takes: the BIOCON seat was built across several sessions and the cost was not tracked per document. Track it for the second company.
