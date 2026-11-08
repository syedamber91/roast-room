# Sources, PIIND (PI Industries): partial

Not a finished source index. Only the documents that have been read so far are listed. Everything else the seat needs is in `docs/piind-seat-plan.md` section 3. The calls, decks and annual reports are not listed because no row has been extracted from them yet.

| Id | Document class | File in this brain | CSV in `docs/company-record/piind/` (sha256, first 12) | Read by | Limits |
|---|---|---|---|---|---|
| S041 | Shareholding pattern (NSE XBRL), 21 filings, 2021-09-30 to 2026-09-30 | `shareholding.md` | `shareholding-pattern-2026-11-09.csv` (65fcebd3ceae) | code (soic-ladder `case_study_shareholding.py`) | none known |
| S042 | Voting results, 3 AGMs or postal ballots, 2023-08-17 to 2026-08-14 | `votes.md` | `voting-results-2026-11-09.csv` (d577566a42f6) | code (`case_study_votes.py`) | resolution wording not read; 2023 AGM unreadable; meeting date is the filing date where the annex prints none |
| S043 | Segment tables (results XBRL to 2024-12-31, results PDFs to 2026-09-30) | `segments.md` | `segments-quarterly-xbrl-2026-11-09.csv` (36ede1b405cb), `segments-quarterly-pdf-2026-11-09.csv` (bceb82f5a46f) | code (`case_study_segments.py`, `case_study_segments_pdf.py`) | 2025-09-30 not read; scanned filings |
| S044 | Quarterly results lines (results XBRL to 2024-12-31, results PDFs to 2026-09-30) | `results.md` | `results-quarterly-xbrl-2026-11-09.csv` (a7fcb9b5c63a), `results-quarterly-pdf-2026-11-09.csv` (65a9bfdf6456) | code (`case_study_results.py`) | 2025-12-31 not read (its own column fails its arithmetic); single cells unread in 4 rows (scans) |

The readers are in the soic-ladder repo, branch `piind-seat-data` (not merged when this was written). The seat is **not ready**: no agent file, no roster entry, no data pack, no call or annual report extraction.
