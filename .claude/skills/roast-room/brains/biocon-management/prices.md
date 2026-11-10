# Prices: BIOCON management, weekly price history

Built from two weekly price series added to the record on 2026-11-10. Nothing here is live: the last week is the
one ending 2026-10-23.

## Sources

- S039 | BIOCON weekly bars (open, high, low, close, volume), 360 weeks from 2019-12-06 to 2026-10-23, as frozen in
  soic-ladder `docs/idea/case-study/BIOCON/weekly-bars-BIOCON.csv` (Yahoo Finance, NSE: BIOCON.NS) | file:
  `docs/company-record/biocon/weekly-bars-BIOCON-2026-10-23.csv`
- S040 | Nifty 500 index weekly bars (Yahoo Finance ^CRSLDX), daily prices grouped into calendar weeks ending on each
  week's last trading day, 360 weeks from 2019-12-06 to 2026-10-23, fetched 2026-11-10 | file:
  `docs/company-record/biocon/weekly-bars-NIFTY500-2026-10-23.csv`

The two series match on all 360 calendar weeks. Join them by ISO year and week, not by date string: a
holiday week can end on a different day for the stock and the index.

Prices are not adjusted for dividends. Splits and bonus issues in the window are not checked here.

## Derived figures (arithmetic on S039 and S040, not record figures)

| Figure | Value | How |
|---|---|---|
| Highest weekly close in the window | 481.95 (week ending 2020-12-24) | max of S039 closes |
| Lowest weekly close in the window | 198.70 (week ending 2023-03-24) | min of S039 closes |
| Worst fall from a prior peak | -58.8% (peak week 2020-12-24, low week 2023-03-24) | largest drop of a close below the highest close before it |
| Last close against its 52-week range | 323.50, range 323.50 to 437.20 | last 52 weekly closes |
| 30-week exponential average of closes | 388.05; last close is below it (-16.6%) | EMA, period 30, seeded with the first close |
| 26-week change, BIOCON | -7.5% | last close against the close 26 weeks earlier |
| 26-week change, Nifty 500 | -5.1% | same, on S040 |
| 26-week change, BIOCON against Nifty 500 | -2.5 percentage points | difference of the two |

These are inputs for the Filings Coach's Level 8 steps (chart, stage, relative strength, price-exit rules). They
describe the price; they are not a view on value and not a signal to act.
