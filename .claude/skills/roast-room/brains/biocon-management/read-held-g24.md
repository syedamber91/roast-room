# read-held g24 (BIOCON), rows L1-49 and L5-28

A screen, not investment advice. Produced by scripts/case_study_read_held_g24.py.

## L1-49

Ask (FC-L1-T6-S3 done-when): every AI-supplied figure in your notes has a page number you checked yourself. The row's held record is the Opus blind check of 30 sampled call question-and-answer states: agreed 23 of 30 (qa-states/opus-check.json: agree 23, sampled 30). Bar 24 of 30 is from qa-states/DESIGN-QA-STATES.md ('at least 24 of 30 sampled items'), a bar the pilot set for itself, not a rulebook key.

Not closable because: opus-check.json holds only labels o01 to o30 with a Sonnet and an Opus state each; it does not record which of the 659 states.csv rows each label is, and no script in the repo draws or saves the sample (searched scripts/case_study_qa_states.py, scripts/case_study_qa_pairs.py, qa-states/*, ar-read, the roast-room and filings-coach trees for 'o30'). Without the identity of the 30 items they cannot be re-checked against the pages. Re-drawing a new 30 would be a different sample and a judgement of answer states, not a figure check; not done.

Held and unchanged: 23 of 30 agreed, bar 24, short by one. Disagreements by label (Sonnet/Opus), counted from the file:

- Disagreeing labels, counted from the file: 7 of 30: o02 partial/deflected; o19 answered/partial; o23 partial/answered; o25 partial/answered; o27 deferred/deflected; o28 answered/partial; o29 deflected/answered
- Agreeing: 23 of 30 (matches the 23 recorded).

Still not held: which states.csv rows the 30 labels are; page-level quotes for them.

## L5-28

Ask (FC-L5-T2-S3): has management guidance been beaten, met and missed, and is there a perfect record of small beats; count how often. No number is a rule (step text: 'Number: none as a rule'). No judgement about honesty here.

Held calls: pre-2022-11 calls held are two: Q4 FY22 call (filings text 2022-05-06 transcript) and Q1 FY23 call (2022-08-03 transcript). Calls before 2022-04 are not held (filings/text starts 2022-04-01; nothing dated 2020 or 2021). Calls 2022-11-15 to 2026-08-06 (14) are in management-text (management turns only).

Rule in code (classify): for revenue, growth, margin and level targets, higher is better: above the top of the window = beat; inside = in line (a floor target met = in line); below the bottom = miss. For R&D-share targets (a spending level, not a result), above / within / below range, never counted as beat or miss. Where the call uses words (mid-teens, high teens, mid-30s) the call states no number; the window is this code's wide reading, listed below. The actual is the company-printed number in a later held call; derived figures are labelled DERIVED. Quarter and year outcomes are matched to the guided period as the metric column says.

Windows used: mid-teens = 12 to 18; high teens = 16 to 20; low teens to high single digits = 7 to 14; mid-30s to 40% = 33 to 40; mid to high 30s = 33 to 40; mid-20s = 23 to 27; around 12% = 11 to 13; double-digit = 10 to no top

| id | metric | guidance (date, file, line, quote) | window | outcome (file, line, quote) | actual | verdict |
|---|---|---|---|---|---|---|
| G1 | Biologics R&D, % of revenue, FY23 | 2022-05-06, 2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall p011.txt line 20: "R&D investments to be around 10 % to 15% of" | 10 to 15 | call-2023-05-24.md line 21: "Net R&D spend for the year was at 16%, which is higher than our guidance of 12%" | 16.0 (as printed) | above range |
| G2 | Biologics R&D, % of revenue, FY23 (restated) | 2022-08-03, 2022-08-03_BIOCON_03082022193118_Q1FY23_EarningsCallTranscript p016.txt line 36: "and we have always guided for the 10% to 12% in terms of revenue." | 10 to 12 | call-2023-05-24.md line 21: "Net R&D spend for the year was at 16%, which is higher than our guidance of 12%" | 16.0 (as printed) | above range |
| G3 | Biologics R&D, % of sales, Q2 FY23 | 2022-11-15, call-2022-11-15.md line 23: "While this is higher than our guidance of 12% to 15% of sales" | 12 to 15 | call-2022-11-15.md line 23: "or 18% of BBL revenues. While this is higher than our guidance of 12% to 15% of sales" | 18.0 (as printed) | above range |
| G4 | Generics R&D, % of Generics revenue, FY23 | 2022-05-06, 2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall p014.txt line 36: "I would continue to hold R&D guidance between 12-14% of Generics revenue." | 12 to 14 | call-2023-05-24.md line 115: "generics R&D spend last year was roughly ₹220 crores for the full year" | 8.3 (DERIVED: R&D 220 / Generics revenue 2,637 x 100) | below range |
| G5 | Generics revenue growth, FY23, % | 2022-05-06, 2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall p013.txt line 17: "I'm quite hopeful that we'll be able to deliver double -digit growth in the next" | >= 10 | call-2023-05-24.md line 21: "delivering a growth of 13% year-on-year" | 13.0 (as printed) | in line (floor met) |
| G6 | Biologics core EBITDA margin, FY23, % | 2022-08-03, 2022-08-03_BIOCON_03082022193118_Q1FY23_EarningsCallTranscript p006.txt line 25: "guidance of it being in the mid-to-high 30s." | 33 to 40 | call-2023-05-24.md line 21: "Core EBITDA for the year was at ₹2,216 crores, up 68%" | 39.7 (DERIVED: core EBITDA 2,216 / Biologics revenue 5,584 x 100) | in line |
| G7 | Syngene revenue growth, FY23, % | 2022-08-03, 2022-08-03_BIOCON_03082022193118_Q1FY23_EarningsCallTranscript p008.txt line 7: "Syngene has raised its revenue guidance for the year from mid-teens to high teens" | 16 to 20 | call-2023-05-24.md line 21: "Operating revenues were ₹3,193 crores in FY23, a growth of 23% over last year" | 23.0 (as printed) | beat |
| G8 | Viatris deal closure date (guided: second half of CY2022) | 2022-05-06, 2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall p008.txt line 16: "We expect deal closure in the second half of the CY2022." | by 2022-12-31 | call-2023-05-24.md line 21: "we concluded this deal at the end of November" | 2022-11-30 (end of November (year read from FY23 call context)) | in line |
| G9 | Biologics quarterly revenue Rs crore, Q3 FY23 (guided: higher than ~1,000 after Q2) | 2022-11-15, call-2022-11-15.md line 53: "the ﬁrst two quarters of this year will be around that ₹1,000 crore mark, and then we will see it break away" | >= 1000 | call-2023-02-15.md line 50: "we are at a ₹1500 crores level this quarter for Biocon Biologics" | 1500.0 (as printed) | in line (floor met) |
| G10 | Biologics quarterly revenue Rs crore, Q4 FY23 (guided: to cross 2,000) | 2023-02-15, call-2023-02-15.md line 50: "we expect this number when we capture the full ﬁnancials of the Viatris business in Q4, to cross ₹2000 crores" | >= 2000 | call-2023-05-24.md line 21: "Biocon Biologics recorded revenues of ₹2,102 crores for Q4" | 2102.0 (as printed) | in line (floor met) |
| G11 | Group R&D, % of revenue ex-Syngene, FY24 | 2023-02-15, call-2023-02-15.md line 22: "We will see R&D investments normalize to around 12% levels of sales" | 11 to 13 | call-2024-05-16.md line 22: "R&D investment for the full year was INR 1,154 crore, up 3% year-on-year and representing 10% of revenues" | 10.0 (as printed) | below range |
| G12 | Generics revenue growth, FY24, % | 2023-05-24, call-2023-05-24.md line 21: "We expect a mid-teen growth trajectory for the Generics business" | 12 to 18 | call-2024-05-16.md line 22: "Generics delivering a modest 1% year-on-year growth" | 1.0 (as printed) | miss |
| G13 | Generics revenue growth, FY24, % (revised guide) | 2023-11-10, call-2023-11-10.md line 104: "might be more titrated down to low teens to high single digits" | 7 to 14 | call-2024-05-16.md line 22: "Generics delivering a modest 1% year-on-year growth" | 1.0 (as printed) | miss |
| G14 | Biologics core EBITDA margin, Q2 FY24, % | 2023-05-24, call-2023-05-24.md line 99: "I think we have guided for mid-30%s to 40% margins." | 33 to 40 | call-2023-11-10.md line 22: "core EBITDA of ₹660 crores with margins of 34%" | 34.0 (as printed) | in line |
| G15 | Biologics core EBITDA margin, Q3 FY24, % | 2023-05-24, call-2023-05-24.md line 99: "I think we have guided for mid-30%s to 40% margins." | 33 to 40 | call-2024-02-09.md line 22: "core EBITDA of INR 587 crores with a margin of 28%" | 28.0 (as printed) | miss |
| G16 | Generics EBITDA margin, FY25, % | 2025-01-31, call-2025-01-31.md line 120: "directionally, what I have guided for is an EBITDA margin of 10% to 12%." | 10 to 12 | call-2025-05-09.md line 23: "EBITDA for FY'25 was INR 377 crores with EBITDA margin at 12%" | 12.0 (as printed) | in line |
| G17 | Biologics R&D, % of revenue, FY25 (guide read 7-9; the call says '6%, 7% to 9%') | 2025-01-31, call-2025-01-31.md line 30: "R&D in that 6%, 7% to 9% range that we have guided." | 7 to 9 | call-2025-05-09.md line 23: "This R&D investments for the year were at 7% of revenue" | 7.0 (as printed) | within range |
| G18 | Syngene operating EBITDA margin, FY26, % | 2026-02-13, call-2026-02-13.md line 25: "those margins have been higher than what our guidance has been in the mid-20s." | 23 to 27 | call-2026-05-08.md line 20: "Operating EBITDA margin at 25% for the year was in line with Syngene's revised full year guidance." | 25.0 (as printed) | in line |

Quote check by code: 18 of 18 rows have both quotes found on the stated line (whitespace ignored, 30 words max).

Counts (by verdict): above range 3; beat 1; below range 2; in line 5; in line (floor met) 3; miss 3; within range 1

Beats 1, misses 3, in line 8 (of which floor met 3), R&D-share rows outside range 5 (above 3, below 2), within range 1. G1, G2 and G3 score the same FY23 / Q2 Biologics R&D outcome against three restatements of the guide; G12 and G13 score the same 1% against the original and the revised Generics guide; G14 and G15 score one guide against two quarters, so rows are not independent statements.

## Guidance statements not scored

- 2022-05-06 capex US$300 million over 2020 to 2024 (p013 line 25-26): no held figure of capex summed over 2020-2024 was read; not searched beyond the call texts and ar-read tables headings
- 2025-05-09 and 2025-08-08 five biosimilar launches in 12 to 18 months: window ends after the held record (to 2026-11); 2025-11-12 line 16 reports four launched and one imminent, so still open
- 2025-11-12 line 28 Biologics R&D 7% to 9% full year FY26: 2026-05-08 call gives Q4 only (7%), no FY26 full-year R&D share held
- 2024-05-16 line 22 Syngene FY25 revenue growth single digit to low double digits: FY25 Syngene growth is not stated in the held Biocon call texts read
- 2022-11-15 line 91 BBL debt target US$1.5 billion: no dated outcome net-debt figure for BBL read; group net debt figures differ in scope

## Still not held
- Calls before 2022-04 (including the FY21 and FY22 earlier quarters); results text was not used here, outcomes come from later held call text as printed by management, not re-derived from statements. Statement-page check of each outcome against the annual report or results filing was not done in this group.
- Management words without a number outside the windows above (for example 'ramp up', 'robust') are not scored.
