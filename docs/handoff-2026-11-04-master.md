# Handoff (master): BIOCON courtroom, post-hearing checks and tooling, 2026-11-04

Repos (all on GitHub under syedamber91): roast-room (branch integration/free-model-offload), soic-ladder, knowledge-toolkit, provenance, learning-vault-invest, claude-memory.
Rules in force: screen not advice (no buy/sell/hold); read primary source before asserting; count before claiming; mark unchecked; never print NVIDIA_API_KEY; no PRs unless asked; commit messages end with the attribution lines.

## What was done
1. Roast Room courtroom on BIOCON. Judge = court-judge, Convict = council-biocon, Lawyer = Analyst seat (heard I3-I9 only) and SOIC seat (all ten issues I1-I10, Opus + Sonnet, high effort). Sessions: sessions/2026-10-30-court-biocon-live-example and sessions/2026-11-01-court-biocon-soic-lawyer (gitignored, not in repo).
2. SOIC-lawyer result: S1 2, S2 0, S3 0, S4 0, S5 1, S6 2, S7 0 = trust 5 of 21 = Wait (trust bands are the seat's own, untested). Direction mixed: sales +10.9%, profit to owners 10,133 to 3,856 (Rs million), operating cash 40,612 to 19,940.
3. Outputs: SOIC report artifact https://claude.ai/artifact/N1JgtiJxJdJDqCVE3nnowD; Receipts page (Kid/Teen/Expert, 12 merged red flags) https://claude.ai/artifact/MWJ1MaL1SzJy68fWNsccjZ; one-sheet PDF stakeholder/biocon-one-sheet.pdf; 124-page two-court PDF docs/courtroom-pdf/biocon-two-courtrooms.pdf. Two stray duplicate artifacts exist (9MK5E4KTmEfhPX6JSmdJho, RkTh36KYuXfTMAA4jZgHuH): delete only on user say-so.
4. Post-hearing findings added as "Found after the hearing" (add_after_panel.py, after-hearing.json, commit 9ad6c94): guarantee 7,245 = Biocon Biosphere 5,375 + Biocon Generics Inc 1,870 (standalone note, PDF p324); subsidiary auditor resignation = Biocon Biologics, planned alignment after BSR's mandatory rotation at the parent (S.R. Batliboi appointed 5 years); 11,345 other income is printed in filed results, management says Eris proceeds Rs 1,057 crore, 775 million gap unexplained; Chairperson pay about 55.0 million (71.78 x median 765,716, derived, Biocon Ltd only); covenant ratios named, no limits, ICRA trigger 3.5x vs 2.6x at 2025-03-31; inventory +11,546 (WIP +6,527, FG +2,803) vs payables +2,234; capitalised interest 5,884/1,597 (finance cost note) vs 1,782/nil (intangibles note, inferred subset).
5. Skill stock-analyzer (from a Notion page) installed at ~/.claude/skills/stock-analyzer and committed to main of all six repos (.claude/skills/stock-analyzer/SKILL.md). Its assets/deep-dive-template.html was NOT on the page and is missing.
6. Quick Take on BIOCON from Screener (price 343, P/E 77.0, ROE 1.40%, ROCE 3.61%). Indicative Shariah ratios by hand (NOT the real screen; status NOT ASSESSED): debt/total assets 24.25% (FY25 31.23%, 35.17% with put options), interest income/revenue 0.68%, DJIMI liquidity 6.10%, AAOIFI/S&P liquidity 13.20%.

## Sources actually fetched or read (this chat)
- Committed in soic-ladder: docs/idea/case-study/BIOCON/ (DATA-LEDGER, truth table, announcements CSVs 582 rows, excerpts of consolidated results, management-text, calls, decks, decks-layout, qa-pairs, storyline, lenses) and annual-report/FY26/p001-p559.md (FY2025-26 report text, printed page = file page minus 4), claims-FY26-v6.csv, tier and decision files (v5 verdict ADOPT).
- Roast-room: case-book.md (built 2026-10-30), external.md, hearing.md (~397 KB), judge final, work/ turns and cards.
- Live fetches from the cloud container: Notion public page API (skill text); Screener BIOCON consolidated page (as of 2026-11-03 close); NSE announcements API and PDFs (2026-08-06 auditor/director letter and BBL auditor resignation letter; ICRA 2025-10-30 and 2025-12-16; CRISIL 2024-11-26); BSE annual report PDF (turned out to be 2022, discarded). Blocked or failed: Tickertape 404, Moneycontrol blocked, biocon.com SSL error, NSE API needs a cookie first.
- Not used: NotebookLM, RAG/vector search, any VPS job in this stretch.

## How the data got into the case book (from repo docs; not re-verified today)
- Transcripts: NSE announcement PDFs fetched by case_study_fetch_urls.py (fetch-calls) with pdftotext, zero model cost; 14 calls held 2022-11-15 to 2026-08-06; management turns only; speaker roles resolved by deterministic code; quote text verified byte-exact against source.
- Investor decks: fetch-decks, poppler layout text (decks-layout), 11 decks; deck figure checker "deck-probe" tiers claims High/Medium by matching to filings/Screener; only High is used (soic-ladder CLAUDE.md thread, versions up to v2.41).
- Annual report: fetch-annual-reports + annual-report-pages jobs on the VPS; reader versions v3 to v6 (annual_report_md, PyMuPDF-based, approved for the FY26 pilot only), claims with tiers, blind grader, bars; tables read, prose not read. Case book notes 3,808 unread table rows and rotated page 365.
- Quarterly results: 11 filings via fetch-results (10) + gap-urls (Mar 2025), consolidated excerpts committed.

## Tools and libraries used in this chat
curl (with browser User-Agent, through agent proxy), grep/regex, python3 (-I for downloaded files), pypdf via media_core.pdf_text (LiteParse OCR installed but tessdata download blocked 403, so no OCR), pytest (141 courtroom tests pass), Node playwright + pypdf (PDF build), git/GitHub, claude.ai Artifact and ArtifactComments tools, Agent tool (general-purpose Sonnet/Opus, web-fetch subagent, court-judge/council-* agents), Jev hook (advisory review on commits, said "escalate" at 0.42, diff cut), free NVIDIA models (earlier trials in docs/courtroom-model-trial-1-results.md).

## Known errors and caveats
- I read the wrong annual report first (2022) and mixed Rs million with Rs crore once (3,856 million = 385.6 crore; Screener FY26 net profit 369 crore; FY25 gap 1,013 vs 1,429 crore unreconciled).
- Judge final predates the closing rewrite; Analyst hearing covers I3-I9 only; flag F1 merges leverage ceiling A7 (arguable); Kid/Teen plain lines need a human skim; Screener "Sep 2026" shareholding column plausible but unchecked.
- Open: Q2 FY27 results due 2026-11-04 (half-year cash flow, covenant statement, finance costs vs 2,132, capitalised interest); notes 4 and 5(B) of the Sep 2024 filing; Chairperson's own pay and Syngene/BBL pay; covenant limits; real Shariah screen (needs Mac + NotebookLM; no VPS job exists).
