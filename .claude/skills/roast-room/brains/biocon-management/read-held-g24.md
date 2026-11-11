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

Rule in code (classify): for revenue, growth, margin and level targets, higher is better: above the top of the window = beat; inside = in line (a floor target met = in line); below the bottom = miss. For R&D-share targets (a spending level, not a result), above / within / below range, never counted as beat or miss. A dated target is in line if the filed date is on or before the guided end, else a miss. The filed figure is the company-printed number in a results filing or annual report (first printed reading); a figure derived from filed rows is labelled DERIVED and is shown but is the filed figure only where nothing is printed. Third-party data is not used. Where the guide uses words (mid-teens, high teens, mid-30s) no number is stated; the window is this code's reading, tabled below with a narrower and a wider one.

Windows used (code's own reading of words): mid-teens = 12 to 18; high teens = 16 to 20; low teens to high single digits = 7 to 14; mid-30s to 40% = 33 to 40; mid to high 30s = 33 to 40; mid-20s = 23 to 27; around 12% = 11 to 13; double-digit = 10 to no top; single digit to low double digits = 1 to 13; around 10% = 9 to 11; high single digit = 7 to 9

### 1. Call figure against filed figure

| id | metric | window | call figure (file, line, quote) | call class | filed figure (file, line, quote) | filed vs call | filed class | class changes? |
|---|---|---|---|---|---|---|---|---|
| G1 | Biologics R&D, % of revenue, FY23 | 10 to 15 | 16.0 (as printed); data/management-text/call-2023-05-24.md line 21: "Net R&D spend for the year was at 16%, which is higher than our guidance of 12%" | above range | 16.0 (printed in the Q4 FY23 press release); data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p008.txt line 28: "Net R&D investments for the year increased 186% to Rs 889 crore, representing 16 % of revenue" | same | above range | no |
| G2 | Biologics R&D, % of revenue, FY23 (restated) | 10 to 12 | 16.0 (as printed); data/management-text/call-2023-05-24.md line 21: "Net R&D spend for the year was at 16%, which is higher than our guidance of 12%" | above range | 16.0 (printed in the Q4 FY23 press release); data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p008.txt line 28: "Net R&D investments for the year increased 186% to Rs 889 crore, representing 16 % of revenue" | same | above range | no |
| G3 | Biologics R&D, % of sales, Q2 FY23 | 12 to 15 | 18.0 (as printed); data/management-text/call-2022-11-15.md line 23: "or 18% of BBL revenues. While this is higher than our guidance of 12% to 15% of sales" | above range | 18.5 (DERIVED: R&D 184 / BBL Q2 revenue 997 x 100 (the filing prints no share)); data/filings/text/2022-11-14_BIOCON_14112022210312_PressRelease141122022/p003.txt line 37: "R&D investments at Rs 184 Crore"; data/filings/text/2022-11-14_BIOCON_14112022210312_PressRelease141122022/p003.txt line 34: "34% YoY to Rs 997 Crore" | same | above range | no |
| G4 | Generics R&D, % of Generics revenue, FY23 | 12 to 14 | 8.3 (DERIVED: R&D 220 / Generics revenue 2,637 x 100); data/management-text/call-2023-05-24.md line 115: "generics R&D spend last year was roughly ₹220 crores for the full year" | below range | not held | n/a | not held | n/a |
| G5 | Generics revenue growth, FY23, % | >= 10 | 13.0 (as printed); data/management-text/call-2023-05-24.md line 21: "delivering a growth of 13% year-on-year" | in line (floor met) | 13.0 (printed in the Q4 FY23 press release); data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p007.txt line 38: "FY23 Revenue at Rs 2,637 Crore, up 13% from Rs 2,341 Crore" | same | in line (floor met) | no |
| G6 | Biologics core EBITDA margin, FY23, % | 33 to 40 | 39.7 (DERIVED: core EBITDA 2,216 / Biologics revenue 5,584 x 100); data/management-text/call-2023-05-24.md line 21: "Core EBITDA for the year was at ₹2,216 crores, up 68%" | in line | 41.0 (printed in the Q4 FY23 investor deck (p025): core EBITDA % of revenue); data/filings/text/2023-05-24_BIOCON_24052023160532_InvestorPresentationQ4_signed/p025.txt line 24: "% of revenue 41% 39%" | differs | beat | yes |
| G7 | Syngene revenue growth, FY23, % | 16 to 20 | 23.0 (as printed); data/management-text/call-2023-05-24.md line 21: "Operating revenues were ₹3,193 crores in FY23, a growth of 23% over last year" | beat | 23.0 (printed in the Q4 FY23 press release); data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p009.txt line 47: "FY23 revenue at Rs 3,193 Crore, up 23% from Rs 2,604 Crore in FY22" | same | beat | no |
| G8 | Viatris deal closure date (guided: second half of CY2022) | by 2022-12-31 | 2022-11-30 (end of November (year read from FY23 call context)); data/management-text/call-2023-05-24.md line 21: "we concluded this deal at the end of November" | in line | 2022-11-29 (filed Regulation 30 disclosure, completion date); data/filings/text/2022-11-29_BIOCON_29112022183212_PressRelease_29112022/p001.txt line 40: "on 29, November, 2022 completed the acquisition of the biosimilars" | differs | in line | no |
| G9 | Biologics quarterly revenue Rs crore, Q3 FY23 (guided: higher than ~1,000 after Q2) | >= 1000 | 1500.0 (as printed); data/management-text/call-2023-02-15.md line 50: "we are at a ₹1500 crores level this quarter for Biocon Biologics" | in line (floor met) | 1507.0 (printed in the Q3 FY23 press release); data/filings/text/2023-02-14_BIOCON_14022023195034_PressRelease_signed/p003.txt line 44: "Biocon Biologics recorded its highest ever quarterly revenue of Rs 1,507 crore" | same | in line (floor met) | no |
| G10 | Biologics quarterly revenue Rs crore, Q4 FY23 (guided: to cross 2,000) | >= 2000 | 2102.0 (as printed); data/management-text/call-2023-05-24.md line 21: "Biocon Biologics recorded revenues of ₹2,102 crores for Q4" | in line (floor met) | 2102.0 (printed in the Q4 FY23 investor deck); data/filings/text/2023-05-24_BIOCON_24052023160532_InvestorPresentationQ4_signed/p025.txt line 15: "Revenue 2,102 982 114" | same | in line (floor met) | no |
| G11 | Biocon Biologics R&D, % of revenue, FY24 (year read from 'as we accrue full revenues from Viatris', the code's reading) | 11 to 13 | 10.0 (as printed); data/management-text/call-2024-05-16.md line 22: "We also continue to invest in our pipeline to support future growth with an R&D spend at 10% of revenues" | below range | 10.0 (printed in the Q4 FY24 press release, Biocon Biologics section (p008)); data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p008.txt line 41: "to drive future growth with R&D investments at 10% of its revenue" | same | below range | no |
| G12 | Generics revenue growth, FY24, % | 12 to 18 | 1.0 (as printed); data/management-text/call-2024-05-16.md line 22: "Generics delivering a modest 1% year-on-year growth" | miss | 1.0 (printed in the FY24 annual report (p075)); annual-report/FY24/p075.md line 28: "reflecting a growth of 1%" | same | miss | no |
| G13 | Generics revenue growth, FY24, % (revised guide) | 7 to 14 | 1.0 (as printed); data/management-text/call-2024-05-16.md line 22: "Generics delivering a modest 1% year-on-year growth" | miss | 1.0 (printed in the FY24 annual report (p075)); annual-report/FY24/p075.md line 28: "reflecting a growth of 1%" | same | miss | no |
| G14 | Biologics core EBITDA margin, Q2 FY24, % | 33 to 40 | 34.0 (as printed); data/management-text/call-2023-11-10.md line 22: "core EBITDA of ₹660 crores with margins of 34%" | in line | 34.0 (printed in the Q2 FY24 press release); data/filings/text/2023-11-10_BIOCON_10112023171756_PressRelease_signed/p007.txt line 41: "Core EBITDA at Rs 660 crore, grew by 47%, reflecting healthy margins of 34%" | same | in line | no |
| G15 | Biologics core EBITDA margin, Q3 FY24, % | 33 to 40 | 28.0 (as printed); data/management-text/call-2024-02-09.md line 22: "core EBITDA of INR 587 crores with a margin of 28%" | miss | 28.0 (printed in the Q3 FY24 press release); data/filings/text/2024-02-08_BIOCON_08022024203450_PressRelease_080224_signed/p008.txt line 15: "Core EBITDA at Rs 587 crore, with Core EBITDA margins at 28%" | same | miss | no |
| G16 | Generics EBITDA margin, FY25, % | 10 to 12 | 12.0 (as printed); data/management-text/call-2025-05-09.md line 23: "EBITDA for FY'25 was INR 377 crores with EBITDA margin at 12%" | in line | 12.0 (printed in the Q4 FY25 investor deck (p010): EBITDA % of total revenue); data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 33: "% of Total Revenue 12% 14%" | same | in line | no |
| G17 | Biologics R&D, % of revenue, FY25 (guide read 7-9; the call says '6%, 7% to 9%') | 7 to 9 | 7.0 (as printed); data/management-text/call-2025-05-09.md line 23: "This R&D investments for the year were at 7% of revenue" | within range | 7.0 (printed in the Q4 FY25 press release); data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p007.txt line 41: "R&D investment of Rs 592 crore, representing 7% of FY25 revenue" | same | within range | no |
| G18 | Biocon Biologics EBITDA margin, FY26, % (guide: the Biologics CEO; the old pairing with Syngene's 25% is dropped) | 23 to 27 | none (call text gives no outcome figure) | not scored | 26.0 (printed in the Q4 FY26 press release, Biosimilars section (adjusted for the BFI divestment gain)); data/filings/text/2026-05-07_BIOCON_07052026233651_Covering_Letter_Press_Release/p006.txt line 4: "FY26 EBITDA at Rs 2,751 crore, up 40% YoY, adjusted for BFI divestment gain; representing EBITDA Margin of 26%" | n/a | in line | n/a |
| G19 | Five biosimilar launches, guided within 12 to 18 months of 2025-05-08 (end = 2026-11-08, DERIVED: 2025-05-08 + 18 months) | by 2026-11-08 | none (call text gives no outcome figure) | not scored | 2026-04-07 (fifth launch (denosumab, US) filed; date = the filing's date, 'today announced'); data/filings/text/2026-04-07_BIOCON_07042026160635_Pressrelease07042026/p002.txt line 16: "today announced the commercial launch of Bosaya" | n/a | in line | n/a |
| G20 | Biologics R&D, % of revenue, FY26 full year (guide 7-9) | 7 to 9 | none (call text gives no outcome figure) | not scored | 6.0 (printed in the FY26 annual report, Biosimilars section (p233)); annual-report/FY26/p233.md line 41: "R&D expenditure at approximately 6% of revenues, directed towards advancing the biosimilars pipeline" | n/a | below range | n/a |
| G21 | Syngene revenue growth, FY25, % (guided on a constant-currency basis; filed figure is reported growth) | 1 to 13 | none (call text gives no outcome figure) | not scored | 4.0 (printed in the Q4 FY25 press release (reported, not constant currency)); data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p008.txt line 29: "FY25 Revenue Up 4% at Rs 3,642 Crore" | n/a | in line | n/a |
| G22 | Biocon Biologics annual revenue, FY24: guided to reach US$1 billion (floor; the filing states the mark was crossed) | >= 1.0 | none (call text gives no outcome figure) | not scored | 1.0 (printed in the Q4 FY24 press release: the USD 1 billion mark was crossed (a statement, value 1.0 stands for 'crossed'; revenue Rs 8,824 crore)); data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p008.txt line 35: "Biocon Biologics crossed the USD 1 billion annual revenue mark in FY24" | n/a | in line (floor met) | n/a |
| G23 | Syngene revenue growth, FY24, % (guided on a constant-currency basis; filed figure is reported growth) | 12 to 18 | 9.0 (as printed); data/management-text/call-2024-05-16.md line 22: "Syngene delivered a 9% year-on-year revenue growth" | miss | 9.0 (printed in the Q4 FY24 press release (reported, not constant currency)); data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p010.txt line 31: "FY24 Revenue at Rs 3,489 Crore, up 9%" | same | miss | no |
| G24 | Biocon Biologics R&D, % of revenue, FY25 (guide 8-9, the 2024-05-16 call) | 8 to 9 | 7.0 (as printed); data/management-text/call-2025-05-09.md line 23: "This R&D investments for the year were at 7% of revenue" | below range | 7.0 (printed in the Q4 FY25 press release); data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p007.txt line 41: "R&D investment of Rs 592 crore, representing 7% of FY25 revenue" | same | below range | no |
| G25 | Generics R&D, % of Generics revenue, FY24 ('next year' in the answer, qa-pairs line 51) | 9 to 11 | none (call text gives no outcome figure) | not scored | 8.0 (printed in the Q4 FY25 investor deck, Generics page (p010): FY24 column); data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 31: "% of Revenue 9.5% 8%" | n/a | below range | n/a |
| G26 | Generics revenue growth, H2 FY23 over H2 FY22, % | 7 to 9 | none (call text gives no outcome figure) | not scored | 8.4 (DERIVED: (Q3 FY23 718 + Q4 FY23 717) / (Q3 FY22 607 + Q4 FY22 717) - 1; all four are printed in the two press releases); data/filings/text/2023-02-14_BIOCON_14022023195034_PressRelease_signed/p006.txt line 26: "Q3FY23 revenue at Rs 718 Crore, up 18% (YoY) from Rs 607 Crore in Q3FY22"; data/filings/text/2023-02-14_BIOCON_14022023195034_PressRelease_signed/p006.txt line 26: "Q3FY23 revenue at Rs 718 Crore, up 18% (YoY) from Rs 607 Crore in Q3FY22"; data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p007.txt line 37: "Q4FY23 revenue at Rs 717 Crore, same as in Q4FY22"; data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p007.txt line 37: "Q4FY23 revenue at Rs 717 Crore, same as in Q4FY22" | n/a | in line | n/a |
| G27 | Generics revenue growth, FY25, % | 7 to 9 | none (call text gives no outcome figure) | not scored | 8.0 (printed in the Q4 FY25 investor deck, Generics page (p010)); data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 27: "Operating Revenue 3,017 2,799 8" | n/a | in line | n/a |
| G28 | Generics R&D, % of revenue, FY26 ('similar trajectory' with no year stated; FY26 is the code's reading) | 8 to 10 | none (call text gives no outcome figure) | not scored | 10.0 (printed in the FY26 annual report, UN goals table (p010)); annual-report/FY26/p010.md line 10: "10% of revenues invested in R&D by Generics business" | n/a | within range | n/a |

Quote check by code: 28 of 28 rows have every guide, call and filed quote found on the stated line (whitespace ignored, 30 words max).

Guidance quotes (date, file, line, quote):

- G1: 2022-05-06, data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p011.txt line 20: "R&D investments to be around 10 % to 15% of"
- G2: 2022-08-03, data/filings/text/2022-08-03_BIOCON_03082022193118_Q1FY23_EarningsCallTranscript/p016.txt line 36: "and we have always guided for the 10% to 12% in terms of revenue."
- G3: 2022-11-15, data/management-text/call-2022-11-15.md line 23: "While this is higher than our guidance of 12% to 15% of sales"
- G4: 2022-05-06, data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p014.txt line 36: "I would continue to hold R&D guidance between 12-14% of Generics revenue."
- G5: 2022-05-06, data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p013.txt line 17: "I'm quite hopeful that we'll be able to deliver double -digit growth in the next"
- G6: 2022-08-03, data/filings/text/2022-08-03_BIOCON_03082022193118_Q1FY23_EarningsCallTranscript/p006.txt line 25: "guidance of it being in the mid-to-high 30s."
- G7: 2022-08-03, data/filings/text/2022-08-03_BIOCON_03082022193118_Q1FY23_EarningsCallTranscript/p008.txt line 7: "Syngene has raised its revenue guidance for the year from mid-teens to high teens"
- G8: 2022-05-06, data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p008.txt line 16: "We expect deal closure in the second half of the CY2022."
- G9: 2022-11-15, data/management-text/call-2022-11-15.md line 53: "the ﬁrst two quarters of this year will be around that ₹1,000 crore mark, and then we will see it break away"
- G10: 2023-02-15, data/management-text/call-2023-02-15.md line 50: "we expect this number when we capture the full ﬁnancials of the Viatris business in Q4, to cross ₹2000 crores"
- G11: 2023-02-15, data/management-text/call-2023-02-15.md line 22: "We will see R&D investments normalize to around 12% levels of sales"
- G12: 2023-05-24, data/management-text/call-2023-05-24.md line 21: "We expect a mid-teen growth trajectory for the Generics business"
- G13: 2023-11-10, data/management-text/call-2023-11-10.md line 104: "might be more titrated down to low teens to high single digits"
- G14: 2023-05-24, data/management-text/call-2023-05-24.md line 99: "I think we have guided for mid-30%s to 40% margins."
- G15: 2023-05-24, data/management-text/call-2023-05-24.md line 99: "I think we have guided for mid-30%s to 40% margins."
- G16: 2025-01-31, data/management-text/call-2025-01-31.md line 120: "directionally, what I have guided for is an EBITDA margin of 10% to 12%."
- G17: 2025-01-31, data/management-text/call-2025-01-31.md line 30: "R&D in that 6%, 7% to 9% range that we have guided."
- G18: 2026-02-13, data/management-text/call-2026-02-13.md line 27: "We did say that we will have the mid-20s for the current financial year."
- G19: 2025-05-08, data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p004.txt line 33: "positioned to launch 5 new products in the next 12-18 months"
- G20: 2025-11-12, data/management-text/call-2025-11-12.md line 28: "we would be in that 7% to 9% of revenues for R&D"
- G21: 2024-05-16, data/management-text/call-2024-05-16.md line 22: "guidance for fiscal '25 includes revenue growth at single digit to low double digits"
- G22: 2023-11-10, data/management-text/call-2023-11-10.md line 22: "we remain on track to deliver US$1 billion revenue for Biocon Biologics"
- G23: 2023-11-10, data/management-text/call-2023-11-10.md line 22: "mid- Transcript - Biocon Limited Q2 FY24 Earnings Call Page 7 of 23 teen constant currency growth in Syngene"
- G24: 2024-05-16, data/management-text/call-2024-05-16.md line 22: "expect R&D investments to be in the 8% to 9% of revenues range"
- G25: 2023-05-24, data/management-text/call-2023-05-24.md line 111: "generics R&D will be around 10% of segment revenues"
- G26: 2022-11-15, data/management-text/call-2022-11-15.md line 51: "the second half of this ﬁscal, we do expect a high single digit growth compared to second half of last year"
- G27: 2024-08-09, data/management-text/call-2024-08-09.md line 44: "For the overall year, we still expect like a high single-digit kind of growth levels for the business."
- G28: 2025-11-12, data/management-text/call-2025-11-12.md line 30: "I expect it to be in a similar trajectory of 8% to 10% of revenues."

### 2. Other filed readings per row (differences flagged)

- G1 (filed figure 16.0, class above range):
  - DERIVED: net R&D 889 / BBL revenue 5,584 x 100 = 15.9 -> above range, same class: data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p008.txt line 28: "increased 186% to Rs 889 crore"; data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p008.txt line 16: "FY23 revenue at Rs 5,584 Crore"
- G2 (filed figure 16.0, class above range):
  - DERIVED: net R&D 889 / BBL revenue 5,584 x 100 = 15.9 -> above range, same class: data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p008.txt line 28: "increased 186% to Rs 889 crore"; data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p008.txt line 16: "FY23 revenue at Rs 5,584 Crore"
- G4 (filed figure None, class not held):
  - BOUND, not a Generics figure: (group net R&D 1,119 - BBL 889) / Generics revenue 2,637 x 100; the remainder also holds Novel Biologics R&D = 8.7 (BOUND, not a figure, not classified): data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p005.txt line 18: "Net R&D Expenses 342 191 79 1,119 595 88"; data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p008.txt line 28: "increased 186% to Rs 889 crore"; data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p007.txt line 38: "FY23 Revenue at Rs 2,637 Crore"
- G5 (filed figure 13.0, class in line (floor met)):
  - DERIVED, segment total revenue in the FY25 five-year summary: FY23 27,644 / FY22 23,409, growth (a different measure; the report does not say why FY23 is not 26,370) = 18.1 -> in line (floor met), same class: company-record/biocon/ar-tables-FY21-FY26.csv line 377: "FY25,FY23,consolidated,highlights,generics_revenue,27644"; company-record/biocon/ar-tables-FY21-FY26.csv line 376: "FY25,FY22,consolidated,highlights,generics_revenue,23409"
- G6 (filed figure 41.0, class beat):
  - printed in the FY23 annual report (p236) = 41.0 -> beat, same class: annual-report/FY23/p236.md line 35: "was at 41% versus 39% in FY22"
  - DERIVED from the deck's own rows: core EBITDA 2,216 / revenue 5,584 x 100 = 39.7 -> in line, CLASS DIFFERS (in line): data/filings/text/2023-05-24_BIOCON_24052023160532_InvestorPresentationQ4_signed/p025.txt line 23: "Core EBITDA 2,216 1,320 68"; data/filings/text/2023-05-24_BIOCON_24052023160532_InvestorPresentationQ4_signed/p025.txt line 22: "Revenue 5,584 3,464 61"
- G9 (filed figure 1507.0, class in line (floor met)):
  - quarterly segment table (XBRL), segment 'Biosimilars' as filed, Rs million / 10 = Rs crore = 1506.6 -> in line (floor met), same class: company-record/biocon/segments-quarterly-2026-10-30.csv line 7: "31-Dec-2022,15-Feb-2023 17:40,Consolidated,Biosimilars,15066.0"
- G10 (filed figure 2102.0, class in line (floor met)):
  - quarterly segment table (XBRL), segment 'Biosimilars' as filed, Rs million / 10 = Rs crore = 2101.6 -> in line (floor met), same class: company-record/biocon/segments-quarterly-2026-10-30.csv line 12: "31-Mar-2023,24-May-2023 19:23,Consolidated,Biosimilars,21016.0"
- G12 (filed figure 1.0, class miss):
  - ar-tables csv row generics_growth FY24 = 1.0 -> miss, same class: company-record/biocon/ar-tables-FY21-FY26.csv line 302: "FY24,FY24,consolidated,highlights,generics_growth,1,%"
  - DERIVED, operating-revenue basis: FY24 2,799 (FY25 deck) / FY23 2,637 (FY23 deck), growth = 6.1 -> miss, same class: data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 27: "Operating Revenue 3,017 2,799 8"; data/filings/text/2023-05-24_BIOCON_24052023160532_InvestorPresentationQ4_signed/p024.txt line 19: "Segment Revenue 2,637 2,341 13"
- G13 (filed figure 1.0, class miss):
  - ar-tables csv row generics_growth FY24 = 1.0 -> miss, same class: company-record/biocon/ar-tables-FY21-FY26.csv line 302: "FY24,FY24,consolidated,highlights,generics_growth,1,%"
  - DERIVED, operating-revenue basis: FY24 2,799 (FY25 deck) / FY23 2,637 (FY23 deck), growth = 6.1 -> miss, same class: data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 27: "Operating Revenue 3,017 2,799 8"; data/filings/text/2023-05-24_BIOCON_24052023160532_InvestorPresentationQ4_signed/p024.txt line 19: "Segment Revenue 2,637 2,341 13"
- G16 (filed figure 12.0, class in line):
  - DERIVED from the deck's own rows: EBITDA 377 / operating revenue 3,017 x 100 = 12.5 -> beat, CLASS DIFFERS (beat): data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 32: "EBITDA 377 394 (4)"; data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 27: "Operating Revenue 3,017 2,799 8"
- G17 (filed figure 7.0, class within range):
  - DERIVED: R&D 592 / BBL revenue from operations 9,017 x 100 = 6.6 -> below range, CLASS DIFFERS (below range): data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p007.txt line 41: "R&D investment of Rs 592"; data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p007.txt line 29: "FY25 Revenue at Rs 9,017 Crore"
- G18 (filed figure 26.0, class in line):
  - DERIVED: FY26 Biosimilars EBITDA 2,751 / Biosimilars FY26 revenue 10,431 x 100 (the table row is the same segment as the section above) = 26.4 -> in line, same class: data/filings/text/2026-05-07_BIOCON_07052026233651_Covering_Letter_Press_Release/p006.txt line 4: "FY26 EBITDA at Rs 2,751 crore"; data/filings/text/2026-05-07_BIOCON_07052026233651_Covering_Letter_Press_Release/p004.txt line 28: "Biosimilars 2,756 2,463 2,463 12 10,431 9,017 9,017 16"
- G20 (filed figure 6.0, class below range):
  - printed in the FY26 annual report, UN goals table (p010) = 6.0 -> below range, same class: annual-report/FY26/p010.md line 10: "6% of revenues invested in R&D by Biosimilars business"
- G21 (filed figure 4.0, class in line):
  - Syngene CEO in the same release: 'in line with our earlier guidance' = 4.0 -> in line, same class: data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p004.txt line 41: "reported revenue growth of 4%, are in line with our earlier guidance"
- G25 (filed figure 8.0, class below range):
  - DERIVED: FY24 R&D 237 / FY24 operating revenue 2,799 x 100 = 8.5 -> below range, same class: data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 30: "R&D 286 237 21"; data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 27: "Operating Revenue 3,017 2,799 8"
- G27 (filed figure 8.0, class in line):
  - DERIVED: operating revenue 3,017 / 2,799 - 1 = 7.8 -> in line, same class: data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 27: "Operating Revenue 3,017 2,799 8"; data/filings/text/2025-05-09_Biocon2_09052025081203_IR09052025/p010.txt line 27: "Operating Revenue 3,017 2,799 8"
- G19 extra: call 2025-11-12: four launched, fifth imminent (management's own tally; separate filed dates for the four not read): data/management-text/call-2025-11-12.md line 16: "we have delivered on this commitment with successful launches of b Ustekinumab, bAspart, bBevacizumab and bAflibercept across geographies, and we expect an imminent launch of bDenosumab"

Rows where the filed figure differs from the call figure by more than rounding: G6, G8. Rows where the beat/miss/range class changes when the filed figure replaces the call figure: G6. A row that has only a filed figure (no call-side outcome) is not counted as a change.

### 3. Counts

Call text only (first pass, 18 rows with a call-side figure): beats 1, misses 4, in line 7 (floor met 3), R&D-share rows above range 3, below range 3, within range 1.
After the filing check, all rows with a held filed figure, else the call class (28 rows): beats 2, misses 4, in line 12 (floor met 4), R&D-share rows above range 3, below range 5, within range 2.

### 4. Independent statements

Raw rows: 28. Distinct outcomes: 25. Distinct guide statements: 25. Independent statements (rows linked by a shared guide statement or a shared outcome count once): 22.

Linked rows: G1+G2; G12+G13; G14+G15; G17+G21+G24; G22+G23.
- G1 and G2 share one outcome (FY23 Biologics R&D share): two restated guides, one outcome. G3 is its own outcome (Q2 FY23) but is the third restatement of the same guide topic.
- G12 and G13 share one outcome (Generics FY24 growth): the original and the revised guide, one outcome.
- G14 and G15 share one guide statement (the 2023-05-24 'mid-30s to 40%' line) against two different quarters: two outcomes, one guide statement. Counted as one independent statement with a split result (in line and miss).

Class tally on distinct outcomes (after the filing check): beats 2, misses 3, in line 12 (floor met 4), R&D-share rows above range 2, below range 4, within range 2.
Class tally on all raw rows (after the filing check): beats 2, misses 4, in line 12 (floor met 4), R&D-share rows above range 3, below range 5, within range 2.
Linked groups whose rows carry different classes: G14+G15, G17+G21+G24, G22+G23.

### 5. Where the word windows decide the class

The calls give no number for these words. The scoring uses the middle window (the code's own, generous to management). Each tested value is the call figure or a filed reading; 'depends' = the class changes between readings. Cost-share rows show within / above / below range, never beat or miss.

| id | words in the guide | narrower | code's | wider | value tested (source) | class narrower | class code's | class wider | depends on reading? |
|---|---|---|---|---|---|---|---|---|---|
| G5 | double-digit | >= 10 | >= 10 | >= 10 | 13.0 (call + printed in the Q4 FY23 press release) | in line (floor met) | in line (floor met) | in line (floor met) | no |
| G5 | double-digit | >= 10 | >= 10 | >= 10 | 18.1 (DERIVED, segment total revenue in the FY25 five-year summary) | in line (floor met) | in line (floor met) | in line (floor met) | no |
| G6 | mid to high 30s | 35 to 39 | 33 to 40 | 32 to 41 | 39.7 (call + DERIVED from the deck's own rows) | beat | in line | in line | YES |
| G6 | mid to high 30s | 35 to 39 | 33 to 40 | 32 to 41 | 41.0 (printed in the Q4 FY23 investor deck + printed in the FY23 annual report) | beat | beat | in line | YES |
| G7 | high teens | 17 to 19 | 16 to 20 | 15 to 21 | 23.0 (call + printed in the Q4 FY23 press release) | beat | beat | beat | no |
| G11 | around 12% | 11.5 to 12.5 | 11 to 13 | 10 to 14 | 10.0 (call + printed in the Q4 FY24 press release, Biocon Biologics section) | below range | below range | within range | YES |
| G12 | mid-teens | 14 to 16 | 12 to 18 | 11 to 19 | 1.0 (call + printed in the FY24 annual report + ar-tables csv row generics_growth FY24) | miss | miss | miss | no |
| G12 | mid-teens | 14 to 16 | 12 to 18 | 11 to 19 | 6.1 (DERIVED, operating-revenue basis) | miss | miss | miss | no |
| G13 | low teens to high single digits | 8 to 13 | 7 to 14 | 6 to 15 | 1.0 (call + printed in the FY24 annual report + ar-tables csv row generics_growth FY24) | miss | miss | miss | no |
| G13 | low teens to high single digits | 8 to 13 | 7 to 14 | 6 to 15 | 6.1 (DERIVED, operating-revenue basis) | miss | miss | in line | YES |
| G14 | mid-30s to 40% | 35 to 40 | 33 to 40 | 31 to 40 | 34.0 (call + printed in the Q2 FY24 press release) | miss | in line | in line | YES |
| G15 | mid-30s to 40% | 35 to 40 | 33 to 40 | 31 to 40 | 28.0 (call + printed in the Q3 FY24 press release) | miss | miss | miss | no |
| G18 | mid-20s | 24 to 26 | 23 to 27 | 22 to 28 | 26.0 (printed in the Q4 FY26 press release, Biosimilars section) | in line | in line | in line | no |
| G18 | mid-20s | 24 to 26 | 23 to 27 | 22 to 28 | 26.4 (DERIVED) | beat | in line | in line | YES |
| G21 | single digit to low double digits | 1 to 12 | 1 to 13 | 1 to 15 | 4.0 (printed in the Q4 FY25 press release + Syngene CEO in the same release) | in line | in line | in line | no |
| G23 | mid-teens | 14 to 16 | 12 to 18 | 11 to 19 | 9.0 (call + printed in the Q4 FY24 press release) | miss | miss | miss | no |
| G25 | around 10% | 9.5 to 10.5 | 9 to 11 | 8 to 12 | 8.0 (printed in the Q4 FY25 investor deck, Generics page) | below range | below range | within range | YES |
| G25 | around 10% | 9.5 to 10.5 | 9 to 11 | 8 to 12 | 8.5 (DERIVED) | below range | below range | within range | YES |
| G26 | high single digit | 8 to 9 | 7 to 9 | 7 to 10 | 8.4 (DERIVED) | in line | in line | in line | no |
| G27 | high single digit | 8 to 9 | 7 to 9 | 7 to 10 | 8.0 (printed in the Q4 FY25 investor deck, Generics page) | in line | in line | in line | no |
| G27 | high single digit | 8 to 9 | 7 to 9 | 7 to 10 | 7.8 (DERIVED) | miss | in line | in line | YES |

Beat/miss/in-line classes that depend on the word reading: G13, G14, G18, G27, G6. Cost-share classes that depend on it: G11, G25. Rows whose class is the same under all three readings: G12, G15, G21, G23, G26, G5, G7.
Rows with a stated number in the guide (G1-G4, G8-G10, G16, G17, G19, G20) use no word window, so they do not appear here.

### 6. Statements the first pass left unscored

Three now have a filed outcome and are scored above as G19 to G21 (rows with no call-side figure). Two stay unscored:

- US$300 million capex over 2020 to 2024 (2022-05-06 call; the answer follows the Generics capacity discussion, and the quote does not say whether it is Generics-only or group): guide quote data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p013.txt line 25: "overall guidance has been US$300 million of capex over a period of 2020 to 2024"
  - status: not held. Searched: annual-report FY22 to FY26 pages for capex; ar-tables-FY21-FY26.csv cash-flow rows; calls 2023-02-15 and 2025-05-09; results press releases. Only group-level capex (all three businesses) is printed, and no total for 2020 to 2024 on the guide's scope exists in the held files (and the scope itself is not stated), so group totals are not used as the outcome.
  - pointer, not an outcome: FY24 annual report prints group capex (Generics, Biosimilars, Research Services together): annual-report/FY24/p071.md line 35: "|Capital Expenditure|19,316|17,263|12|"
  - pointer, not an outcome: 2023-02-15 call, Generics capex per year: data/management-text/call-2023-02-15.md line 202: "I expect CapEx to be around ₹700 to ₹800 Crores per year"
- BBL debt target US$1.5 billion (2022-11-15 call): guide quote data/management-text/call-2022-11-15.md line 91: "on BBL's books, the debt target is $1.5 billion"
  - status: open: no scoring rule. Searched: calls 2023-2026, decks and press releases 2023-2026, annual reports FY23 to FY26. The statement gives a level at closing plus an intent to pay down, with no date and no net or gross basis, so there is no pass or fail line; a filed net debt reading exists but is a reading, not a score.
  - filed reading, not a score: BBL net debt at the Q3 FY24 deck: data/filings/text/2024-02-09_BIOCON_09022024143655_InvestorPresentation_090224_signed/p024.txt line 25: "BBL net debt at $1.2 billion"
  - filed reading, not a score: FY24 prepayment out of the acquisition debt: annual-report/FY24/p077.md line 15: "During FY24, Biocon Biologics prepaid USD 250 million out of the acquisition consortium debt of USD 1.2 billion."

## Still not held
- Calls before 2022-04 (including the FY21 and FY22 earlier quarters).
- Constant-currency Syngene FY25 growth (guide basis); only reported growth is held. Separate filed launch dates for the first four of the five biosimilar launches (management's own tally is held). Generics-only R&D in FY23 as a filed figure (only a group-minus-BBL bound is held). Generics-only capex 2020 to 2024.
- Management words without a number outside the windows above (for example 'ramp up', 'robust') are not scored.
