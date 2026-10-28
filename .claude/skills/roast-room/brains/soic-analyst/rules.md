# Rules: SOIC Analyst

Every numeric threshold, band, ratio bar, multiple, holding period, moving-average length, stop and exit trigger the SOIC course states, merged across its lectures, worked analyses and decision notes. This is the file an analyst looks up before quoting a number. Quotes are quoted from the notes on the course, never the seat's own words.

Contents:
- How to read an entry
- A. Screening gates (growth, margins, return ratios, debt, cash flow)
- B. Forensic bars
- C. Ratio bars by sector and by lender versus non-lender
- D. Valuation (P/E bands, PEG, implied growth, margin of safety, DCF assumptions)
- E. Technicals and timing (30-week average, RSI, relative strength, stages, entry and exit)
- F. Position sizing and portfolio
- G. Capital cycle and capacity
- H. Sector-specific bars
- I. Where the sources disagree, in one place
- J. The course does not state a number for

## How to read an entry

- **Status.** RULE means the course states the number as a rule, a screen setting or a stated bar. EXAMPLE means a worked case, one company's figures or an illustration. ASSUMPTION means the course says "let's assume" or builds a scenario input. Where the course itself calls a number a rule of thumb or the instructor's heuristic, the entry says so beside the status.
- **PERISHABLE** marks a company snapshot, a dated market level, a policy as of the lecture, or a forecast. It is true of one date only. Do not carry it forward as a bar.
- **Dates** are the note or lecture date: S001 to S003 2026-07-28; S005 to S011 and S506 to S528 2026-07-14 (S507 2026-07-27); S012 to S123 and S425 to S505 mostly 2026-07-27; S124 to S225 and S307 to S424 2026-07-26; S226 to S233, S247 to S254 and S292 to S306 2026-07-28.
- **Sources** counts the distinct sources that state the item, with ids. One source repeating itself counts once. Where sources state different numbers for the same thing, both are shown with ids and the entry says DISAGREE.
- **Lesson code.** The code after each source id (for example MODULB 01:58:04) is the lesson and timestamp inside that source.
- **Compiled lists are not lecture notes.** S001 (the compiled framework list), S002 (a compiled rule set) and S003 (a compiled metric registry) were built from the lectures. They are not lecture notes. A bar supported only by S001 to S003 (and the worked case S010) is a compiled-list claim, and the seat says so. Such an entry is marked Status: COMPILED RULE (compiled list, not stated in a lecture note).
- **Quotes are note prose unless they carry a lecture code.** Many quotes are summary text written in the notes. Only a quote that carries a lecture code and timestamp (for example MASTEC 00:09:35) is transcript speech.
- These are the course's numbers, described. They are not advice to buy, sell or hold anything, and a number here never overrides the check of live company data.

---

## A. Screening gates (growth, margins, return ratios, debt, cash flow)

### A1. The growth screen: quarterly sales above 15%, quarterly PAT above 20%
- **Rule:** the course's mechanical first-pass screen flags companies whose latest quarterly sales grew above 15% year on year and whose quarterly PAT grew above 20% year on year, both at once.
- **Number:** sales growth more than 15% YoY AND PAT growth more than 20% YoY.
- **Applies to:** companies on the Indian quarterly results screen. The compiled framework list (S001) records that the course's own prose calls it "a first-pass screen, not a buy signal on its own" (S001).
- **Status:** RULE (a stated screen setting). Dates: 2026-07-27 (S119, S454), 2026-07-28 (S001, S002), 2026-07-14 (S005, S006, S506, S513, S515, S522, S525).
- **Quote:** "greater than 15% year-over-year quarterly sales growth" (S454, MASTEC 00:09:35)
- **Sources:** 11 (S001, S002, S005, S006, S119, S454, S506, S513, S515, S522, S525). The tracker is run one day a week, for example Friday evenings (S513, S515, S522, S525).
- **Disagree:** none on the numbers. S431 gives a looser version, "top-line or profit growth exceeding 15% to 20% over multiple quarters" (S431, TVGPB 00:56:57), which is a growth range, not the two-bar screen.

### A2. Operating leverage turns on above about 15% to 20% sales growth
- **Rule:** operating leverage shows in profit once sales growth is above roughly 15% to 20%.
- **Number:** 20 or more in the compiled rule set (S002); 15 to 20 percent in the lecture (S289).
- **Applies to:** businesses with a large fixed-cost base (PEB, hotels, capex-heavy plants).
- **Status:** RULE (the 15 to 20 band is stated in the PEB lecture, S289); COMPILED RULE (compiled list, not stated in a lecture note) for the 20 line, quarterly sales growth YoY at or above 20 (S002); EXAMPLE for the sector statement in S289. Dates 2026-07-28 (S001, S002), 2026-07-26 (S289).
- **Quote:** "if a company has more than 15-20% sales growth in the sector, then you can get an element of operating leverage there" (S289, PEB 00:44:09)
- **Sources:** 3 (S001, S002, S289).
- **Disagree:** the compiled rule set (S002) uses 20 as its line; the lecture (S289) and the compiled framework list (S001) state a 15 to 20 band. This is the compiled list set against the lecture, not the course disagreeing with itself. Both are shown.

### A3. Share-gain test: three-year compounded sales growth at or above 20%
- **Rule:** a company growing 20% or more over three years, against a market growing far slower, is gaining share.
- **Number:** 3-year compounded sales growth at or above 20 (S002, the compiled rule set); the "sitting-duck test" compares 20% to 30% growth against nominal GDP (S001).
- **Status:** COMPILED RULE (compiled list, not stated in a lecture note) for the 20 line (S002); EXAMPLE for the Entero case. PERISHABLE for Entero. Dates 2026-07-28 (S001, S002), 2026-07-14 (S506, S517, S519).
- **Quote:** "Entero Healthcare was growing at 28%, compared to the Indian pharma market's overall growth rate of 9%." (S517)
- **Sources:** 5 (S001, S002, S506, S517, S519). Entero's 28% against 9% is about 3x.
- **Related rule of thumb (S282, 2026-07-26):** "if a company is growing at a rate of 12-15% per annum we can say that either the company is small or they might be taking away some market share" (S282, AROMA 00:25:41). This is the instructor's own reading, for a sector growing 2% to 3% a year.

### A4. Margin-expansion scan: operating margin up 10% quarter on quarter for three or four quarters
- **Rule:** scan for companies whose operating profit margin rose 10% on the prior quarter, held for three or four consecutive quarters, rather than one.
- **Number:** OPM latest quarter greater than OPM one quarter back by 10%; OPM above a floor of 1%; the S001 version adds market cap under 20,000 cr and a breakout above 30 percent over a flat baseline. An alternate scan in S482 uses margin expansion above 20%.
- **Applies to:** the "fundamental breakout" scan across listed companies.
- **Status:** RULE (stated scan setting). Dates 2026-07-27 (S119, S482), 2026-07-28 (S001).
- **Quote:** "OPM latest quarter is greater than of OPM one quarter back by 10%" (S482, SOICE3 00:42:51)
- **Sources:** 3 (S001, S119, S482).
- **Disagree:** S482 also gives "today's earnings are more than 30%" (S482, SOICE3 00:14:46) and "margin expansion is more than of 20%" (S482, SOICE3 00:46:21) as alternate values; S119 and S001 use 10%.

### A5. Hyper growth and the J-curve window
- **Rule:** hyper growth is defined on the top line, and the course says enter during the first quarters of the inflection, not after years of it.
- **Number:** hyper growth "anywhere above 20-25%" on the top line; enter during the first three to four quarters of inflection; growth of 50% to 80% typically lasts one to three years.
- **Status:** RULE for the definition and entry window (S496); EXAMPLE for the duration (S491). Date 2026-07-27.
- **Quote:** "anywhere above 20-25% on a top line level" (S496, SOICE5 01:02:25)
- **Sources:** 2 (S491, S496). No second source on the one-to-three-year duration.

### A6. Return on capital and return on equity at or above 15%
- **Rule:** a quality company earns return on capital or equity above 15%, or is trending toward it.
- **Number:** 15% (ROC or ROE). The core-portfolio profile in S096 states 15 to 20% ROE with 20 to 25% compounding growth.
- **Applies to:** non-lenders on the fundamentals leg of the checklist; for banks the course uses ROA and ROE (see C).
- **Status:** RULE (checklist leg). Dates 2026-07-27 (S096, S456), 2026-07-28 (S001).
- **Quote:** "above the 15% threshold" (S456, MASTED 01:36:54)
- **Sources:** 3 (S001, S096, S456).
- **Context numbers (EXAMPLE):** a 10% return on capital is poor against a 5 to 6 percent fixed deposit (S032, MODULB 00:06:37); ROE of 25% is "phenomenal" and the Nifty 500 average ROE is about 14% (S061, 2026-07-27); long-term Nifty earnings growth and ROE are "between 12-14%" (S087, HOWB 00:21:02).

### A7. Debt to equity at or below 0.7; above 1 is a caution
- **Rule:** a healthy balance sheet runs debt to equity under 0.7; above 1 is treated with caution.
- **Number:** at or below 0.7 (S002, the compiled rule set); "less than 0.7 times" (S451 lecture note); above 1 is the caution level (S001 F26, S456).
- **Applies to:** non-lenders. For lenders the course describes leverage of 14x to 16x for PSU and regional banks (S332), so this bar does not carry over.
- **Status:** RULE. Dates 2026-07-27 (S451, S456), 2026-07-28 (S001, S002).
- **Quote:** "debt-to-equity ratio of less than 0.7 times for a healthy balance sheet" (S451, MASTEA 01:52:15)
- **Sources:** 4 (S001, S002, S451, S456).
- **Disagree (boundary):** S002 uses "at or below 0.7"; S451 says "less than 0.7". The course does not say what to do between 0.7 and 1.

### A8. Cash conversion: CFO to EBITDA about 70% for B2C and 60% for B2B
- **Rule:** the share of EBITDA that turns into operating cash flow should be about 70% for consumer-facing B2C and 60% for B2B, because B2B carries more inventory and looser credit. The course treats it as a veto-class gate (F21).
- **Number:** about 70% (B2C), about 60% (B2B). The compiled rule set (S002) states a single line: 3-year average CFO/EBITDA at or above 60.
- **Status:** RULE (rule of thumb). Dates 2026-07-27 (S036, S045, S050), 2026-07-28 (S001, S002).
- **Quote:** "should ideally be around 70% for consumer-facing B2C businesses and 60% for B2B businesses" (S036, MODULB 01:58:04)
- **Sources:** 5 (S001, S002, S036, S045, S050). Cash flow statements arrive with the Q2 (H1) and Q4 (H2) results (S050).
- **Disagree (denominator):** S036, S050 and S001 apply 70/60 to CFO over EBITDA. S045 words it as CFO divided by PAT: "more than 70% for B2C business and for B2B is more than 60%" (S045, UPDAT 00:13:06). A second pair appears in A9.
- **Rule on method:** subtract other income from EBITDA before the ratio, because it "does not reflect core cash operating profit" (S050, MODULA 00:23:26).

### A9. Cash conversion: CFO to PAT, four different bands
- **Rule:** CFO to PAT is checked beside CFO to EBITDA. The sources state the bar at different levels; none is marked authoritative.
- **Numbers (DISAGREE):**
  - Above 80% to 90%, ideal: S001 and S470 (2026-07-28, 2026-07-27).
  - Business-to-business 60% to 70% of PAT adequate, business-to-consumer 80% to 90%: S452 (2026-07-27).
  - Above 90% to 95% as a preference, with CFO to EBITDA above 60% to 65%: S494 (2026-07-27) and S001 F38 (2026-07-28). S001 says to treat the two pairs as "calibration ranges, not one authoritative number".
  - 70% B2C and 60% B2B on CFO over PAT: S045 (see A8).
