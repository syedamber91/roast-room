# numbers: BIOCON, filed quarters and price

Nothing in this file is live. It is a dated snapshot of the record. Last price week: 2026-10-23. Money is in Rs million as filed (consolidated).

## Filed quarters, consolidated

Source: the company's quarterly results filings, consolidated. The Source column says which filing each row was read from. Each row is the quarter ended on that date.

| Quarter ended | Revenue from operations | of which other operating revenue | Operating profit | Operating margin % | Finance costs | Profit for the period | Profit to shareholders | Source |
|---|---|---|---|---|---|---|---|---|
| 2023-12-31 | 39,537 | 4,050 | 9,268 | 23.4 | 2,667 | 7,533 | 6,600 | own filing |
| 2024-03-31 | 39,171 | 533 | 9,159 | 23.4 | 2,270 | 2,229 | 1,355 | own filing |
| 2024-06-30 | 34,329 | 568 | 6,204 | 18.1 | 2,360 | 8,618 | 6,597 | comparative in the Sep 2024 filing (agrees with the Jun 2025 filing's year-ago column) |
| 2024-09-30 | 35,904 | 454 | 6,854 | 19.1 | 2,256 | 271 | -160 | own filing |
| 2024-12-31 | 38,214 | 484 | 7,518 | 19.7 | 2,234 | 811 | 251 | own filing |
| 2025-03-31 | 44,170 | 589 | 10,782 | 24.4 | 2,124 | 4,594 | 3,445 | own filing |
| 2025-06-30 | 39,419 | 318 | 7,489 | 19.0 | 2,767 | 892 | 314 | own filing |
| 2025-09-30 | 42,955 | 330 | 8,354 | 19.4 | 2,722 | 1,328 | 845 | comparative column in the Dec 2025 filing (the quarter's own filing text is too damaged to read) |
| 2025-12-31 | 41,730 | 500 | 8,335 | 20.0 | 2,099 | -518 | 1,438 | own filing with two cells repaired by identity |
| 2026-03-31 | 45,166 | 323 | 10,203 | 22.6 | 2,315 | 1,986 | 1,259 | own filing |
| 2026-06-30 | 43,360 | 442 | 8,472 | 19.5 | 2,132 | 1,368 | 1,411 | own filing |

Notes the filing read carries:

- 2023-12-31: Text layer has OCR damage elsewhere in the filing; every figure here ties out and sales and profit match XBRL. Other income 5655 and other operating revenue 4050 carry one-offs.
- 2024-03-31: Sales and profit match XBRL.
- 2024-06-30: The quarter's own filing text was not parsed. Sales and profit match XBRL, which is the quarter's own filing. Other income 11345 is a one-off.
- 2024-09-30: Sales and profit match XBRL. Tax includes 199 on removal of the indexation benefit.
- 2024-12-31: Sales and profit match XBRL.
- 2025-03-31: No XBRL for this quarter (the NSE endpoint stops at Dec 2024).
- 2025-06-30: The Jun 2026 filing re-presents this quarter: total expenses 39075, profit before exceptional items 1141, exceptional items -172. Profit before tax 969 and profit 892 are unchanged. This row is as first filed.
- 2025-09-30: The Sep 2025 filing's own text is OCR-damaged (for example total income reads 43 8!5 and cost of materials 13 615). Cost of materials is 13675 because only that value makes the cost lines sum to the printed 42185. Needs a second source (a third-party data aggregator) and carries the label OCR-read.
- 2025-12-31: Total income prints as 42 !l03 and is 42903 (revenue plus other income, and the Mar 2026 filing's comparative). Deferred tax prints as (830) in the clean cell. Exceptional items -2934 are large. No XBRL.
- 2026-03-31: No XBRL.
- 2026-06-30: No XBRL.

## Segments

Source: the filed segment note. Rs million. The third segment changes name in the filings: Research services, then CRDMO from the quarter ended 2025-06-30, then Services from 2026-06-30. The Q1 FY27 deck (S025) also moved a utilities cross charge out of Generics, so the 2026-06-30 row is not on the same basis as the rows before it.

| Quarter ended | Generics | Biosimilars | Third segment (name as filed) | Third segment | Net sales | Source |
|---|---|---|---|---|---|---|
| 2023-12-31 | 7,034 | 24,829 | Research services | 8,535 | 39,537 | own filing |
| 2024-03-31 | 7,184 | 23,578 | Research services | 9,169 | 39,171 | comparative column in the Mar 2025 filing (the Mar 2024 filing's own table was not read) |
| 2024-06-30 | 6,593 | 20,834 | Research services | 7,897 | 34,329 | comparative column in the Sep 2024 filing (agrees with the Jun 2025 filing) |
| 2024-09-30 | 6,243 | 21,816 | Research services | 8,910 | 35,904 | own filing |
| 2024-12-31 | 6,864 | 22,890 | Research services | 9,437 | 38,214 | own filing |
| 2025-03-31 | 10,475 | 24,634 | Research services | 10,180 | 44,170 | own filing |
| 2025-06-30 | 6,965 | 24,578 | CRDMO | 8,745 | 39,419 | own filing (first filed) |
| 2025-09-30 | 7,736 | 27,211 | CRDMO | 9,106 | 42,955 | comparative column in the Dec 2025 filing (the quarter's own filing is OCR-damaged) |
| 2025-12-31 | 8,513 | 24,967 | CRDMO | 9,171 | 41,730 | own filing |
| 2026-03-31 | 8,467 | 27,556 | CRDMO | 10,365 | 45,166 | own filing (first filed) |
| 2026-06-30 | 7,597 | 28,556 | Services | 7,360 | 43,360 | own filing |

## Price, as of the last weekly bar

There is no live feed. The price is the last close in the weekly closes on file. It is context for the dates above, not a signal.

| Measure | Value | As of | Source |
|---|---|---|---|
| Last weekly close | 323.50 | week ending 2026-10-23 | NSE weekly closes |
| 52-week high / low of weekly closes | 437.20 / 323.50 | 52 weeks to 2026-10-23 | NSE weekly closes |
