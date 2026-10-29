# Company seat spec: the structure the extractor must fill

Status: design, 2026-10-29. Nothing here is built. The BIOCON seat (`.claude/skills/roast-room/brains/biocon-management/`, agent `council-biocon`) is the template: the owner likes its structure, so the extractor is built to fill that structure, not a new one. Machine record and field list: soic-ladder branch `claude/company-record` (`docs/idea/case-study/record/FIELDS.yaml`, `docs/superpowers/specs/2026-10-29-company-record-design.md`).

## 1. The structure to keep

| File | What it holds today (BIOCON) | Kind |
|---|---|---|
| `_hot.md` | as-of line, five dated numbers, annual report headline numbers, scorecard, lens, where it misfires | generated index plus curated lens |
| `sources.md`, `books.md` | 26 sources (14 calls, 11 decks, 1 annual report), one id each, dated | generated |
| `numbers.md` | 11 filed quarters, segment revenue, annual report tables, price | generated from the record |
| `positions.md` | dated management statements by topic, older and newer wording side by side, "what was filed" notes | statements, topic by topic |
| `record.md` | 39 scored statements: Kept 14, Missed 5, Still open 9, Depends on reading 11 | scorecard against outcomes |
| `frameworks.md` | 16 ways management reasons (core EBITDA, margin guide ladder, capex phase gate) | curated, evidence-led |
| `stories.md` | episodes by date (Viatris, Eris, Bicara, the launch wave) | curated |
| `principles.md`, `voice.md` | rules of thumb; how management talks; speaker roster | curated |
| `changes.md` | what moved since the last refresh | generated at each refresh |

## 2. Where today's gaps fall in that structure

| Seat file | Missing today | Fields (FIELDS.yaml) | Source document |
|---|---|---|---|
| `numbers.md` Filed quarters | other income with one-off tag, exceptional items, profit to minority holders (the VPS truth table has them; the seat holds profit for the period and to shareholders but not these) | F03, F04, F08 | RES, AR |
| `numbers.md` Segments | segment result (profit) by quarter; only revenue held | F21 | RES, AR |
| `numbers.md` Annual report | receivables, financing flows, equity, EBITDA, undrawn lines, contingent liabilities, related party amounts, key pay, dividends | F13, F14, F19, F20, F24, F25, F30, F31 | AR |
| `numbers.md` new table "Ownership by quarter" | promoter holding, pledge, institutions | F27 to F29 | FIL, AR |
| `numbers.md` new table "Shares and EPS" | share count, EPS, dilution (valuation inputs) | F26 | AR, RES |
| `positions.md` existing topics | annual report prose on debt, capex, R&D, outlook; management's explanation of one-offs | T01 to T04 | AR, CALL, DECK |
| `positions.md` NEW topics | Promoter, pledge and succession; Board and committees; Auditor and controls; Related parties; Litigation, regulators and tax orders; Accounting changes and restatements; Risks the company names; Events after the year end | T05 to T15 | AR, FIL |
| `record.md` NEW section | "Questions asked on the calls and how they were answered": each analyst question with a state (answered, partial, deflected, declined, deferred); the call texts today keep management turns only | T16 | CALL |
| `record.md` | guidance slips and moved ranges counted once, in one place | T18 | CALL, DECK |
| `frameworks.md` | management's own measure definitions tied to a filing line (core EBITDA, like-for-like) | T17 | DECK, RES |
| `sources.md`, `books.md` | annual reports FY22 to FY26 (prose and tables), full call transcripts, periodic filings | new source ids | all |
| `_hot.md` | a coverage line and a "figures the brief may need" index | generated | the record |

The seat already has a place for what it cannot answer: positions.md "Subjects with no recorded position" and "What management says it will and will not disclose". An unresolved required field is written there with its reason, so a gap is always visible.

## 3. The builder: prerequisites first, then the seat

Order for a new company seat, and for each refresh of an existing one. The first four steps are the prerequisites; the seat is not generated before they finish.

1. **Intake.** Company, exchange code, as-of date, document classes (AR annual report, RES quarterly results, DECK investor presentation, CALL full transcripts, FIL periodic exchange filings).
2. **Inventory and fetch (VPS, no model).** List what the VPS holds; fetch what is missing for this company only; pin each file by sha256.
3. **Extract (Sonnet) and verify (code).** Every field of FIELDS.yaml ends found, not_stated, not_applicable or unreadable. Quotes and numbers are checked against the frozen text; sums tie.
4. **Review (Opus).** Re-search every not_stated, audit unvisited sections, judge the fuzzy calls, re-extract a 20% sample. Disagreements stay `contested`.
5. **Coverage gate.** The seat is created as `ready` (all required fields resolved), `partial` (gaps listed in `_hot.md` and `Subjects with no recorded position`; the Chair says "brief incomplete" before any stock rating) or `blocked`.
6. **Write the brain.** Generated files (sources, books, numbers, changes, the `_hot.md` index) come from the record. Statement files (positions, record) are written by Sonnet from the statement rows, with Opus review, then `check_quotes` verifies every quote is verbatim.
7. **Agent and roster.** The agent file from the BIOCON template (company name, as-of dates, counts), a roster entry, the line in `seats.md`.
8. **Refresh.** After each quarterly result: repeat 2 to 4 on the new documents only, regenerate the generated files, append the dated paragraph to `changes.md`, re-score open items in `record.md`.

## 4. Generated against curated text

Generated blocks sit between `<!-- generated:record START -->` and `<!-- generated:record END -->` markers and are rewritten at each refresh. Everything outside a marker is curated (frameworks, stories, principles, voice, the lens in `_hot.md`) and is never overwritten. Each generated row carries its row id from the record so a seat can cite it.

## 5. At council time

- The seat reads `_hot.md` first (it now carries the coverage line and the file index), then at most three files. The routing the agent file should add: S1 guidance and promises, `record.md`; S2 earnings quality, `numbers.md` Filed quarters plus `positions.md` One-offs; S3 and S4, `numbers.md` Annual report plus `positions.md` Debt; S5, `positions.md` Related parties; S6, `numbers.md` Ownership plus `positions.md` Promoter; S7, `positions.md` Auditor and Board.
- The Chair runs `build_data_pack` before the council and writes the data pack into `brief.md`, with derived figures computed by code and stale rows marked.
- Seats read files only. No live fetch. Refresh is a VPS job before the run.

## 6. Rules that stay, and one decision for the owner

Stay as written in `council-biocon.md`: the seat is not Biocon or an executive; no view on buying, selling, holding or valuing shares; every number carries its as-of date and basis; a figure from the annual report tables is a filed number, never a quote.
**Owner decision, yes on 2026-10-29:** annual report prose by the chairperson or managing director (letter, management discussion) is management speech and may be quoted with its source id and page; the auditor's report is the auditor's words, quoted as such; the governance report is the company's filing. The agent file `council-biocon.md` is changed only when the first prose statements are verified and synced, not before, so the seat never cites a source it does not hold.

## 7. Cannot say yet

Whether prose extraction reaches table-level accuracy, whether the NSE shareholding, governance and related party endpoints are reachable from the VPS, and how the same builder behaves on a company with no earnings call transcripts. The spec's pilot is BIOCON only.