- **Status:** RULE (stated as ideal, working standard or preference).
- **Quote:** "should ideally be above 80% to 90%" (S470, SOICC2 00:16:24)
- **Sources:** 5 (S001, S045, S452, S470, S494).
- **Related:** S452 adds that B2B models should generally trade at a valuation discount. Net margin on traded third-party goods runs about 1% against 10% to 15% for core manufacturing (S001 F21, EXAMPLE).

### A11. Incremental returns: reinvestment rate times ROIIC
- **Rule:** intrinsic compounding equals the reinvestment rate multiplied by the return on incremental invested capital. Reinvestment rate is incremental invested capital over cumulative earnings for the period.
- **Number:** none stated as a bar. The worked case: almost 60% reinvested at a 35% return gives 20% intrinsic compounding (Chipotle, nine years).
- **Status:** EXAMPLE for the figures, RULE for the formula. PERISHABLE (one company). Date 2026-07-27.
- **Quote:** "Multiplying this reinvestment rate by the ROIIC yielded an intrinsic compounding rate of 20%" (S059, MODULG 00:21:53)
- **Sources:** 1 for the worked figures (S059); S084 and S046 teach the same incremental-return idea without a threshold.

---

## B. Forensic bars

### B1. Contingent liabilities above 20% of net worth
- **Rule:** be cautious when contingent liabilities exceed 20% of net worth.
- **Number:** 20% of net worth. Worked cases, PERISHABLE: one company at 479% of net worth, mostly guarantees to relatives and subsidiaries (S049); Heranba at 61% (S008).
- **Status:** RULE (instructor's caution level); EXAMPLE for the cases. Dates 2026-07-27 (S049), 2026-07-14 (S008).
- **Quote:** "479%" (S049, MODULG 00:25:45) is the company case; the 20% line is spoken at MODULG 00:25:55 (S049).
- **Sources:** 2 (S008, S049).

### B2. Related-party transactions: above 10% of sales is suspect; 35% to 40% of PAT is uninvestable
- **Rule:** related-party transactions above 10% of sales call for suspicion. Routing 35% to 40% of PAT through related parties makes a company generally uninvestable.
- **Number:** 10% (of sales); 35% to 40% (of PAT).
- **Status:** RULE. Date 2026-07-27.
- **Quote:** "Anything more than 10% should be viewed with suspicion." (S066, MODULJ 00:11:24)
- **Second quote:** "companies routing 35% to 40% of their profit after tax (PAT) through related parties are generally considered uninvestable" (S068, MODULJ 00:11:01)
- **Sources:** 2 (S066, S068). S054 adds three tests that a related-party flow is genuine (healthy operating cash flow to EBITDA, debtor days showing money is collected, dividends paid) with no numeric cut.

### B3. Miscellaneous expenses and management pay
- **Rule:** miscellaneous expenses of 20% to 30% of total other expenses are a red flag. The maximum remuneration a company can normally take is 11% of PAT.
- **Number:** 20% to 30% of other expenses; 11% of PAT.
- **Status:** RULE. Date 2026-07-27.
- **Quote:** "if it represents 20-30% of total other expenses, it constitutes a red flag" (S066, MODULJ 00:06:21)
- **Sources:** 1 (S066). The 11% line is in the same source at MODULF 00:28:56.

### B4. Receivables delayed beyond 180 days
- **Rule:** a spike in trade receivables delayed by more than 180 days is a flag. Receivable days that run disproportionately above peers can signal fabricated sales; days that keep stretching signal poor quality of sales.
- **Number:** 180 days.
- **Status:** RULE (flag). Dates 2026-07-28 (S001), 2026-07-27 (S036, S057).
- **Quote:** "a spike in trade receivables that are delayed by more than 180 days" (S001, MODULA 00:15:05)
- **Sources:** 3 (S001, S036, S057). The course gives no days bar for "normal" receivables; it asks for comparison with peers.

### B5. Goodwill and impairment assumptions
- **Rule:** a discount rate of 12% or higher is standard, and a terminal growth of 2% to 4% is historically normal in an impairment test. Far more aggressive assumptions used to avoid impairment are a red flag.
- **Number:** discount rate 12% or higher; terminal growth 2% to 4%.
- **Status:** RULE (stated as standard and acceptable). Date 2026-07-27.
- **Quote:** "A discount rate of 12% or higher is considered standard and acceptable, and a terminal value growth expectation between 2% and 4% is historically normal" (S053, MODULH 00:18:07)
- **Sources:** 1 (S053). Intangible write-off rates of 23 to 33 percent were shown for Sharda (S008, EXAMPLE, PERISHABLE).

### B6. Auditor and key-management exits
- **Rule:** a mass exodus of key managers or auditors is an amber flag demanding scepticism, not proof of fraud. A qualified audit opinion is a yellow flag.
- **Number:** none as a bar. Statutory auditor resignations spiked to 42 across the market in 2018 (PERISHABLE, S052).
- **Status:** RULE (flag colour); EXAMPLE for the 42.
- **Quote:** "amber flag" (S052, MODULE 00:01:10); "yellow flag" (S470, SOICC2 00:29:50)
- **Sources:** 5 (S001, S052, S111, S116, S470); S111 and S116 name governance lapses and an auditor or board leaving as exit reasons.

### B7. Abnormal profit growth builds a base
- **Rule:** profit growth of 200% to 300% builds a large base and sets up risk the next year if it does not repeat. Straight-line earnings at a triple-digit P/E usually mean time to exit.
- **Number:** 200% to 300%.
- **Status:** RULE (instructor guidance). Date 2026-07-27.
- **Quote:** "setting up for disaster in next financial year if the growth doesn't repeat" (S111, FRAMEC 01:18:28)
- **Sources:** 2 (S111; S507 describes the mirror case, post-IPO growth struggles against an inflated base).

### B9. Concentration and dependence filters
- **Rule:** single-product, single-customer and single-country dependence is a risk; some deletion filters are stated outright.
- **Numbers:** one molecule at 35% to 50% of sales draws a commodity P/E (Excel Industries), Aztec at 50% to 60%, Bharat Rasayan targets a cap of 12% to 13% per product (S008, PERISHABLE). Delete a company that is 50%, 60% or 70% dependent on China for materials (S401). 27 products on the scheduled-for-ban list, a domestic market of about 12,000 cr (S008, S341, PERISHABLE).
- **Status:** RULE (deletion filter, S401); EXAMPLE and PERISHABLE (company shares).
- **Quote:** "50, 60, 70% dependent is on China for all material" (S401, APIM 00:02:29)
- **Sources:** 3 (S008, S341, S401). S401 also deletes on volatile margins and on unresolved regulatory violations (APIM 00:02:19, 00:02:36).

### B10. Volume against value growth
- **Rule:** pure volume-led growth is the highest quality; value-led growth is good when it comes from a better mix. Do not substitute value growth for volume growth.
- **Number:** the compiled rule set states a 10% volume-growth line (S002), and value growth must not stand in for volume growth. Best case price times volume: 10 packets at 10 rupees becomes 12 packets at 12 rupees, plus 44% (S005, S342).
- **Status:** RULE (ordering); EXAMPLE (the 44%). Dates 2026-07-27 (S039), 2026-07-26 (S342), 2026-07-14 (S005), 2026-07-28 (S002).
- **Quote:** "Volume is more important than value" (S039, MODULA 01:00:39)
- **Sources:** 4 (S002, S005, S039, S342).

### B11. Capital-light and lease-heavy adjustments
- **Rule:** for lease-heavy businesses (airlines, retailers, quick-service restaurants) do not rely on EBITDA margins after Ind AS 116; compare PAT margin.
- **Number:** none.
- **Status:** RULE. Date 2026-07-27.
- **Quote:** "null and void for us as investors" (S038, MODULD 01:16:46)
- **Sources:** 1 (S038).

---

## C. Ratio bars by sector and by lender versus non-lender

The course does not use one set of bars for all companies. It first picks the metric that fits the business, then reads the bar for that sector. A lender is read on a different set of ratios from a non-lender: leverage that fails a manufacturer is a normal feature of a bank.

### C1. Pick the valuation and ratio metric by business type first
- **Rule:** match the metric to the business model before comparing any bar. Banks and financial institutions on price to book with ROA and ROE; asset-heavy hospitals and hotels on EV/EBITDA; cement on EV per ton or EV/EBITDA; real estate on market cap to pre-sales or an imputed EBITDA; IT and FMCG stay on P/E.
- **Number:** none (routing). It is the first step of the course's sector-metric routing (S001 F24).
- **Status:** RULE. Dates 2026-07-28 (S001), 2026-07-27 (S042, S047, S091, S446), 2026-07-26 (S371).
- **Quote:** "ratio of EBITDA to market cap" (S047, UPDAT 00:23:47)
- **Quote:** "P ratio is not like, is not a relevant metric" (S371, REAL 00:43:00), said of real estate because profit shows projects delivered 3 or 4 years ago (S371, REAL 00:49:28).
- **Sources:** 6 (S001, S042, S047, S091, S371, S446). Asset-heavy businesses use an exit market cap to EBITDA multiple in scenarios (S042).

### C2. Depreciation share separates asset-light from asset-heavy
- **Rule:** an asset-light platform loses little of sales to depreciation; an asset-heavy operator loses far more, which depresses P/E and justifies EV/EBITDA.
- **Number:** about 3.6% to 3.7% of sales for CDSL; about 20% (depreciation plus lease rentals) for Bharti Airtel and hospitals.
- **Status:** EXAMPLE. PERISHABLE (company benchmarks). Dates 2026-07-28 (S001), 2026-07-27 (S446).
- **Quote:** none verbatim in the source for the figures; the course states them as a comparison. Hospital buildings last 20 to 40 years, so booked depreciation is overstated (S091, 2026-07-27).
- **Sources:** 3 (S001, S091, S446).

### C3. Non-lender sector baselines (operating margin, asset turns)
- **Rule:** write the sector baseline down before judging a company. FMCG: operating margin from mid-teens to early twenties with high ROC. Specialty chemicals: operating margin more than 15% to 18% and net fixed asset turnover under 2x. Pharma net fixed asset turns 1 to 1.5x; agro is higher.
- **Status:** EXAMPLE (the note calls these sector norms). Date 2026-07-27.
- **Quote:** "more than 15 to 18%" (S062, MODULI 00:03:21)
- **Sources:** 2 (S062, S406). S406: pharma CDMO asset turns close to 1 to 1.5x with ROC above 30% for patented molecules, development cost about $2.3 billion; agro CDMO asset turns 2.5 to 3x, development cost about $250 million.
- **Quote:** "asset turns are lower, somewhere close to 1 to 1.5x asset turns, but the margins are higher" (S406, APIE 00:05:12)

### C4. Return ratios by chain node (non-lenders, all PERISHABLE)
- **Rule:** the profit pool differs by node of the value chain, so a return bar is read against that node.
- **Numbers (lecture-date, S007, 2026-07-14):** aviation tyres 25% to 30% EBITDA; aviation MRO 13% to 22%; domestic-protected solar cells 56% to 60%; water chemicals about 70% ROC; jewellery retail 15% to 18% ROE with store ROC 16% to 18% and a 5-year payback; domestic branded pharma 30% to 50% ROC; pharma CDMO 15% to 30%; generic API 15% to 17% ROC.
- **Other nodes:** integrated textile manufacturers with depreciated plants 24% to 35% ROCE; traditional garmenting capped at 15% to 17% (S306, 2026-07-28); packaging incumbents 15% to 20% ROE (S305, 2026-07-28); deep cyclicals in hotels 18% to 20% ROE and ROC for about 3 to 4 years, then a dip (S329); airports 14% ROE on aero revenue (S203).
- **Status:** EXAMPLE and PERISHABLE.
- **Quote:** "single digit ROC business" (S306, HOWD 00:19:28), said of garmenting in a downturn.
- **Sources:** 6 (S007, S203, S302, S305, S306, S329). S302 (2026-07-28) states patented CDMOs earn ROE of 15% up to 30% and domestic branded pharma 30% to 50% ROCE.
- **Disagree:** S007 lists pharma CDMO as 15% to 30% on ROC; S302 states 15% to 30% on ROE; S406 says above 30% ROC for patented molecules. The metric differs between sources; do not merge them.

### C5. Regulated and hard-asset return caps
- **Rule:** where a regulator caps returns, expect ROE or ROC to sit near the cap. If ROCE rose to 40% to 50% the regulator would step in.
- **Numbers:** regulated transmission owner ROE capped at 12% to 13% (S256); hard-asset natural monopolies near 12% to 13% (S250); ports behave like a toll road at 15% to 16% ROE (S216); data center asset owners 10% to 12% ROE while proxy suppliers earn 25% to 35% (S248).
- **Status:** EXAMPLE and PERISHABLE. Dates 2026-07-26 (S216, S256), 2026-07-28 (S248, S250).
- **Quote:** "capped at 12-13%" (S256, CAPITA 02:18:26)
- **Sources:** 4 (S216, S248, S250, S256).
- **Disagree:** S248 states data center asset owners earn "around 10% to 12%" (S248, HIGHLB 00:49:22) and, elsewhere in the same source, "a low 6% to 10% return on equity for operators" (S248, HIGHLB 01:11:58). The two ranges are not reconciled.

### C6. Banks (lender): growth, ROA and ROE bars
- **Rule:** a bank's ROE and ROA dictate its price to book. Large private banks with 15% to 20% loan growth are the "compounder" type; old private banks are cyclical and the course says the only viable time to invest is a benign credit cycle. Avoid single-digit ROE banks.
- **Number:** loan growth 15% to 20%; ROE at least double digit. EXAMPLE, not a bar: S339 describes large private banks as having ROA above 1.8% (DECODA 00:05:48), a description of that type of bank, not a screen setting. A smaller bank growing 10% to 12% against 18% to 20% for HDFC or ICICI and not cheap needs no further look (S336).
- **Status:** RULE (stated bars) and EXAMPLE (the HDFC and ICICI comparison, PERISHABLE). Dates 2026-07-26 (S336, S339, S359), 2026-07-27 (S426).
- **Quote:** "at least double digit return on equity should be there" (S359, MASTEB 00:13:04)
- **Sources:** 4 (S336, S339, S359, S426).

### C7. Banks (lender): asset quality, cost and leverage
- **Rule:** read recoveries against slippages, cost to income, and leverage. Value unlocks when recoveries exceed slippages.
- **Numbers:** gross NPA means no principal or interest for more than 90 days (S334, S426); benign cycle: slippages down to about 1% and net NPAs near 1%; PSU and regional bank leverage 14x to 16x; small finance bank cost to income "usually north of 60%" (PERISHABLE); a cost to income fall from 70% to 50% can lift profit and re-rate (EXAMPLE); small finance banks must lend 75% of advances to the priority sector (S333, S339); a bank needs 1 rupee of equity for each rupee lent as the course frames it (S359).
- **Status:** RULE for the definitions and priority-sector share; EXAMPLE and PERISHABLE for the rest. Dates 2026-07-26 (S332, S333, S334, S339, S359), 2026-07-27 (S426).
- **Quote:** "debt to equity will be more because they have seen cycles and their leverage ratio is more, 15 to 16x, 14x is of all of them" (S332, DECODE 00:19:47)
- **Quote:** "greater than 90 days" (S334, DECODC 00:20:21)
- **Sources:** 5 (S332, S333, S334, S339, S426).
- **Disagree:** the leverage range is spoken as "15 to 16x, 14x" in the same sentence; read it as roughly 14x to 16x. S091 says one unit of equity can fund "ten units of assets" in general terms (S091, 2026-07-27).

### C8. NBFC funding cost and credit cards (lender, PERISHABLE)
- **Rule:** funding cost sets who can lend cheaply; unsecured books carry high credit cost.
- **Numbers:** NBFC cost of funds "7, 8% to almost 10 to 11%" by rating and equity book (S335); an NBFC at a 10% to 11% cost charging 24% to 25% against a small finance bank at about 6.6% offering 16% to 17% (S333). Credit cards: transactors are "almost 35 to 40% of any credit card book", normal NPAs 2.8% to 2.9% and 5% to 5.5% in crises, credit cost 5.5% to 6% (S338).
- **Status:** EXAMPLE, PERISHABLE. Date 2026-07-26.
- **Quote:** "almost 35 to 40% of any credit card book" (S338, DECODF 00:55:24)
- **Sources:** 3 (S333, S335, S338).

### C9. Insurance (lender-like, balance-sheet driven)
- **Rule:** read the solvency ratio, persistency, complaints and total cost ratio; value life insurers on price to embedded value.
- **Numbers:** regulatory minimum solvency of 1.5 (150%); below 200% insurers go for fundraising in practice; persistency is measured after the 13th, 49th and 61st month; complaints are counted per 10,000 policies; first-year commission about 18.5% (PERISHABLE); a tax rise from 12.5% to 25% takes a 15% hit on embedded value; global combined ratio hovers around 100% (S378).
- **Status:** RULE (regulator's minimum, 1.5); EXAMPLE for the others. Date 2026-07-26.
- **Quote:** "at least a solvency ratio of 1.5 plus" (S380, UNDERA2 01:55:23)
- **Quote:** "take a hit of 15% on their embedded value" (S382, UNDERB2 03:05:10)
- **Sources:** 3 (S378, S380, S382). Practical level: "whenever it dips below 200%" (S380, UNDERB2 02:07:02).

### C10. Gold-loan lenders: loan to value of 75% or lower, with all four safety conditions
- **Rule:** lending against gold is safe when the collateral is worth more than the loan, the lender takes possession, the collateral is independent of the borrower and the collateral is liquid. Loan to value stays at 75% or lower.
- **Number:** LTV at or below 75. In practice, as the course puts it, "They'll give out 60% around that 59, 60%." (S391, GOLDB 00:14:34). Interest sits outside the LTV. Worked case: gold value 100, LTV 75, interest of 24% on the loan, total owed 96, so a fall of about 4% reaches parity. A three-month tenure reduces the total to 82 rupees out of 100. The course says to expect a fall of 10% in a year.
- **Status:** RULE (75, S001 F12 and S002); EXAMPLE for the worked case. Dates 2026-07-28 (S001, S002), 2026-07-26 (S391, S392).
- **Quote:** "The collateral's worth should be more than the loan" (S392, GOLDB 00:22:46)
- **Quote:** "Imagine if the price falls by 4%, what will happen? The gold value and the loan taken will be same" (S391, GOLDB 00:15:30)
- **Sources:** 4 (S001, S002, S391, S392). Gross NPA "around 2.2" for the standard and about 1 for one operator, and online gold at 59% of one operator's AUM, are PERISHABLE (S391, GOLDB 00:18:45, 00:13:47).

---

## D. Valuation (P/E bands, PEG, implied growth, margin of safety, DCF assumptions)

### D1. P/E bands: 15 to 35, 15 to 30, below 50 or 40, below 25 (four bars, none a knockout)
- **Rule:** the course states several P/E lines for different jobs. 15 to 35 is the modelling band, stated only in the compiled lists and the worked case (S001, S002, S010; with 3-year profit growth at or above 20 in S002); 15 to 30 is the realistic entry band for the growth screen; below 50 or below 40 is a filter that shrinks the list; below 25 appears in one worked screener.
- **Numbers (DISAGREE across sources):** 15 to 35 (S001, S002, S010); 15 to 30 (S001, S454); below 50 or 40 (S005, S006, S228, S515, S522, S525); market cap over 1,000 cr, P/E under 25 and quarterly profit growth over 15% (S498, EXAMPLE).
- **Status:** COMPILED RULE (compiled list, not stated in a lecture note) for the 15 to 35 band, which appears only in S001, S002 and S010 (checked by search over all 528 notes); RULE for the 15 to 30 band and the below 50 or 40 filter; EXAMPLE for the S498 screen. Dates 2026-07-28 (S001, S002), 2026-07-27 (S454, S498), 2026-07-14 (S005, S006, S010, S515, S522, S525).
- **Quote:** "price-to-earnings ratio between 15 and 30 times" (S454, MASTEC 00:34:07)
- **Quote:** "setting a Price-to-Earnings (P/E) ratio filter to less than 50 or 40 times to narrow the market to a manageable list of companies matching predefined criteria" (S515)
- **Sources:** 11 (S001, S002, S005, S006, S010, S228, S454, S498, S515, S522, S525). A rapidly growing stock at a P/E of 5 is "impractical expectation" (S454, MASTEC 00:33:51).
- **Use:** the four bars are bands against growth, not an intrinsic value, and none of them is a knockout. A company's own P/E has to be read against live data before any band is applied.

### D2. PEG below 1.5
- **Rule:** the price-to-earnings-to-growth ratio should be below 1.5.
- **Number:** below 1.5 (S505 says "ideally less than 1.5 times").
- **Status:** RULE. Dates 2026-07-28 (S001), 2026-07-27 (S456, S505), 2026-07-14 (S010).
- **Quote:** "should ideally be less than 1.5 times" (S505, INSIGN 01:37:05)
- **Quote:** "Price/Earnings-to-Growth (PEG) ratio that is below 1.5" (S456, MASTED 02:51:39)
- **Sources:** 5 (S001, S010, S456, S460, S505). S460 uses PEG under 1.5 in a worked screen on US companies (EXAMPLE).
- **Worked case, PERISHABLE (S010):** the worked analysis computes PEG on two bases, 3-year profit growth and quarterly PAT growth, and the two give different values. The course gives no growth period for the PEG (limits.md).

### D3. Growth must match the multiple
- **Rule:** paying a high P/E needs growth to match. Rough pairs: P/E of about 60x needs 40% to 50% growth; P/E of about 15x to 20x needs 15% to 20% growth. At a P/E of 26x a firm must keep growing earnings about 20% or double sales in 3 to 4 years.
- **Status:** RULE (S505, S001 F38); EXAMPLE (the 26x case in S403, PERISHABLE). Dates 2026-07-27 (S505), 2026-07-28 (S001), 2026-07-26 (S403).
- **Quote:** "if you are paying a PE ratio of 60 times, the company must possess a growth rate of at least 40% to 50%" (S505, INSIGL 00:04:27)
- **Sources:** 3 (S001, S403, S505).

### D4. Growth-trap and value-trap territory
- **Rule:** a P/E of 30 to 50 times or higher assumes supernormal growth continues; above 50x needs supernormal growth to justify it. A value trap is a cheap, typically single-digit P/E with no earnings growth. Pure low P/E is not a screen: of 500 low-P/E companies only 10 or 11 beat the benchmark index over a multi-year period.
- **Number:** 30 to 50 times and above; over 50x; single-digit P/E; 10 or 11 of 500.
- **Status:** RULE (course shorthand, not a hard cutoff) for the 30 to 50 times range, quoted from the lecture (S430). The compiled rule set (S002) treats a P/E at or above 30 as an advisory flag only. Dates 2026-07-27 (S430, S432), 2026-07-28 (S001, S002).
- **Quote:** "above 30 to 50 times earnings" (S430, TVGPF 00:24:22)
- **Quote:** "only 10 or 11 managed to beat the benchmark index" (S430, TVGPG 01:12:26)
- **Sources:** 4 (S001, S002, S430, S432). S002 states that "calling a trap too early is often indistinguishable from being wrong" (S002).

### D5. Market-level valuation: Nifty 50 P/E under 20
- **Rule:** when the Nifty 50 P/E is below 20, outcomes 12 to 36 months later were predominantly positive in the course's reading, and it is treated as a key buying signal. Combined with 200-day breadth below 20% it marks extreme pessimism.
- **Number:** below 20. Worked tranches at P/E 20, 19.5 and 18.5 (EXAMPLE).
- **Status:** RULE (observation); EXAMPLE for the tranches; PERISHABLE for the 19x level (S142, S476). Dates 2026-07-28 (S001), 2026-07-27 (S471, S477, S498), 2026-07-26 (S142).
- **Quote:** "Nifty 50 is at 19 times PE right now." (S142, EVA 00:17:29)
- **Sources:** 6 (S001, S142, S471, S476, S477, S498).

### D6. Peak earnings trap and cyclical timing
- **Rule:** low P/E at peak margins is a trap; high P/E at trough margins is the time to study a cyclical. Use long-term average margins in valuation models.
- **Number:** none as a line; SAIL worked case: value emerges below 0.6 times price to book, and when it goes above 1 the cycle has usually peaked; the value zone can last 1 to 2 years (EXAMPLE, PERISHABLE).
- **Status:** RULE for the principle; EXAMPLE for SAIL. Dates 2026-07-14 (S007, S009), 2026-07-28 (S305), 2026-07-27 (S087, S446), 2026-07-26 (S319).
- **Quote:** "don't pay peak PE on peak margin on peak narrative" (S009)
- **Quote:** "Whenever it goes above 1, usually in the past the cycle has peaked" (S319, UNCOVC 00:50:25)
- **Quote:** "When their P/E ratio is getting higher, that is the time to study these companies" (S007, P3 00:41)
- **Sources:** 6 (S007, S009, S087, S305, S319, S446).

### D7. Cyclicals on price to sales or price to book against their own median
- **Rule:** buy a cyclical when price to sales is below its own historical median and sell at the cycle's peak; compare cyclicals on P/S or P/B, not an absolute level.
- **Status:** RULE. Dates 2026-07-28 (S001), 2026-07-27 (S446).
- **Sources:** 2 (S001, S446).
- **Disagree:** S228 (2026-07-28) rejects the metric in general: "Price to sales is not the correct metric in my view because in high margin businesses it will always be high." (S228, IDENTC 00:11:40). The two views apply to different businesses (cyclicals against their own history, versus high-margin businesses); the course does not reconcile them.

### D8. EV/EBITDA ceilings for asset-heavy sectors (PERISHABLE)
- **Rule:** hospitals above 30x EV/EBITDA are expensive and below 20x are cheaper; the absolute maximum for cement tends to be around 21x. A hotel exit multiple of 18x to 20x EV/EBITDA is the reasonable assumption, with similar assets trading at 15x to 17x.
- **Status:** EXAMPLE, PERISHABLE (dated calibration, "not durable thresholds" in S001). Dates 2026-07-27 (S446), 2026-07-26 (S325), 2026-07-28 (S001).
- **Quote:** "absolute maximum EV to EBITDA multiple in the cement sector tends to be around 21 times" (S446, CLASSF 02:01:19)
- **Sources:** 3 (S001, S325, S446). More hotel multiples in H.

### D9. DCF and discount-rate assumptions
- **Rule:** the course teaches DCF and reverse DCF as ballpark tools, not precision. Terminal value is a large share of the total, and the terminal growth rate must stay close to real GDP growth.
- **Numbers:** terminal value 55 to 60 percent of valuations (S088); terminal value up to 60% of valuation and terminal growth 2% to 4% (S443); cost of capital "around eight to ten percent" (S084) and about 10% in India (S061); a domestic investor may use 10% to 12% against 6% for a foreign investor (S443, EXAMPLE); goodwill tests use 12% or higher (S053, see B5); a reverse DCF that needs 30% growth for 15 to 20 years flags hyper overvaluation (S088, EXAMPLE). Example inputs in S443: interest cost on new debt 9%, tax 25%.
- **Status:** RULE for the shape; ASSUMPTION or EXAMPLE for the discount rates.
- **Quote:** "terminal growth rate must align closely with the real GDP growth" (S443, CLASSG 02:15:24)
- **Quote:** "generally estimated to be around eight to ten percent" (S084, MODULC 00:31:16)
- **Sources:** 5 (S053, S061, S084, S088, S443). Dates 2026-07-27.
- **Disagree (discount rate):** 8% to 10% (S084), about 10% (S061), 10% to 12% domestic and 6% foreign (S443), 12% or higher for impairment (S053). They answer different questions; none is a universal hurdle.

### D10. Bull, base and bear scenarios
- **Rule:** model three cases with growth and an exit multiple each, and update them on a schedule. Do not project a highly cyclical industry more than two years.
- **Numbers (EXAMPLE, S428):** bull 25% PAT growth and 40x exit P/E; base 18% and 30x; bear 15% and 25x. S089 (EXAMPLE): bear 12% to 13%, base 18%, bull 30% to 35%. Privi (PERISHABLE, S283): 25x bear, 32x to 35x base, 40x to 45x bull. Hikal (S407, PERISHABLE): bear 4,000 cr sales at 1x price to sales; bull EBITDA margin 24% to 25% at 5x price to sales and 20,000 cr.
- **Update cadence (DISAGREE):** every 6 to 12 months (S089); every 18 months (S407).
- **Status:** ASSUMPTION and EXAMPLE. Dates 2026-07-27 (S089, S428), 2026-07-26 (S283, S407).
- **Quote:** "not recommended to project the models further out than two years" (S428, TVGPJ 00:53:39)
- **Quote:** "after every 18 months, you have to update your valuation scenarios." (S407, APIH 00:18:23)
- **Sources:** 4 (S089, S283, S407, S428).

### D11. Margin of safety: stated as a multiple band for a few names, never a percentage
- **Rule:** the course names no percentage discount to value. It speaks of margin of safety as low multiples near a cyclical low, a price to book of about one or half for pessimism entries, and a shallow cycle.
- **Numbers (PERISHABLE, instructor's own bands):** RTAs: margin of safety "between 30 to 40p", risky "above 60p or 50p"; depositories: euphoric multiple warning "48KPG or 50KPG" and "70 80-90p is not normal for a cyclical business" (S265, S268). The "p" is the transcript's shorthand and is read here as a P/E multiple; unchecked against the audio.
- **Status:** EXAMPLE. Dates 2026-07-26 (S265, S268), 2026-07-27 (S116).
- **Quote:** "anything above 60p or 50p... could be risky" (S268, THEB 00:44:02)
- **Quote:** "margin of safety in valuations" (S116, FRAMEA 01:30:18)
- **Sources:** 3 (S116, S265, S268).

### D12. Roughly right, not precise
- **Rule:** finance is part art and part science, and valuation is a gate rather than the centerpiece. Euphoric markets can push multiples past any model.
- **Number:** the course puts it at 50% to 60% art and 40% to 50% science.
- **Status:** RULE (stated stance). Dates 2026-07-27 (S058, S438, S439), 2026-07-14 (S520).
- **Quote:** "50 60% art and only 40 50% science" (S439, CLASSB 00:19:56)
- **Quote:** "we have to be roughly right rather than be precisely wrong" (S058, MODULH 02:52:59)
- **Quote:** "The valuation step is a gate, not the centerpiece of the analysis" (S520)
- **Sources:** 5 (S058, S438, S439, S443, S520). S439 gives a retail stock at P/E 279, about five times the normal standard deviation for retail, as "very expensive" without a precise target (EXAMPLE, PERISHABLE).

### D13. The valuation bar flexes with the market cycle
- **Rule:** bear markets are strict on P/E; bull markets tolerate a higher P/E for a visible multi-year runway with technical confirmation. The course forbids a hard cap.
- **Number:** none.
- **Status:** COMPILED RULE (compiled list, not stated in a lecture note): the no-hard-cap wording is in S001 and S010 only (checked by search over all 528 notes). Dates 2026-07-28 (S001), 2026-07-27 (S456), 2026-07-14 (S010).
- **Quote:** "the valuation bar itself flexes with" (S010, section 0)
- **Sources:** 3 (S001, S010, S456).

### D14. Order-book businesses are not valued on P/E
- **Rule:** value an order-book business as an order-book business. Discount the pipeline for the chance of winning. When the ratio of order book to revenue passes five to seven times in a long-dated book, growth can last five to seven years.
- **Number:** discount the pipeline by 50% to 60%; order book ratio above 5 to 7 times.
- **Status:** RULE (method and rule of thumb). Date 2026-07-26.
- **Quote:** "order book business should be valued like order book businesses" (S211, DRONE 01:38:21)
- **Quote:** "discount the pipeline from 50% to 60% that much you will get the order" (S217, FUTURB 00:44:33)
- **Sources:** 4 (S145, S211, S217, S232).

### D15. Forward earnings over trailing; heavy capex means skip P/E
- **Rule:** use forward earnings for a company at an inflection or with disrupted plants; for a company with plant disruption and heavy capex do not use P/E, go two or three years forward and plug in numbers.
- **Status:** RULE. Dates 2026-07-14 (S005), 2026-07-26 (S136, S202), 2026-07-27 (S428).
- **Quote:** "it won't be 1 goes to 2, it will come 4 times in terms of profitability that type of scalability some of these companies could see so you have to think beyond evaluation TTM valuation" (S202, AEROA 01:05:56)
- **Sources:** 4 (S005, S136, S202, S428).

### D16. Re-rating needs earnings growth; P/E can fall even as profits rise
- **Rule:** abnormal top-line growth draws institutional buying and a P/E re-rating; later, P/E can compress even while profit grows.
- **Numbers (EXAMPLE, PERISHABLE):** P/E can go from 20 to 15 even with 25% profit growth (S484).
- **Status:** EXAMPLE. Dates 2026-07-27 (S427, S432, S484).
- **Quote:** "If the rate of change is accelerating, your P multiple could read it" (S432, TVGPF 00:28:57)
- **Sources:** 3 (S427, S432, S484).

### D17. Brokerage targets
- **Rule:** ignore stock targets from Wall Street, and treat target-price cuts as lagging indicators that follow a crash.
- **Status:** RULE. Dates 2026-07-27 (S070), 2026-07-28 (S001).
- **Quote:** "should simply ignore these stock targets entirely" (S070, MODULP 00:13:14)
- **Sources:** 2 (S001, S070).

### D18. Sum of the parts: a worked method, not a rule
- **Rule:** value each segment against its closest peer, then subtract from market cap to find what the market pays for the core. SRF's core came out at "almost 80 times EBIT" (S367, FLUORE 00:18:26), EXAMPLE, PERISHABLE.
- **Quote:** "I am just giving you hints of valuations so that you can do it yourself independently" (S126, WATCH 00:55:57)
- **Sources:** 3 (S126, S367, S413). Dates 2026-07-26.

---

## E. Technicals and timing (30-week average, RSI, relative strength, stages, entry and exit)

The course uses technicals for timing and exits, not for picking the business, and prefers the weekly chart for medium-term holders. Each entry below is the course's stated setting; none is a prediction.

### E1. Entry screen: weekly RSI at or above 50 and weekly ADX at or above 20
- **Rule:** a Stage 2 entry candidate shows weekly RSI crossing 50 and weekly ADX crossing 20. The worked screen in S474 adds price 5% above the 30-week EMA.
- **Number:** RSI 50 (one source also says 45 or 50); ADX 20; price 5% above the 30-week EMA.
- **Applies to:** the technical entry half of the screen.- **Status:** RULE (stated screen settings). Dates 2026-07-27 (S093, S095, S122, S455, S474, S488), 2026-07-28 (S001, S002).
- **Quote:** "The Relative Strength Index (RSI) acts as an additional entry confirmation, and it should ideally cross above 45 or 50" (S095, TECHNE 00:16:53)
- **Quote:** "Monitor the Average Directional Index to see when it crosses above the 20 level" (S093, HOWD 00:41:19)
- **Sources:** 8 (S001, S002, S093, S095, S122, S455, S474, S488).
- **Disagree:** S095 allows RSI to cross "45 or 50"; every other source states 50. S455 uses RSI crossing 50 on a weekly or monthly basis as a new-uptrend confirmation and a monthly RSI below 50 in a multi-year compounder as a possible multi-year top (S455, MASTEC 02:25:20).
- **Rule on momentum:** the worked analysis says momentum does not change a call made on other gates, because timing sequences a thesis and never originates one (S010, section 5, 2026-07-14).

### E2. The triple exit: 30-week EMA break, relative strength negative, V-Stop negative
- **Rule:** exit when price breaks below the 30-weekly EMA, relative strength turns negative, and the volatility stop turns negative, all together. Waiting for all three means accepting that 10% to 25% from the top is given up.
- **Number:** 30-weekly EMA; RS length 26 or 52 weeks; V-Stop based on average true range, length 10, multiplier 2 or 2.5; give-up of 10% to 25%.
- **Applies to:** primarily satellite holdings; core holdings follow business conviction (see E10).
- **Status:** RULE. Dates 2026-07-28 (S001), 2026-07-27 (S114).
- **Quote:** "10% to 25% from the top" (S001, FRAMEC 01:47:39)
- **Sources:** 2 state the triple together (S001, S114); the single legs are taught in S095, S122, S319, S329 and S332.
- **Related:** "30 weekly EMA do not forget it. If that 30 weekly EMA is breaking comprehensively with high volumes... that's a risk you must understand" (S329, HOTEL 01:59:45). For the V-Stop alone: "whenever weekly VSTOPs are turning positive then it means that it has entered into a positive territory whenever they turn negative it means it's gone" (S319, UNCOVC 00:51:39).

### E3. V-Stop settings: length 10, multiplier 2 to 3
- **Rule:** the volatility stop (V-Stop) uses average true range with length 10. The multiplier is tighter for expensive or cyclical names and wider for steady compounders.
- **Numbers (DISAGREE on what the number is set to):**
  - Weekly: length 10, multiplier 2 or 2.5 (S114, S001).
  - Weekly or monthly: length 10, multiplier 2 (S447).
  - Entry/exit page: length 10, multiplier 2.5 or 3 for structural compounders and 2 for cyclicals (S095).
  - Monthly chart: length 10 months; multiplier 2 when valuation is highly inflated, 2.5 for a steady compounder at a reasonable valuation, and 3 or 3.5 for investors with a 10 to 15 year horizon (S093).
- **Status:** RULE (settings). Dates 2026-07-27 (S093, S095, S114, S447), 2026-07-28 (S001).
- **Quote:** "To accommodate different business types, the multiplier is set to 2.5 or 3 for structural compounders, and 2 for cyclical stocks to ensure tighter risk control" (S095, TECHNB 01:31:23)
- **Sources:** 5 (S001, S093, S095, S114, S447).
- **Note:** the course treats the V-Stop as a lagging indicator that needs downside volatility to expand before it triggers (S093).

### E4. Time stop: 4 to 8 quarters
- **Rule:** if a fundamentally sound stock stays flat or corrects for a set time, exit on time. The investor picks 4 quarters (12 months), 6 quarters (18 months) or 8 quarters (24 months). One to two quarters is too short.
- **Number:** 4, 6 or 8 quarters.
- **Status:** RULE (the instructor's personal rule).
- **Quote:** "The instructor notes that 1 to 2 quarters is generally too brief, personally opting to use a rule of 4 to 8 quarters before triggering a sale" (S114, FRAMEC 01:30:47)
- **Sources:** 2 (S001, S114). Dates 2026-07-28, 2026-07-27.
- **Disagree:** for a stalled sector the instructor says "I have put a time stop loss of 6 to 9 months" (S202, AEROB 01:06:38, 2026-07-26). Separately S175 (2026-07-26) says to sit through the J-curve for "36 to 48 quarter" in his spoken phrasing, as quoted from the transcript; that phrasing is not reconciled with 4 to 8 quarters here.

### E5. Relative strength: length and the market-cap floor
- **Rule:** relative strength (RS) compares a stock to an index, and the course sets the lookback in weeks. A shorter lookback spots a trend change earlier.
- **Numbers (DISAGREE):** 26 or 52 weeks against the Nifty 50 or Nifty 500 (S114, S001); 13 weeks (a three-month window) or 26 weeks (five to six months), avoiding the default 52 (S103). Filter out companies below 1,000 crores of market cap (S103, S108, S464, S001 for the custom index, S498 screener).
- **Status:** RULE (settings). Dates 2026-07-27 (S103, S108, S114, S464, S498), 2026-07-28 (S001).
- **Quote:** "The default 52-week setting should be avoided because it lags and misses the earliest signs of strength" (S103, ADDITB 00:06:14)
- **Quote:** "filtering out companies with a market capitalization below 1,000 crores is recommended" (S103, ADDITB 00:35:34)
- **Sources:** 6 (S001, S103, S108, S114, S464, S498).

### E6. Relative strength is not RSI, and it leads
- **Rule:** RS and RSI are different measures. A stock up 10% while the index is up 20% has poor relative strength; a stock down 10% while the index falls 20% shows positive relative strength. RS turns first and the course says RS leaders outperform by about 20% in total returns.
- **Number:** 20% outperformance (instructor-cited); the Nifty long-term average is given as 12% to 14% (S121).
- **Status:** EXAMPLE (the 10/20 case); RULE (the 20%, cited source). Dates 2026-07-27.
- **Quote:** "stocks which have better relative strength outperform 20% in terms of total returns on an average" (S455, MASTEC 01:46:42)
- **Quote:** "different dimensions and different galaxies" (S104, ADDITB 00:23:51)
- **Sources:** 4 (S104, S121, S455, S103).
- **Limit:** "relative strength at market turns could be a bad idea" (S281, AROMA 01:42:52).

### E7. Extension and climax signals
- **Rule:** when price runs far above its averages the course tightens the exit.
- **Numbers:** more than 70% above the 30-weekly EMA in a parabolic rise: shift to a 10-weekly or 40-daily average (S114, S001); distance of the price above the 200-day EMA over 80% plus a volume spike is a climax signal (S001); a close of more than 5% on volume at least two times the average is an entry candle (S259); EPS rating above 80 (S259); a move of "60 to 80% within a week" is a climax warning (S259); RSI above 83 to 85 is peak momentum, a poor time for a new position or a fresh SIP tranche (S095); base counting: base number three or higher is riskier and 4 to 5 bases is prone to loss of EPS momentum (S001, S447).
- **Status:** RULE (settings and warnings). Dates 2026-07-27 (S095, S114, S259, S447), 2026-07-28 (S001).
- **Quote:** "the distance between 200 exponential moving average on daily charts with the stock price goes above 80%" (S001, CLASSC 02:39:21)
- **Quote:** "price close of more than 5% on a volume that is two times of the average minimum" (S259, CAPITC 00:51:04)
- **Sources:** 5 (S001, S095, S114, S259, S447).
- **Trade-off:** a shorter average "will give you earlier exits so it will also shake you out of stocks" (S319, UNCOVB 01:55:06).

### E8. Stage rules and the 10% to 15% discrepancy
- **Rule:** Stage 2 starts with a breakout above the 30-weekly average on high volume with a positive earnings surprise; Stage 4 comes with loss of EPS momentum. The turn from Stage 3 to Stage 4 is often clear only in hindsight, so exact-peak exits are impossible.
- **Number:** a 10% to 15% discrepancy from the top; a recent IPO lacking data for a 30-weekly EMA uses a 10-weekly or 21-weekly average (S114).
- **Status:** RULE. Dates 2026-07-28 (S001), 2026-07-27 (S114, S122, S431, S447, S464).
- **Quote:** "10 to 15% discrepancy" (S001, CLASSE 01:16:41)
- **Quote:** "If you are opening the daily chart, then the stock will go for 10-15% correction more often without hitting your stop loss on the weekly chart" (S259, CAPITC 00:35:35)
- **Sources:** 7 (S001, S095, S099, S114, S122, S431, S447). The 30-week average stands for about 150 days of price (S431).
- **Rule on sectors:** a sector index moving into Stage 2 tends to pull its stocks, "similar to how a mother cat moves forward and her kittens follow behind" (S001, SOICE3 00:05:20); leaders turn first: "Top performing stocks will lead the broader market, averages at important turning points" (S464, SOICE3 00:02:18). No sector stays in Stage 2 forever (S431).

### E9. Monthly system for compounders: ADX, Parabolic SAR and the V-Stop
- **Rule:** for medium-term holders the course uses a monthly chart. Buy when ADX crosses above 20 together with the Parabolic SAR beneath the candle; hold while the V-Stop is green; sell when it turns red. Pyramid only when the V-Stop stays green, ADX is above 20 and the SAR dots point up.
- **Number:** ADX 20; Parabolic SAR increment 0.05 and max value 0.2; V-Stop length 10; holding horizon two to four years.
- **Applies to:** structural compounders on monthly charts. Cyclicals use weekly averages (S107, "21 weekly EMA in 30 weeks", a phrase the note itself calls garbled).
- **Status:** RULE. Date 2026-07-27.
- **Quote:** "Pyramiding is authorized only when three conditions are met simultaneously: the VStop remains green, the ADX is above 20, and the Parabolic SAR dots begin pointing upwards" (S095, TECHNE 00:15:39)
- **Sources:** 3 (S093, S095, S107).

### E10. Where the technical exit applies
- **Rule:** use the technical exit system mainly for satellite stocks; core holdings follow business conviction.
- **Status:** RULE. Dates 2026-07-28 (S001), 2026-07-27 (S114).
- **Quote:** "recommended primarily for 'satellite PF stocks' rather than 'core holdings'" (S001, FRAMEC 01:56:49)
- **Sources:** 2 (S001, S114). A golden crossover is the 10-weekly EMA crossing over the 30-weekly EMA (S456).

### E11. Market breadth: share of stocks above the 200-day average
- **Rule:** use the share of stocks above their 200-day moving average as a deployment guide: very low is a lump-sum zone; very high is a time for care.
- **Numbers (DISAGREE):**
  - 16% to 17% marks bear bottoms; below 20% to 25% raise SIPs or deploy a lump sum; above 90% avoid large lump sums (S001, S478).
  - Below 20% is the lump-sum point and above 90% is greed; the instructor calls the lump-sum times ones that occur once in every two to three years (S471, S476).
  - Below 25% with the index above its own average is a lump-sum zone, below 20% is "juicy" (S147).
  - Above 60% to 70% is a bull phase, below 25% a bear phase (S488).
  - 50-day breadth reached about 15% near bear bottoms before rising above 70% (S155).
  - A rise from 17% to 63% signals broadening (S479, PERISHABLE).
- **Status:** RULE (stated signals) with "You can't time it to perfection" attached (S147, SOFT 00:37:20). PERISHABLE: the 16 to 17 percent reading in March 2026.
- **Quote:** "very good lump sum times which get created once in every two to three years" (S476, SOICD2 00:29:49)
- **Quote:** "goes above 60-70% this is bull market phase" (S488, SOICB4 00:27:18)
- **Sources:** 7 (S001, S147, S155, S471, S476, S478, S488).

### E12. Time corrections and post-IPO phases
- **Rule:** time corrections end when earnings catch up or enough sideways time pulls the P/E down. A post-IPO stock typically struggles, then goes sideways, then trends.
- **Numbers:** time corrections ran 175 to 177 weeks (2011 to 2013) or 19 to 20 months (S001, S477). Post-IPO: first 3 to 4 quarters weak, a bombed-out phase of 15 to 24 months, then 9 to 12 months of bottoming; earnings downgrade cycles of 4 to 8 quarters, sometimes up to 4 years (S507). A beaten-down sector: wait until it is up about 10% to 15% from the lows and the narrative has changed (S466). Accumulation takes 6 to 12 months (S281).
- **Status:** RULE (stated as a pattern, not a hard rule, in S507) and EXAMPLE. Dates 2026-07-27 (S466, S477, S507), 2026-07-26 (S281), 2026-07-28 (S001).
- **Quote:** "typical earnings downgrade cycles might last 4 to 8 quarters, they can sometimes stretch for multiple years (even up to 4 years) before reversing" (S507, FRAMEA 00:39:41)
- **Quote:** "up 10 to 15% from the lows" (S466, SOICE5 00:52:40)
- **Sources:** 5 (S001, S281, S466, S477, S507).

### E13. Smart-money and promoter signals
- **Rule:** FII plus DII together raising their stake by 2 percentage points or more is a screen input; promoters taking part in a warrant issue is a favourable sign; a warrant locks the price and converts within 18 months. Do not follow FII and DII blindly.
- **Numbers:** 2 percentage points; the course's own backtest found only 25 of 54 businesses outperformed, about a coin flip (S001 F33); a promoter-holding change scan of more than 1% or 2% (S123); 18 months (S155, S467).
- **Status:** RULE (screen); EXAMPLE (the backtest).
- **Quote:** "FII's plus DI's cumulatively increasing their stake by 2%" (S467, SOICE3 01:00:14)
- **Quote:** "who is participating in the warrant issue, if the promoters are participating, that is very good" (S467, SOICE3 00:28:17)
- **Sources:** 5 (S001, S123, S155, S164, S467). Dates 2026-07-27, 2026-07-26.

### E14. The system is wrong 20% to 30% of the time
- **Rule:** expect to be wrong 20% to 30% of the time even on a stock that clears every item; sell quickly when trends fail.
- **Status:** RULE (stated expectation). Date 2026-07-27.
- **Quote:** "wrong 20% to 30% of the time" (S455, MASTED 02:09:54)
- **Quote:** "20-30% of the times" (S456, MASTED 02:09:54)
- **Sources:** 2 (S455, S456).

### E15. Small-cap graduation
- **Rule:** moving across about 10,000 crore of market cap changes who owns the stock. Mid-caps of 8,000 to 30,000 crore get institutional money.
- **Number:** 10,000 crore; 8,000 to 30,000 crore.
- **Status:** RULE (stated threshold). Dates 2026-07-27 (S484), 2026-07-28 (S001 F37).
- **Quote:** "cross the 10, 000 crore threshold and ecosystem changes completely" (S484, SOICE6 00:07:37)
- **Sources:** 2 (S001, S484).

### E16. Commodity and macro levels (PERISHABLE, lecture-date)
- **Rule:** dated levels, not bars. Gold: if the weekly RSI holds 50 the trend is fine, with support at 4,524 dollars. Crude could return to 60 to 70 dollars on a US and Iran deal (conditional). Nifty 50 at 19 times earnings after two years of consolidation. The US 10-year at 4.6%. A rupee falling much faster than its normal 4.1% to 4.5% a year has coincided with weak Nifty returns.
- **Status:** EXAMPLE, PERISHABLE. Dates 2026-07-26 (S142, S146), 2026-07-27 (S471, S478).
- **Quote:** "This 4524 dollars is a very strong support level for gold at the moment" (S146, SOFT 01:30:21)
- **Sources:** 4 (S142, S146, S471, S478).

---

## F. Position sizing and portfolio

### F1. The 2/4/6/8 sizing family
- **Rule:** weight each stock by conviction in a small set of fixed percentages. The "268" strategy gives satellite stocks 2% and high-conviction core stocks 6% or 8%. The "2468" version gives topsy-turvy models 2% or less, medium-conviction ideas 4% to 6%, and the top ideas an 8% allocation at cost basis.
- **Number:** 2, 4, 6 and 8 percent; variants 3, 6 and 9, and 3, 6, 9 and 12 ("36912"). Core sizes 4, 6 or 8% and unproven names 2% (S505). Start experimental ideas at 2% and raise to 4% or 5% when the thesis shows in numbers (S502).
- **Status:** RULE (sizing template). Weights are set at original cost; if a price move inflates a position, rebalance it back down (S090).
- **Quote:** "satellite stocks receive a strict 2% allocation, while high-conviction core stocks receive either 6% or 8% allocations" (S090, HOWI 00:00:26)
- **Quote:** "getting shown into numbers" (S502, INSIGM 01:08:28)
- **Sources:** 6 (S001, S015, S017, S090, S502, S505). Dates 2026-07-27, 2026-07-28 (S001).
- **Limit:** S015 and S017 teach only the name, "two four six eight percentage approach"; S017 notes that the criteria for choosing a 2% over an 8% weight are never explained in that lecture.

### F2. Core and satellite caps
- **Rule:** split the portfolio into a core and a satellite. The satellite holds fragile, new or not-yet-understood businesses and cyclical names; the core holds companies with a track record, high return on capital and a clear runway.
- **Number:** satellite at most 10% of the portfolio, 20% for aggressive investors; core 80% to 90%; individual satellite stocks 2% to 3%; core stocks 6% to 8%.
- **Status:** RULE. Date 2026-07-27.
- **Quote:** "Cap the total weight of the satellite portfolio at a 10% maximum, though aggressive investors can extend this ceiling to 20%" (S090, HOWI 00:04:19)
- **Quote:** "individual satellite stocks should be capped at around 2% to 3% each" (S096, TECHNK 01:59:34)
- **Sources:** 2 (S090, S096).
- **Deviation:** the instructor discloses a personal "over concentration" of 35% in one business, "drastically violating" the standard framework (S090, HOWD 02:25:23). Treat as a recorded exception, not a rule.

### F3. Equal weight and the number of holdings
- **Rule:** equal weights are an accepted template: 4% each across 25 stocks or 5% across 20, rebalanced every six months. Diversification benefit plateaus around 20 to 30 names.
- **Numbers (DISAGREE on the count):**
  - 10, 15 or 20 solid companies (S022).
  - A minimum of 10 and a maximum of 15 to 25; 70 to 80 stocks dilute winners (S096).
  - 15 to 17 or 15 to 20 stocks (S353).
  - 20 to 30 stocks (S177 for licence-based businesses; S502; S001 F40 "plateaus around 20 to 30").
  - A 20-stock portfolio will have two-stock losses, and that is structural (S006).
  - Other templates in S001 F40: 10% times 10 names; 20% times a handful.
- **Status:** RULE (practice, "not a formula" in S353).
- **Quote:** "A portfolio should contain a minimum of 10 and a maximum of 15 to 25 stocks" (S096, TECHNK 01:55:40)
- **Quote:** "you should make a portfolio of 20 to 30 stocks. Because in India you are very concentrated investing" (S177, MOATA 01:05:00)
- **Sources:** 7 (S001, S006, S022, S096, S177, S353, S502). Dates 2026-07-26 to 2026-07-28.

### F4. Sizing arithmetic
- **Rule:** small weights cap the damage of a wrong pick; large weights let winners count.
- **Numbers:** a 2% position falling 70% costs 1.4% of the portfolio; an 8% position rising 400% adds 32%; a 50% drawdown in a 10% position costs 5% of the portfolio and in a 20% position costs 10% (S001 F40); a 6% to 8% core position that becomes a multi-bagger gives a 4% to 5% impact on the portfolio (S096).
- **Status:** EXAMPLE (arithmetic).
- **Quote:** "if a 2% allocation plummets by 70%, the overall negative impact on the entire portfolio is a heavily mitigated 1.4%" (S090, HOWI 00:01:34)
- **Sources:** 3 (S001, S090, S096). Date 2026-07-27.

### F5. Drawdown arithmetic and the first rule
- **Rule:** the first rule is to not lose money, because recovery from a loss needs a larger gain.
- **Numbers:** a 10% fall needs an 11% gain, 25% needs 33%, 50% needs 100%, 75% needs 300%, 90% needs 900%. Moderate compounders (15% to 18%) and fast compounders (30% to 35%) both work over two decades if severe drawdowns are avoided. The Sensex grew about 500 times over 31 to 32 years at a CAGR of just 15% to 16% (S024); Buffett earned a 27,44,062% absolute return from 1965 to 2019 at 20% CAGR (S023).
- **Status:** RULE (arithmetic) and EXAMPLE (the cases).
- **Quote:** "do not lose money" (S020, MODULB 00:11:49)
- **Sources:** 4 (S020, S021, S023, S024). Date 2026-07-27.

### F6. Hard cap on policy-dependent businesses
- **Rule:** the instructor will not put 20% to 30% in a business that depends on policy. Position size is the main defence against regulatory risk.
- **Number:** "20-30%" is the size he will not take.
- **Status:** RULE (personal cap). Dates 2026-07-14 (S005, S006), 2026-07-28 (S229).
- **Quote:** "I cannot put 20-30% in such a business" (S006, SBQA L150-158)
- **Sources:** 3 (S005, S006, S229).

### F7. Portfolio mix: trending sectors, valuation-comfort sectors and reversals
- **Rule:** the instructor's own mix is mostly sectors that are trending, with a smaller share in valuation-comfort sectors. Reversals double in about 18 months and tailwind names double in about 3 years.
- **Numbers (DISAGREE):** 65% to 70% in trending sectors and 25% to 30% in valuation-comfort sectors (S150); 60% to 70% in the tailwind slice and roughly 25% to 30% in valuation-comfort sectors (S149).
- **Status:** EXAMPLE (his own mix, not a rule). Date 2026-07-26.
- **Quote:** "65 to 70 percentage of the portfolio will be with the sectors which are trending in the market" (S150, SOFT 01:01:17)
- **Quote:** "sectors where there will be a lot of valuation comfort" (S149, SOFT 01:02:16)
- **Sources:** 3 (S149, S150, S160). S149 adds: "I'm not saying don't do momentum, do momentum, but do it in a good business model" (S149, SOFT 01:02:52).

### F8. Expect errors and judge at portfolio level
- **Rule:** with 15 to 20 stocks, expect some to be wrong, and measure at the portfolio level, not stock by stock.
- **Numbers:** "100% 4-5 stocks are wrong" and "20-25% are wrong" (S353); in a falling market a portfolio down 5% to 10% while small caps fall 10% to 20% is a good return; in a rising market the bar is to beat the index (S180).
- **Status:** EXAMPLE (the instructor's expectations).
- **Quote:** "100% 4-5 stocks are wrong" (S353, SOICD 00:41:29)
- **Quote:** "If the index is falling like 10-20% in small cap space and you are falling like 5-10% that's a good return." (S180, MOATB 01:14:32)
- **Sources:** 3 (S180, S353, S437). Dates 2026-07-26, 2026-07-27.

### F9. Stock attribution: theme, liquidity, stock picking
- **Rule:** the course apportions a stock's move to the theme, to liquidity and to the pick. It also says about 60% of a stock's return relies on its sector.
- **Number:** 60% theme, 20% liquidity, 20% stock picking.
- **Status:** RULE (stated by the instructor as attribution). Date 2026-07-27.
- **Quote:** "60% of a stock's move is attributable to the theme, 20% is attributable to the liquidity and last 20% is attributable to your stock picking" (S494, SOICC 00:03:05)
- **Quote:** "Roughly 60 percent of a stock's return relies entirely on its underlying sector performing well" (S448, CLASSF 00:07:45)
- **Sources:** 3 (S444, S448, S494).

### F10. Holding periods
- **Rule:** the course states time horizons by type of business, not one holding period.
- **Numbers:** minimum horizon three years, expecting profits to double (S022); core stocks with a clear runway over three to four years (S090); CDMO thesis 3 to 5 years (S175, S168); complex-API 3 to 4 years (S399); CDMO judged over two to three years (S402); a structural mix change two to four years, "doesn't happen in 1-2 quarters" (S110); airports, ports and shipbuilders with operating-leverage-led growth stay put with a technical entry and exit framework (S211); quality investors 10 to 20 years (S096); ultra long-term investors 10 to 15 years (S093).
- **Status:** RULE for stated horizons; EXAMPLE for company cases.
- **Quote:** "In CDMO businesses, you see 3 to 5 years horizon. This is not a 1 to 2 year business." (S175, MOATB 00:01:07)
- **Sources:** 9 (S022, S090, S093, S096, S110, S168, S175, S399, S402). Dates 2026-07-26 and 2026-07-27.

---

## G. Capital cycle and capacity (utilisation, capex to sales)

The course reads capex as a cycle: capacity is built ahead of demand, margins follow utilisation, and supply catches up. It gives few hard thresholds; the numbers below are the ones it states.

### G1. CWIP and the capex that is about to start earning
- **Rule:** a high ratio of capital work in progress to existing fixed assets signals that a large amount of capex is nearly finished and about to become operational. The market often rewards this with higher valuations ahead of the growth. CWIP cannot be depreciated while the asset is under construction.
- **Number:** no threshold stated. Entry at 30% to 40% capacity utilisation is the "de-risked" pre-opex entry; the other school buys at the worst pre-opex quarters (S112).
- **Applies to:** non-lenders.
- **Status:** RULE (general reading). Dates 2026-07-27 (S034, S112).
- **Quote:** "huge jump in revenues" (S034, MODULD 00:17:09)
- **Sources:** 2 (S034, S112).

### G2. Pre-engineered buildings (PEB): usable capacity is 80% to 85%
- **Rule:** in PEB, a plant never runs at 100%; because every project is custom, the usable level is 80% to 85%, and utilisation tops out there. Both sources (S288, S504) state this for PEB plants only. The course does not state a usable-capacity ceiling for other kinds of plant.
- **Number:** 80% to 85% for PEB. Rough capacity to revenue: about 3 times tons to crores (the instructor's own warning attached).
- **Status:** RULE for the 80% to 85% in PEB (two sources), EXAMPLE for the 3x metric. Dates 2026-07-26 (S288), 2026-07-27 (S504).
- **Quote:** "every plant is like a project in itself. So you can never utilize a capacity of 100%" (S288, PEB 00:29:05)
- **Quote:** "Just a rough metric might not be completely right. But roughly we can assume right" (S288, PEB 01:04:59)
- **Sources:** 2 (S288, S504).

### G3. Where operating leverage kicks in on utilisation
- **Rule:** operating leverage works as fixed costs spread over more volume.
- **Numbers:** in hotels, real operating leverage kicks in as occupancy goes from 65% to 67% up to 78% to 80% or 85% (S330); at peak utilisation cash flow exceeds reported profit because depreciation is non-cash (S449); gross margin of about 55% with full utilisation gives about 25% operating margin in the CDMO worked case (S170, PERISHABLE).
- **Status:** EXAMPLE. Dates 2026-07-26 (S170, S330), 2026-07-27 (S449).
- **Quote:** "real operating leverage kicks in when you go from 65-67% occupancy to 78-80% or even 85%" (S330, HOTEL 00:40:00)
- **Sources:** 3 (S170, S330, S449).

### G4. Operating-leverage arithmetic
- **Rule:** with a big fixed-cost base, a modest sales rise lifts profit by more. Without margin expansion, bottom line growth equals top line growth.
- **Numbers (EXAMPLE, PERISHABLE):** revenue up 13% leading to EBITDA up 20% (hotels, S006, S294); in an upcycle revenue up 40% to 50% with bottom line up 70% to 90% (S257).
- **Status:** EXAMPLE.
- **Quote:** "if they've grown their revenues by 13%, it leads to 20% growth in EBITDA" (S006, TURN L206-209)
- **Quote:** "your top line growth will be your bottom line growth" (S011, PIPE 00:30:39)
- **Sources:** 4 (S006, S011, S257, S294). Dates 2026-07-14, 2026-07-26, 2026-07-28.

### G5. Time from capex to numbers
- **Rule:** capacity is built ahead of demand and takes time to show.
- **Numbers:** capacity built about 18 months in advance; a pain period of 6 to 12 months before it turns into numbers (S489); first growth after 18 to 24 months (S260); CDMO capex payoff in about 27 to 28, with early cost hits (S171, PERISHABLE); hospital capex splits equipment 30% to 40% and land and building 35% to 40% (S351); the instructor found hospital capex 70% to 80% correlated with stock returns (S351, his own estimate, PERISHABLE).
- **Status:** EXAMPLE and RULE of thumb. Dates 2026-07-26 (S171, S260, S351), 2026-07-27 (S489).
- **Quote:** "will probably take 6 to 12 months before that it turns into numbers" (S489, SOICB3 00:23:31)
- **Quote:** "show growth after 18 to 24 months" (S260, CAPITA 00:44:22)
- **Sources:** 4 (S171, S260, S351, S489).

### G6. Capital cycles: supply catches up
- **Rule:** abnormal margins attract capacity; when supply catches up, margins fall. Study the industry when it is in a margin contraction cycle, not an expansion.
- **Numbers:** only 25% of winners from one bull market lead in the next cycle (S427); each up-cycle crossed the prior peak by at least 15% to 17% and cycles ran every 3 to 4 years before 2018 (S190, commercial vehicles); packaging runs about three years of suppressed margins then two to three years of expansion, with demand doubling in 6 to 7 years while supply can double quickly (S305); hotels' up or down cycles last at least 3 to 5 years (S326); a transformer down cycle ran 13 years after 2008 (S303); act within 12 to 18 months of a contraction beginning (S241).
- **Status:** RULE (the contraction timing) and EXAMPLE (cycle lengths, sector-specific, PERISHABLE).
- **Quote:** "you have to look at this industry when it goes through a margin contraction cycle, not when it is going through an expansion cycle" (S241, PREMA 01:04:45)
- **Quote:** "only 25% of the winners from one bull market manage to lead in the next cycle" (S427, TVGPA 00:02:50)
- **Sources:** 6 (S190, S241, S303, S305, S326, S427). Dates 2026-07-26, 2026-07-27, 2026-07-28.
- **Related:** model long-term average margins in valuation (S087, see D6).

### G7. Order-book timing
- **Rule:** an order book is not the same as earnings; check how fast it is executed and whether it recurs.
- **Numbers:** long-dated order books run 12 to 18 months, short-dated 8 to 12 months (S501); defence electronics or rail electrification six to twelve months, road corridors three to four years, shipbuilding seven to ten years (S232); PEB execution 8 to 12 months, now 8 to 9 months for large orders (S289); a ratio of order book to revenue above five to seven times (S217); an order book multiplying 3 to 4 times is a convexity example (S110).
- **Rule on regime:** not to be long-term in a down cycle in an order-book business, and to exit near peak execution (S006, S232, S501).
- **Status:** RULE for the regime statements; EXAMPLE for the timings.
- **Quote:** "You can't be long term in a down cycle in an order book driven business" (S232, IDENTA 01:34:39)
- **Quote:** "now suddenly it has come down to 8 to 9 months for most of the large orders" (S289, PEB 00:44:39)
- **Sources:** 7 (S006, S110, S217, S232, S289, S501, S511). Dates 2026-07-14, 2026-07-26, 2026-07-27, 2026-07-28.

### G8. Qualification and gestation times (barriers to a new entrant)
- **Rule:** long approval and qualification times are what make a supplier moat. The numbers differ by industry.
- **Numbers (stated, mostly PERISHABLE):** nuclear vendor qualification 8 to 10 years (S154, S480); atomic approval alone three to four years (S163, S481); BHEL, NTPC or oil and gas approvals two to four years, leaving three to five vendors per project (S162); tier 1 aerospace 3 to 5 years (S202) and 5 to 10 years to build aerospace-grade capability (S200); naval type approval about five years (S215); a new-supplier gestation of five to eight years (S205); a customer takes 9 to 12 months to qualify battery chemicals (S136); switching a supplier takes 18 to 24 months (S404); a new agrochemical registration takes four to five years (S344); a new chemical approval cycle "sometimes takes 10-10 years" as transcribed (S279); Fine Organics takes 3 to 5 years to win one customer (S419).
- **Status:** EXAMPLE and instructor statements; sector-specific.
- **Quote:** "Capability is high and entry barriers are due to lengthy qualification cycles, 3 to 5 years for a tier 1 status it takes" (S202, AEROB 00:41:03)
- **Quote:** "actually takes 18 to 24 24 months to actually switch a supplier from validation to commercialization" (S404, APID 00:08:43)
- **Sources:** 14 (S136, S154, S162, S163, S200, S202, S205, S215, S279, S344, S404, S419, S480, S481).
- **Disagree:** nuclear approval is 8 to 10 years for vendor qualification in S154 and S480, and three to four years for atomic approval alone in S163 and S481. They are different steps.

### G9. M&A and capital allocation
- **Rule:** an acquisition should be smaller than the core, self-financed or with debt that is not over the roof, at a reasonable multiple, and integrated over 18 to 24 months. Return ratios stay depressed after an acquisition, and 90% of M&A fail.
- **Number:** 18 to 24 months; 90% fail. A dip in margin is expected after an acquisition, then recovery (S227).
- **Status:** RULE (blueprint) and instructor statement.
- **Quote:** "size of the acquired entity not larger than the core entity" (S500, INSIGA 00:20:05)
- **Quote:** "self-financed or debt not over the roof" (S500, INSIGA 00:20:05)
- **Sources:** 3 (S008, S227, S500). Dates 2026-07-14, 2026-07-27, 2026-07-28.

---

## H. Sector-specific bars

Every figure here is a lecture-date snapshot, an instructor estimate or a company example. PERISHABLE throughout unless marked RULE. Read the sector's own lecture before using any of them.

### H1. Hotels
- **Numbers:** net debt to EBITDA guided at 4x to 4.5x in a turnaround (S296, S006); average occupancy 67% to 68% (S328); Q3 and Q4 carry 70% to 75% of annual EBITDA (S328); sustainable price hikes 7% to 8%, a 20% to 25% hike risks customers leaving (S330); build time about four years (S328); branded supply growth 5% to 6% against demand 8% to 10% (S326); multiples at the lecture date: Indian Hotels 22.6x, Shalye 17.4x, Oberoi/EIH 14x to 15x, Lemon Tree 15x EV/EBITDA (S329). Preferred return metric is ROE, with ROC adjusted for lease expense (S329).
- **Status:** EXAMPLE, PERISHABLE. Date 2026-07-26 (S296 is 2026-07-28).
- **Quote:** "the highest you are getting in the sector is the Indian hotels, 22.6 times" (S329, HOTEL 01:49:48)
- **Sources:** 6 (S006, S296, S326, S328, S329, S330).

### H2. Hospitals
- **Numbers:** EV/EBITDA above 30x expensive, below 20x cheaper (S446); capex split equipment 30% to 40%, land and building 35% to 40% (S351); health spend about 3.5% of GDP and sector growth 15% to 17% (S352); Aster ROC 8% to 10% and a "value trap" without capex cuts or a demerger (S350). Course exit view: when hospitals run out of land and restart greenfield spending, the sector's cycle is late (S351).
- **Status:** EXAMPLE, PERISHABLE. Dates 2026-07-26 (S350, S351, S352), 2026-07-27 (S446).
- **Quote:** "cheap for a reason" (S350, SOICC 00:52:45)
- **Sources:** 4 (S350, S351, S352, S446).

### H3. Pharma, API and CDMO
- **Numbers:** Phase 3 approval chance 80% to 85% and a patent life of 10 to 15 years with royalty at 95% to 99% gross margin (S302); Para IV exclusivity window 6 to 8 months (S302); generic API top players reach gross margin 70% (S406); API is 6% to 10% of the final formulation cost (S251); Laurus gross margin above 55%, Hikal gross margin 55% to 58% and operating margin 19%, Neuland guided from 15% to 25% (S168, S170). Judge a CDMO over two to three years.
- **Status:** EXAMPLE, PERISHABLE (company guidance); RULE for the 2 to 3 year judging window. Dates 2026-07-26 (S168, S170, S251, S402, S406), 2026-07-28 (S302).
- **Quote:** "quarter on quarter variation is a game which is played by analysts" (S402, APIF 00:05:12)
- **Sources:** 6 (S168, S170, S251, S302, S402, S406).
- **Disagree:** the Para IV window is "for 6 months no one came because of Para4" (S148, SOFT 01:20:22) against 6 to 8 months (S302).

### H4. Agrochemicals
- **Numbers:** 27 products scheduled for ban, a domestic market of about 12,000 cr (S008, S341); insecticides 50% to 60% of sales and only about 40% of farmland irrigated (S341); 9(3) registration gives 3 years of data exclusivity (S005, S346); registration takes four to five years and costs 100,000 to 5 million euros per molecule (S344); a spot-selling exporter trades at commodity multiples until even 15% to 20% of business shifts to regulated markets (S345); PI Industries inventory 69 to 80 days against Anupam about 250 to 260 working capital days (S348).
- **Status:** EXAMPLE, PERISHABLE. Dates 2026-07-14 (S005, S008), 2026-07-26 (S341 to S348).
- **Quote:** "for 3 years you get exclusivity" (S346, AGROCA 00:20:14)
- **Sources:** 6 (S005, S008, S341, S344, S345, S346).

### H5. Specialty, commodity and aroma chemicals
- **Numbers:** EBITDA ladder: refrigerant gases 18% to 22%, CRAMS 28% to 30% (S363); phenol spread at a 10-to-11-year low took basic margins to about 5% (S252); Alkyl Amines margin from 18% to almost 33% in a spike (S420); flavours and fragrances gross margin 58% to 59% (S282); Privi and Manorama sustainable EBITDA 23% to 27% (S176); a four-company group holds 60% to 70% of the world flavour and fragrance market (S279).
- **Status:** EXAMPLE, PERISHABLE. Dates 2026-07-26 (S176, S279, S282, S363, S420), 2026-07-28 (S252).
- **Quote:** "18 to 22% types of EBITDA margins" (S363, FLUORC 00:05:00)
- **Sources:** 6 (S176, S252, S279, S282, S363, S420).

### H6. Steel, pipes and metals
- **Numbers:** Tata Steel domestic EBITDA per ton 16,000 to 17,016 rupees (S317); stainless EBITDA per ton above 20,000 to 21,000 rupees (S183); seamless and SAW pipes for oil and gas trade at P/E "10, 12, 13 times, not more than that", ERW building pipes 40x to 50x, converters 24x to 50x, a normalised multiple of 22x to 25x for over-earning pipe businesses (S320, S321); iron ore auction winners paid an average premium of 129% (S318).
- **Status:** EXAMPLE, PERISHABLE. Date 2026-07-26.
- **Quote:** "P multiple of 10, 12, 13 times, not more than that" (S321, UNCOVB 00:20:25)
- **Sources:** 5 (S183, S317, S318, S320, S321).

### H7. Alcohol and premiumisation
- **Numbers:** start serious study once prestige-and-above mix crosses 15% to 20% (S237); the proprietary-brand story gets interesting at 25% to 30% share, up from 13% (S220); super premium above Rs. 3,500 is 1% to 2% of the industry and 21% of profit, while regular and popular are 52% of industry and 19% of profit (S223); scotch duty cut from 150% to 75% worth 2% to 3% of margin (S236); a per-capita income of $2,300 as the premiumisation trigger (S246); Radico at 101x and United Spirits at 60x to 80x for a decade (S220, S236).
- **Status:** RULE of thumb (15% to 20%); EXAMPLE and PERISHABLE (the rest). Date 2026-07-26.
- **Quote:** "The moment it crosses 15-20% then you should start studying that company seriously" (S237, PREMA 00:42:37)
- **Sources:** 5 (S220, S223, S236, S237, S246).

### H8. Commercial vehicles, autos and ancillaries
- **Numbers:** each commercial-vehicle up-cycle crossed the previous peak volume by at least 15% to 17%, cycles ran every 3 to 4 years, and the 2018 axle-load revision of 20% to 25% extended the down-cycle (S190); a leaf-spring leader holds 62% to 65% of M&HCV (S193); SUVs rose from 7% to 52% of car sales (S240); Uno Minda grew 18% to 20% while its sector grew 1% to 2% (S483); a supplier's growth ceiling is its customer's growth (S239).
- **Status:** EXAMPLE, PERISHABLE. Dates 2026-07-26, 2026-07-27 (S483).
- **Quote:** "every upcycle as made sure that previous upcycle volumes are at least crossed by 15 to 17%" (S190, CV 00:15:41)
- **Sources:** 5 (S190, S193, S239, S240, S483).

### H9. Aerospace, defence, shipping and drones
- **Numbers:** India's commercial fleet projected to grow 13% to 15% a year (S200); India's MRO market $1.7 billion growing 9% a year to $4 billion by 2031, with 80% to 85% of the work done overseas (S300); the top 10 aerostructure suppliers hold 44% (S205, garbled in the transcript); ADS EBITDA 25% to 30% against auto-ICE 15% to 17%, and lifting ADS from 5% to 20% of revenue adds about 3 to 4 points of margin (S199); counter-drone market growing 27% against 10% for drones (S207); a diving support vessel earns $80,000 a day against $55,000 in 2015 (S214).
- **Status:** EXAMPLE, PERISHABLE. Dates 2026-07-26, 2026-07-28 (S300).
- **Quote:** "India's total commercial fleet is projected to grow at 13-15% per annum" (S200, AEROA 00:50:19)
- **Sources:** 6 (S199, S200, S205, S207, S214, S300).

### H10. Nuclear and power equipment
- **Numbers:** plant load factor: nuclear 80% to 92%, coal 50% to 60%, solar 18% to 22% (S156); capex shares: reactor island 25% to 30%, civil 20% to 25%, balance of plant and I&C 16% to 24% (S157); nuclear is a "double digit or a mid-teens contribution at best" even for top suppliers (S158); nuclear is 5% to 6% of BHEL's order book with a ceiling of 10% to 11% (S158); Russia holds about 40% of global enrichment capacity (S152).
- **Status:** EXAMPLE, PERISHABLE. Date 2026-07-26.
- **Quote:** "this number is between 80-92% because it is continuous in nature it is more continuous source of power" (S156, NUKE 00:31:26)
- **Sources:** 4 (S152, S156, S157, S158).
- **Disagree (BHEL order book):** 2.3 lakh crore (S154, S158) against 1.8 lakh crore, "their lifetime high order book", in S162 (2026-07-26). The sources do not reconcile them; do not merge.

### H11. Oil and gas
- **Numbers:** rising crude helps explorers and falling crude helps refiners (S309); US shale is not profitable below $40 (S313); 2030 scenarios as stated: base $80, high $95, low $55 to $60 (S313); the median return on capital employed for oil companies is 10% (S315); declining rig utilisation and a falling rig count are bearish (S314); an ONGC reserve replacement ratio above 1.0 for 18 years (S315).
- **Status:** EXAMPLE, PERISHABLE. Date 2026-07-26.
- **Quote:** "most of the companies return on capital employed are 10% median" (S315, OILA 00:21:40)
- **Sources:** 4 (S309, S313, S314, S315).

### H12. Pre-engineered buildings, packaging and textiles
- **Numbers:** PEB organised players earn 10% to 11% margins and the sector band is 8% to 11% (S289, S290); the top six players hold 80% to 85% of the organised market (S290); PEB utilisation tops out at 80% to 85% (S504); packaging EBITDA 18% to 24% can crash in glut years and the baseline is 16% to 20% (S305); cotton is bought 6 to 9 months in advance (S306).
- **Status:** EXAMPLE, PERISHABLE. Dates 2026-07-26 (S289, S290), 2026-07-28 (S305, S306), 2026-07-27 (S504).
- **Quote:** "minimum 8 to 11 percent margin band" (S289, PEB 00:28:58)
- **Sources:** 5 (S289, S290, S305, S306, S504).

---

## I. Where the sources disagree, in one place

- **CFO to EBITDA or PAT:** 70/60 on EBITDA (S001, S036, S050) against 70/60 on PAT (S045); CFO to PAT 80% to 90% (S001, S470), 60% to 70% for B2B (S452), above 90% to 95% (S494). See A8, A9.
- **P/E lines:** 15 to 35 (compiled lists S001, S002, S010 only), 15 to 30 (S454), below 50 or 40 (S515), below 25 (S498). See D1.
- **Discount rate:** 8% to 10% (S084), about 10% (S061), 10% to 12% domestic and 6% foreign (S443), 12% or higher (S053). See D9.
- **V-Stop multiplier:** 2 or 2.5 (S114), 2 (S447), 2.5 or 3 for compounders and 2 for cyclicals (S095), 2 to 3.5 by horizon (S093). See E3.
- **RS length:** 26 or 52 weeks (S114) against 13 or 26, avoiding 52 (S103). See E5.
- **Time stop:** 4 to 8 quarters (S114) against 6 to 9 months (S202). See E4.
- **Breadth:** below 20% (S471, S476), below 20% to 25% (S001, S478), below 25% (S147, S488). See E11.
- **Number of holdings:** 10 to 20 (S022), 15 to 25 (S096), 15 to 20 (S353), 20 to 30 (S177, S502). See F3.
- **Mix:** 65% to 70% trending (S150) against 60% to 70% tailwind (S149). See F7.
- **Operating leverage line:** 20 in the compiled rule set (S002) against 15 to 20 in the lecture (S289). This is the compiled list against the lecture, not the course disagreeing with itself. See A2.
- **Data-center ROE:** 10% to 12% against 6% to 10% inside S248. See C5.
- **BHEL order book:** 2.3 lakh crore (S158) against 1.8 lakh crore (S162). See H10.

---

## J. The course does not state a number for

For each item below the course gives a method or a direction, or says nothing. Where it names the concern without a figure, the entry says so. None of these is filled from outside the course.

- **A promoter pledge percentage that is too high.** Pledging is named a "huge red flag" with no cut (S470).
- **A stop-loss percentage from the entry price.** Exits run on the 30-weekly average, relative strength, the V-Stop, a swing low and a time stop, never a fixed percent loss (S001, S114, S259).
- **A delivery-volume rule.** Not in the course text.
- **An interest-coverage minimum.** Mentioned only as "a high interest coverage ratio" for one oil company (S315).
- **A current-ratio, dividend-payout, dividend-yield or Altman-style bar.** Not stated.
- **A maximum or minimum promoter holding for a good company.** Only the weak-incentive example of 2% to 7% after ESOPs (S434).
- **A margin-of-safety percentage.** The course names the idea and a few multiples, never a discount to value (D11).
- **A universal exit P/E or required return.** Exit P/E is a manual input and the discount rate is subjective (S042, S443).
- **A receivable-days, inventory-days or payable-days bar.** Peer comparison and trend only (S036, S057), apart from the 180-day flag (B4).
- **A debt-to-EBITDA bar for companies in general.** Only hotel guidance of 4x to 4.5x (S296) and the D/E lines in A7.
- **A general operating-margin or net-margin bar.** Only sector baselines (C3) and the scan settings (A4).
- **A debt-to-equity bar for lenders.** Leverage of 14x to 16x is described, not capped (S332).
- **A cap per sector or per theme.** Only the hard cap on policy-dependent names (F6) and the satellite caps (F2).
- **A fixed holding period for a core stock.** Horizons are by business type (F10).
- **A free-float minimum or a liquidity floor beyond the 1,000 crore market-cap filter** (E5).
- **A buy or sell price for any stock.** The sessions "do not give buy/sell recommendations or target prices, only the method" (S514).
- **A rule for when a bubble has formed.** The course says do not call it without study: "Just to say something is a bubble without reading it for the last 2-3 years is not the right frame of mind I believe." (S180, MOATB 01:08:43)
