# India macro series and real revenue growth, BIOCON: S052

Written 2026-11-11 from series fetched on the VPS (soic-ladder `case-study` mode `macro-wb`; files with sha256 in `docs/idea/case-study/BIOCON/data/macro-wb/worldbank-manifest.csv`) and RBI Handbook tables already held. The framework rows name MoSPI releases, which did not connect from here, so these stand in; each line says which source and which basis. **Calendar-year values (World Bank) and fiscal-year values (RBI) are not interchangeable.** Real growth is arithmetic on stored figures and never a filed number. A screen, not investment advice.

## Inflation (consumer prices)

| Basis | FY22 | FY23 | FY24 | FY25 | FY26 | Five-year chain |
|---|---|---|---|---|---|---|
| RBI Handbook Table 236 (fiscal year, NSO series), % | 5.5 | 6.7 | 5.4 | 4.6 | 3.1 | factor 1.2795 |
| World Bank, calendar year used for each fiscal year (the year the fiscal year starts: 2021 to 2025), % | 5.13 | 6.70 | 5.65 | 4.95 | 2.40 | factor 1.2736 |

Use the RBI fiscal-year series as the primary basis; the two agree within about 1 point over five years.

## Biocon's growth made real, FY21 to FY26 (derived)

| Line | Nominal | Real (fiscal CPI, factor 1.2795) |
|---|---|---|
| Revenue from operations, Rs 71,431 million (FY21) to Rs 169,270 million (FY26) | +137.0% | **+85.2%** |
| Total income, Rs 73,976 million to Rs 172,695 million | +133.4% | **+82.4%** (+83.3% with the World Bank chain; compound rates 18.48% nominal and 12.88% real) |

**The choice of line matters for a single year.** FY26 growth is 4.85% on total income and about 10.9% on revenue from operations (nominal); over five years the choice moves the real figure by under 3 points. Total income includes other income, so it is the company's stated-margin basis, not its revenue line. The year-by-year table is `docs/idea/case-study/BIOCON/record/macro-wb/real-growth-2026-08-30.csv` (soic-ladder), which matches fiscal year X to calendar year X-1 for the World Bank chain (9 of the 12 months fall there): an approximation, not a MoSPI fiscal-year figure.

## GDP growth

World Bank real GDP growth for India, calendar year, 1996 to 2025: geometric mean **6.27% a year** (30 values). Recent: 2020 -5.78, 2021 9.69, 2022 7.61, 2023 7.21, 2024 7.10, 2025 7.57 (%). A nominal long-run growth can be chained from the World Bank GDP deflator file and comes to about 11.83% a year, **derived, not published**; it is about 5.6 points above the real figure, so any comparison must say which one it uses. RBI Handbook Tables 226 and 227 give published fiscal-year nominal and real growth for FY20 to FY26 (for example FY26 nominal growth 8.89%, 34,635,638 against 31,807,309).

## Deposit and lending rates (for a cost-of-capital comparison)

RBI Handbook Table 59, end of March: scheduled commercial banks' all-banks weighted average domestic term deposit rate FY22 5.03, FY23 6.22, FY24 6.96, FY25 7.11, FY26 6.62 (%); five-bank 1 to 3 year deposit rates 5.00 to 5.20, 5.30 to 5.60, 6.50 to 7.25, 6.70 to 7.25 and 6.25 to 6.60 (%) for FY22 to FY26. The SBI card held is current only, with no history. The World Bank deposit-rate series returned no values for India; its lending and real rate series stop at 2022. **The cost of capital itself is the reader's own assumption; no document fixes it.**

## What is still not held

An industry growth history for the years past (the annual reports hold forward projections only), monthly CPI before April 2024, and crude (PPAC Indian basket) for April 2022 to March 2023 and before 2020. Rows L6-0 and L8-61 stay partial for these reasons.
