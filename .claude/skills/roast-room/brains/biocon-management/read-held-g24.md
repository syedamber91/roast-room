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

### 1. Entity of the guide and entity of the outcome (every row)

A guide is only scored against an outcome about the same business. Each row names both entities and quotes what shows them; '(inferred)' marks a case where the quoted text does not name the business outright.

| id | entity of the guide | entity of the outcome | same? | quotes that show the guide's entity | quotes that show the outcome's entity |
|---|---|---|---|---|---|
| G1 | Biocon Biologics | Biocon Biologics | yes | data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p011.txt line 16: "M.B Chinappa: This year we ended at 9%"; data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p003.txt line 18: "Chief Financial Officer, Biocon Biologics Limited" | data/management-text/call-2023-05-24.md line 21: "Biocon Biologics recorded revenues of ₹5,584 crores in FY23" |
| G2 | Biocon Biologics | Biocon Biologics | yes | data/filings/text/2022-08-03_BIOCON_03082022193118_Q1FY23_EarningsCallTranscript/p016.txt line 25: "M.B. Chinappa: Good morning, Prakash"; data/filings/text/2022-08-03_BIOCON_03082022193118_Q1FY23_EarningsCallTranscript/p003.txt line 16: "Chief Financial Officer, Biocon Biologics Limited" | data/management-text/call-2023-05-24.md line 21: "Biocon Biologics recorded revenues of ₹5,584 crores in FY23" |
| G3 | Biocon Biologics | Biocon Biologics | yes | data/management-text/call-2022-11-15.md line 23: "or 18% of BBL revenues. While this is higher than our guidance of 12% to 15% of sales" | data/management-text/call-2022-11-15.md line 23: "or 18% of BBL revenues" |
| G4 | Generics | Generics | yes | data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p014.txt line 36: "R&D guidance between 12-14% of Generics revenue" | data/management-text/call-2023-05-24.md line 115: "generics R&D spend last year was roughly ₹220 crores for the full year" |
| G5 | Generics (inferred: the passage is about API capacity) | Generics | yes | data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p013.txt line 11: "building a very large-scale, synthetic API" | data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p007.txt line 36: "GENERICS: APIs & Generic Formulations"; data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p007.txt line 38: "FY23 Revenue at Rs 2,637 Crore, up 13%" |
| G6 | Biocon Biologics | Biocon Biologics | yes | data/filings/text/2022-08-03_BIOCON_03082022193118_Q1FY23_EarningsCallTranscript/p006.txt line 19: "Biocon Biologics recorded a revenue of ₹977 Crores" | data/management-text/call-2023-05-24.md line 21: "Biocon Biologics recorded revenues of ₹5,584 crores in FY23, a year-on-year growth of 61%. Core EBITDA for the year was at ₹2,216 crores" |
| G7 | Syngene | Syngene | yes | data/filings/text/2022-08-03_BIOCON_03082022193118_Q1FY23_EarningsCallTranscript/p008.txt line 7: "Syngene has raised its revenue guidance for the year" | data/management-text/call-2023-05-24.md line 21: "Syngene delivered full-year results ahead of its upgraded guidance"; data/management-text/call-2023-05-24.md line 21: "Operating revenues were ₹3,193 crores in FY23, a growth of 23% over last year" |
| G8 | Biocon Biologics (the Viatris biosimilars deal) | Biocon Biologics | yes | data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p008.txt line 18: "In summary, Biocon Biologics has delivered strong revenue and profit growth this fiscal" | data/filings/text/2022-11-29_BIOCON_29112022183212_PressRelease_29112022/p001.txt line 39: "We hereby inform you that, Biocon Biologics Limited"; data/filings/text/2022-11-29_BIOCON_29112022183212_PressRelease_29112022/p001.txt line 40: "completed the acquisition of the biosimilars" |
| G9 | Biocon Biologics | Biocon Biologics | yes | data/management-text/call-2022-11-15.md line 53: "Shreehas Tambe, Deputy Chief Executive Officer, Biocon Biologics Limited" | data/management-text/call-2023-02-15.md line 50: "we are at a ₹1500 crores level this quarter for Biocon Biologics" |
| G10 | Biocon Biologics | Biocon Biologics | yes | data/management-text/call-2023-02-15.md line 50: "we are at a ₹1500 crores level this quarter for Biocon Biologics" | data/management-text/call-2023-05-24.md line 21: "Biocon Biologics recorded revenues of ₹2,102 crores for Q4" |
| G11 | Biocon Biologics | Biocon Biologics (the old pairing used Group R&D ex-Syngene, FY24 10%, AR FY24 p208 line 17; the number is the same, the entity was wrong) | yes | data/management-text/call-2023-02-15.md line 22: "or 19% of Biocon Biologics revenues. We will see R&D investments normalize to around 12% levels of sales" | data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p008.txt line 30: "Biocon Biologics reported a YoY growth of 12%"; data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p008.txt line 41: "R&D investments at 10% of its revenue" |
| G12 | Generics | Generics | yes | data/management-text/call-2023-05-24.md line 21: "We expect a mid-teen growth trajectory for the Generics business" | data/management-text/call-2024-05-16.md line 22: "Generics delivering a modest 1% year-on-year growth" |
| G13 | Generics (inferred: formulations and API are the two Generics lines named) | Generics | yes | data/management-text/call-2023-11-10.md line 104: "H2 API business should pick up compared to H1" | data/management-text/call-2024-05-16.md line 22: "Generics delivering a modest 1% year-on-year growth" |
| G14 | Biocon Biologics (inferred: the question names core margins at a 39% level, not the business; 39.7% is the Biologics FY23 figure) | Biocon Biologics | yes | data/qa-pairs/qa-2023-05-24.csv line 46: "Is there scope for improvement from the high 39% odd level that we are seeing" | data/filings/text/2023-11-10_BIOCON_10112023171756_PressRelease_signed/p007.txt line 30: "BIOSIMILARS: Biocon Biologics Limited (BBL)"; data/filings/text/2023-11-10_BIOCON_10112023171756_PressRelease_signed/p007.txt line 41: "Core EBITDA at Rs 660 crore, grew by 47%, reflecting healthy margins of 34%" |
| G15 | Biocon Biologics (inferred, as G14) | Biocon Biologics | yes | data/qa-pairs/qa-2023-05-24.csv line 46: "Is there scope for improvement from the high 39% odd level that we are seeing" | data/filings/text/2024-02-08_BIOCON_08022024203450_PressRelease_080224_signed/p008.txt line 15: "Core EBITDA at Rs 587 crore, with Core EBITDA margins at 28%"; data/filings/text/2024-02-08_BIOCON_08022024203450_PressRelease_080224_signed/p008.txt line 18: "Biocon Biologics pre paid ~USD 200 million towards reducing the acquisition-related debt" |
| G16 | Generics (inferred: the facility named is the Liraglutide drug-substance plant) | Generics | yes | data/management-text/call-2025-01-31.md line 120: "our margins did go down because the Liraglutide facility of the drug substance" | data/management-text/call-2025-05-09.md line 23: "For the Generics business, EBITDA for the quarter was INR 243 crores"; data/management-text/call-2025-05-09.md line 23: "EBITDA for FY'25 was INR 377 crores with EBITDA margin at 12%" |
| G17 | Biocon Biologics | Biocon Biologics | yes | data/management-text/call-2025-01-31.md line 30: "The margins for the Biocon Biologics business have been quite healthy. And we continue to invest in R&D in that 6%, 7% to 9% range that we have guided" | data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p007.txt line 25: "BIOSIMILARS: Biocon Biologics"; data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p007.txt line 29: "FY25 Revenue at Rs 9,017 Crore" |
| G18 | Biocon Biologics (the speaker is its CEO) | Biocon Biologics (the Biosimilars segment: same revenue figure, Rs 2,358 crore for Q4 FY24, under both names) | yes | data/management-text/call-2026-02-13.md line 27: "Chief Executive Officer & Managing Director, Biocon Biologics Limited"; data/management-text/call-2026-02-13.md line 27: "We did say that we will have the mid-20s for the current financial year" | data/filings/text/2026-05-07_BIOCON_07052026233651_Covering_Letter_Press_Release/p006.txt line 10: "The Biosimilars business remained the core growth driver"; data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p008.txt line 30: "Biocon Biologics reported a YoY growth of 12% for Q4FY24 with revenue at Rs 2,358 crore"; data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p005.txt line 18: "Biosimilars 2,358 2,102 12 8,824 5,584 58" |
| G19 | Biocon Biologics | Biocon Biologics (biosimilar denosumab, under the Biosimilars heading) | yes | data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p004.txt line 22: "BIOCON BIOLOGICS"; data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p004.txt line 33: "positioned to launch 5 new products in the next 12-18 months" | data/filings/text/2026-05-07_BIOCON_07052026233651_Covering_Letter_Press_Release/p006.txt line 10: "The Biosimilars business remained the core growth driver"; data/filings/text/2026-05-07_BIOCON_07052026233651_Covering_Letter_Press_Release/p006.txt line 19: "The Company launched Bosaya™ and Aukelso ™, the Denosumab biosimilars" |
| G20 | Biocon Biologics | Biocon Biologics (the FY26 annual report's biosimilars business) | yes | data/management-text/call-2025-11-12.md line 28: "Chief Executive Officer & Managing Director, Biocon Biologics Limited"; data/management-text/call-2025-11-12.md line 28: "we would be in that 7% to 9% of revenues for R&D" | annual-report/FY26/p233.md line 39: "our biosimilars business recorded revenues of"; annual-report/FY26/p233.md line 41: "R&D expenditure at approximately 6% of revenues, directed towards advancing the biosimilars pipeline" |
| G21 | Syngene | Syngene | yes | data/management-text/call-2024-05-16.md line 22: "guidance for fiscal '25 includes revenue growth at single digit to low double digits" | data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p004.txt line 39: "Syngene reported Q4FY25 revenue growth of 11% year-on-year"; data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p008.txt line 26: "RESEARCH SERVICES" |
| G22 | Biocon Biologics | Biocon Biologics | yes | data/management-text/call-2023-11-10.md line 22: "we remain on track to deliver US$1 billion revenue for Biocon Biologics" | data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p008.txt line 35: "Biocon Biologics crossed the USD 1 billion annual revenue mark in FY24" |
| G23 | Syngene | Syngene | yes | data/management-text/call-2023-11-10.md line 22: "mid- Transcript - Biocon Limited Q2 FY24 Earnings Call Page 7 of 23 teen constant currency growth in Syngene" | data/management-text/call-2024-05-16.md line 22: "Syngene delivered a 9% year-on-year revenue growth"; data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p010.txt line 29: "RESEARCH SERVICES: Syngene" |
| G24 | Biocon Biologics (inferred: the sentence sits in the Biologics part of the call, just before 'Novel Biologics'; Group R&D ex-Syngene was also 7% in FY25, AR FY25 p068, so the class is the same either way) | Biocon Biologics | yes | data/management-text/call-2024-05-16.md line 22: "R&D investments to be in the 8% to 9% of revenues range. Novel Biologics Let me now give a brief update" | data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p007.txt line 25: "BIOSIMILARS: Biocon Biologics"; data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p007.txt line 41: "R&D investment of Rs 592 crore, representing 7% of FY25 revenue" |
| G25 | Generics (the question asks what part of R&D is earmarked for the generics segment) | Generics | yes | data/qa-pairs/qa-2023-05-24.csv line 51: "What part of that would be earmarked for the generics segment" | data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p007.txt line 7: "GENERICS: APIs & Generic Formulations"; data/filings/text/2024-05-16_BIOCON_16052024175855_PressRelease_160524_signed/p007.txt line 9: "FY24 Revenue at Rs 2,799 Crore, up 1%" |
| G26 | Generics (inferred: the sentence follows 'When it comes to generic formulation') | Generics | yes | data/management-text/call-2022-11-15.md line 51: "When it comes to generic formulation, as we said, we've got a few approvals in emerging markets" | data/filings/text/2023-02-14_BIOCON_14022023195034_PressRelease_signed/p006.txt line 25: "GENERICS: APIs & Generic Formulations"; data/filings/text/2023-05-23_BIOCON_23052023211340_PressRelease_signed/p007.txt line 36: "GENERICS: APIs & Generic Formulations" |
| G27 | Generics | Generics | yes | data/qa-pairs/qa-2024-08-09.csv line 9: "business prospects for Biocon Generics" | data/management-text/call-2025-05-09.md line 23: "For FY'25, Revenue from Operations was INR 3,017 crores, reflecting an 8% year-on-year increase"; data/management-text/call-2025-05-09.md line 23: "For the Generics business, EBITDA for the quarter was INR 243 crores" |
| G28 | Generics | Generics | yes | data/management-text/call-2025-11-12.md line 30: "the R&D spend again, last quarter was at 9% of Generics revenue" | annual-report/FY26/p010.md line 10: "10% of revenues invested in R&D by Generics business" |

Rows whose guide and outcome belong to different entities: none. G11 and G18 were the two found; the old pairings (G11: Group R&D ex-Syngene 10%, AR FY24 p208; G18: Syngene's 25% FY26 margin, 2026-05-08 call line 20, against the Biologics CEO's 'mid-20s') are dropped, not scored.

### 2. Call figure against filed figure

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

### 3. Other filed readings per row (differences flagged)

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
  - printed in the FY26 annual report, biosimilars business (p233) = 26.0 -> in line, same class: annual-report/FY26/p233.md line 41: "translating into an EBITDA margin of 26%"
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

Rows where the filed figure differs from the call figure by more than rounding: G6, G8. Rows where the beat/miss/range class changes when the filed figure replaces the call figure: G6. A row that has only a filed figure (no call-side figure) is not counted as a change.

### 4. Counts (the code's own window, printed figure first)

Call text only (rows with a call-side figure): beats 1, misses 4, in line 7 (floor met 3), R&D-share rows above range 3, below range 3, within range 1.
After the filing check, all 28 rows (a filed figure where held, else the call class): beats 2, misses 4, in line 12 (floor met 4), R&D-share rows above range 3, below range 5, within range 2.

### 5. Independent statements

Raw rows: 28. Distinct outcomes: 25. Distinct guide statements: 27. Independent statements (rows linked by a shared guide statement or a shared outcome count once): 24.

Linked rows: G1+G2; G12+G13; G14+G15; G17+G24.
- G1 and G2 share one outcome (FY23 Biologics R&D share): two restated guides, one outcome. G3 is its own outcome (Q2 FY23) but is the third restatement of the same guide topic.
- G12 and G13 share one outcome (Generics FY24 growth): the original and the revised guide, one outcome.
- G14 and G15 share one guide statement (the 2023-05-24 'mid-30s to 40%' line) against two different quarters: two outcomes, one guide statement. Counted as one independent statement with a split result (in line and miss).
- G17 and G24 share one outcome (Biologics FY25 R&D 7%): two guides (6%, 7% to 9% and 8% to 9%), one outcome.
- G22 and G23 come from one sentence (2023-11-10 line 22) but are two statements about two businesses; they are not linked.

Class tally on distinct outcomes (after the filing check): beats 2, misses 3, in line 12 (floor met 4), R&D-share rows above range 2, below range 4, within range 2.
Class tally on all raw rows (after the filing check): beats 2, misses 4, in line 12 (floor met 4), R&D-share rows above range 3, below range 5, within range 2.
Linked groups whose rows carry different classes: G14+G15, G17+G24.

### 6. Where the word windows decide the class, and the counts as a range

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
| G18 | mid-20s | 24 to 26 | 23 to 27 | 22 to 28 | 26.0 (printed in the Q4 FY26 press release, Biosimilars section + printed in the FY26 annual report, biosimilars business) | in line | in line | in line | no |
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

Counts under each window reading and each choice of filed figure (printed first, or derived first where both exist: G6 and G16 differ; G4 uses the call figure because its filed reading is a bound):

| window | filed figure used | beats | misses | in line | R&D-share within | above | below | distinct outcomes: beats / misses / in line |
|---|---|---|---|---|---|---|---|---|
| narrower | printed first | 2 | 5 | 11 | 2 | 3 | 5 | 2 / 4 / 11 |
| narrower | derived first | 4 | 6 | 8 | 1 | 3 | 6 | 4 / 5 / 8 |
| code's | printed first | 2 | 4 | 12 | 2 | 3 | 5 | 2 / 3 / 12 |
| code's | derived first | 2 | 4 | 12 | 1 | 3 | 6 | 2 / 3 / 12 |
| wider | printed first | 1 | 4 | 13 | 4 | 3 | 3 | 1 / 3 / 13 |
| wider | derived first | 2 | 3 | 13 | 3 | 3 | 4 | 2 / 3 / 12 |
| RANGE over the six readings | | 1 to 4 | 3 to 6 | 8 to 13 | 1 to 4 | 3 | 3 to 6 | 1 to 4 / 3 to 5 / 8 to 13 |

Rows that are a miss under all three windows with the printed figure: G12, G13, G15, G23. Rows that are a miss under all three windows with the printed figure AND with the derived figure: G12, G15, G23 (G13's derived 6.1% falls inside the wider 'low teens to high single digits' window, so G13 is a miss under all three windows only on its printed 1%).
Answered WITHOUT any window: 'never a miss' is false. G12, G13, G15, G23 each fall outside even the widest window on the printed figure, and G12, G15, G23 do so on either figure, so the answer to 'does the company always beat by a small margin and never miss?' is no, and it does not depend on how any guidance word is read.
Needs a window (the step names no number): how many guides were beaten, met or missed. Only the range above is stated, never one count. 'Small' in 'small beat' has no stated size, so which beats are small is not answered.

### 7. Statements left unscored

Two statements from the first pass stay unscored (G19 to G21 are scored above):

- US$300 million capex over 2020 to 2024 (2022-05-06 call; the answer follows the Generics capacity discussion, and the quote does not say whether it is Generics-only or group): guide quote data/filings/text/2022-05-06_BIOCON_06052022174949_Biocon_Transcript_EarningsCall/p013.txt line 25: "overall guidance has been US$300 million of capex over a period of 2020 to 2024"
  - status: not held. Searched: annual-report FY22 to FY26 pages for capex; ar-tables-FY21-FY26.csv cash-flow rows; calls 2023-02-15 and 2025-05-09; results press releases. Only group-level capex (all three businesses) is printed, and no total for 2020 to 2024 on the guide's scope exists in the held files (and the scope itself is not stated), so group totals are not used as the outcome.
  - pointer, not an outcome: FY24 annual report prints group capex (Generics, Biosimilars, Research Services together): annual-report/FY24/p071.md line 35: "|Capital Expenditure|19,316|17,263|12|"
  - pointer, not an outcome: 2023-02-15 call, Generics capex per year: data/management-text/call-2023-02-15.md line 202: "I expect CapEx to be around ₹700 to ₹800 Crores per year"
- BBL debt target US$1.5 billion (2022-11-15 call): guide quote data/management-text/call-2022-11-15.md line 91: "on BBL's books, the debt target is $1.5 billion"
  - status: open: no scoring rule. Searched: calls 2023-2026, decks and press releases 2023-2026, annual reports FY23 to FY26. The statement gives a level at closing plus an intent to pay down, with no date and no net or gross basis, so there is no pass or fail line; a filed net debt reading exists but is a reading, not a score.
  - filed reading, not a score: BBL net debt at the Q3 FY24 deck: data/filings/text/2024-02-09_BIOCON_09022024143655_InvestorPresentation_090224_signed/p024.txt line 25: "BBL net debt at $1.2 billion"
  - filed reading, not a score: FY24 prepayment out of the acquisition debt: annual-report/FY24/p077.md line 15: "During FY24, Biocon Biologics prepaid USD 250 million out of the acquisition consortium debt of USD 1.2 billion."

The re-sweep (section 8) adds 30 more numeric guides that are not scored, each with its reason: hits 3, 6, 7, 8, 9, 12, 18, 22, 30, 33, 34, 36, 37, 43, 44, 47, 61, 68, 74, 78, 89, 92, 117, 120, 121, 123, 137, 142, 150, 152.

Found outside the cue list while reading (hand reading; not scored):

- 2023-02-15 call: Biologics exit FY23 at a US$1 billion trajectory (a run rate, FX not held; the 2023-05-24 call says 'as per our guidance', management's own claim): data/management-text/call-2023-02-15.md line 22: "exiting FY23 at a US$ 1 billion trajectory". Unscored: no band or no filed outcome as stated in the label.
- 2024-05-16 call: Syngene FY25 operating EBITDA margin 'similar to fiscal'24 levels' and net profit growth in single digits (the rest of G21's guide sentence; 'similar to' states no band): data/management-text/call-2024-05-16.md line 22: "operating EBITDA margin to be similar to fiscal'24 levels and Net Profit growth in single digits". Unscored: no band or no filed outcome as stated in the label.
- 2023-05-24 Q&A: Generics R&D 'closer to Rs 300 crores next year' (FY24; 'closer to' states no band; FY24 R&D 237 is in G25's deck row): data/qa-pairs/qa-2023-05-24.csv line 51: "will be closer to ₹300 crores next year". Unscored: no band or no filed outcome as stated in the label.
- 2025-05-09 call: 'from '25 to '30' a product launched a year (cadence to FY30, not due): data/management-text/call-2025-05-09.md line 101: "we saw ourselves launching a product a year". Unscored: no band or no filed outcome as stated in the label.

### 8. Re-sweep of the 14 calls for numeric guides

Cue list and rule are written above HIT_TABLE in the script. Cues: guid-, expect-, target-, on track, plan, aim, intend, anticipate, project, 'we had said/given', will normalise, will be around/in; each with a digit or a number-word (mid-teens, double digit, ...). Calls swept: the 14 in management-text, 2022-11-15 to 2026-08-06. The two older calls (2022-05-06, 2022-08-03) are page files and were read for G1, G2, G4 to G8 only, not swept. The cue list is not exhaustive: section 'found outside the cue list' below names what a hand reading added.

| call | candidate sentences | scored guides (ROW) | new scored (NEW) | restatements (RES) | outcome reports (OUT) | unscored guides (UNS) | not a numeric guide (NOT) | numeric guides found (ROW+NEW+RES+UNS) |
|---|---|---|---|---|---|---|---|---|
| 2022-11-15 | 9 | 2 | 1 | 0 | 0 | 5 | 1 | 8 |
| 2023-02-15 | 29 | 1 | 0 | 2 | 0 | 8 | 18 | 11 |
| 2023-05-24 | 22 | 2 | 1 | 3 | 2 | 3 | 11 | 9 |
| 2023-11-10 | 6 | 1 | 1 | 0 | 1 | 1 | 2 | 3 |
| 2024-02-09 | 6 | 0 | 0 | 0 | 1 | 1 | 4 | 1 |
| 2024-05-16 | 17 | 1 | 1 | 0 | 0 | 3 | 12 | 5 |
| 2024-08-09 | 11 | 0 | 1 | 0 | 1 | 1 | 8 | 2 |
| 2025-01-31 | 9 | 2 | 0 | 0 | 0 | 0 | 7 | 2 |
| 2025-05-09 | 11 | 0 | 0 | 2 | 1 | 2 | 6 | 4 |
| 2025-08-08 | 12 | 0 | 0 | 1 | 0 | 2 | 9 | 3 |
| 2025-11-12 | 7 | 1 | 1 | 1 | 0 | 1 | 3 | 4 |
| 2026-02-13 | 3 | 1 | 0 | 0 | 0 | 1 | 1 | 2 |
| 2026-05-08 | 6 | 0 | 0 | 0 | 1 | 0 | 5 | 0 |
| 2026-08-06 | 4 | 0 | 0 | 0 | 0 | 2 | 2 | 2 |
| ALL | 152 | 11 | 6 | 9 | 7 | 30 | 89 | 56 |

Quote check by code: 152 of 152 quotes below are on the stated line (first 30 words of the sentence, whitespace ignored).

Every numeric guide found (ROW, NEW, RES, UNS): hit number, call date, line, tag, reason, quote.

- 1 | 2022-11-15 line 23 | ROW:G3 | guide and outcome in one sentence | "While this is higher than our guidance of 12% to 15% of sales, we believe it will normalize once we accrue revenues from Serum's vaccines and Viatris' biosimilars businesses."
- 3 | 2022-11-15 line 45 | UNS | US market-share target 'mid to high teens': product and period not named in the sentence; no filed share figure held | "Almost on a weekly basis, we see them adding more customers to the list and we believe we're trending in the right direction towards that mid to high teens market"
- 4 | 2022-11-15 line 51 | NEW:G26 | Generics H2 FY23 growth, scored from the printed quarterly revenues | "So overall, the second half of this ﬁscal, we do expect a high single digit growth compared to second half of last year."
- 5 | 2022-11-15 line 53 | ROW:G9 | scored row | "So, in terms of what we had said on the revenue numbers, we had in the past said that the ﬁrst two quarters of this year will be around that"
- 6 | 2022-11-15 line 87 | UNS | the same share target as hit 3 | "We will trend towards those mid to high teens that we've guided and that seems to be moving in the right direction, Sameer."
- 7 | 2022-11-15 line 91 | UNS | Biologics debt target US$1.5 billion: listed in section 7 (no date, no net or gross basis) | "So, on BBL's books, the debt target is $1.5 billion, which we expect to pay down through improved cash ﬂows going forward and of course further equity raised from time"
- 8 | 2022-11-15 line 99 | UNS | a '12 months or so' timeline whose subject is not named in the sentence | "**Siddharth Mittal, CEO & Managing Director, Biocon Limited:** I think it would be a bit premature to comment on the timeline, but what we have said in the past, it"
- 9 | 2022-11-15 line 141 | UNS | Serum vaccines US$300 million a year at mid-to-high 30s margin: no vaccines line in any held segment table (Generics, Biosimilars, Research services only) | "So, as we've indicated, we could expect revenues in the range of $300 million per annum, and with an EBITDA close to our core EBITDA margins, which is the mid"
- 12 | 2023-02-15 line 22 | UNS | validation batches at both sites by H1 FY24: the filed outcomes say 'process validation' (Vizag in the Q2 FY24 release, Bengaluru in the Q3 FY24 release), at quarter level; that the two phrases mean the same is not shown | "We expect to complete the validation batches in both sites by H1 of FY24."
- 16 | 2023-02-15 line 50 | ROW:G10 | scored row | "But, let me start by saying that you have already seen that we are at a ₹1500 crores level this quarter for Biocon Biologics and we expect this number when"
- 17 | 2023-02-15 line 52 | RES:G10 | restates the Q4 Rs 2,000 crore guide | "Just the way Kiran put it, ₹2000 crores is our expected revenues for Q4, excluding vaccines, that translates to a run rate of US$ 1 billion per annum."
- 18 | 2023-02-15 line 68 | UNS | interchangeable product launch 'July of 2023': no filed launch date found (searched releases June 2023 to March 2024 for 'interchangeab') | "But as I said, the BBL dates of this would matter only after the ﬁrst commercial launch of the interchangeable product, which we believe will be in July of 2023."
- 20 | 2023-02-15 line 100 | RES:G3 | restates the Biologics R&D 12 to 15% range, no year stated | "But going forward, we expect to basically normalize R&D spends to that sort 12% to 15% levels."
- 22 | 2023-02-15 line 132 | UNS | facility revenue 'not expected until FY25': no facility-level revenue in the held filings | "So, the revenues from these facilities are not expected to commence until FY25."
- 30 | 2023-02-15 line 160 | UNS | own Semaglutide market entry 'end of calendar 2024/early 2025': later calls move the date (2025-01-31 line 94) but no filing states a launch, so no filed outcome | "We are still under litigation with Novo Nordisk, so Biocon has not yet settled but we expect to be in the market as mentioned, end of Calendar 2024/early 2025."
- 33 | 2023-02-15 line 180 | UNS | Ustekinumab filing by end-2023: the filings print the FDA accepting the application (FY24 AR p018 line 53), with no filing date | "So, we are right now in Phase I / Phase III trial for Ustekinumab, we have guided earlier that end 2023, we should be able to get to ﬁling."
- 34 | 2023-02-15 line 196 | UNS | new facilities capitalised once approved, 'FY25': a date; no filed capitalisation date read for it | "The new facilities will be capitalized once we received approvals from the FDA, which is expected in FY '25."
- 36 | 2023-02-15 line 202 | UNS | Generics capex Rs 700 to 800 crore a year: the annual report prints group capex only (FY24 AR p071 line 35) | "**Siddharth Mittal, CEO & Managing Director, Biocon Limited:** So, Generics I expect CapEx to be around ₹700 to ₹800 Crores per year, which includes the incremental capacities on our non-immunosuppressants"
- 37 | 2023-02-15 line 204 | UNS | Biologics capex Rs 100 to 150 million a year: only group capex is printed | "Chinappa, Chief Financial Officer, Biocon Biologics Limited:** We have given guidance of ₹100 to ₹150 million CapEx per annum."
- 43 | 2023-05-24 line 21 | UNS | the validation-batches guide of hit 12, restated | "Our facility in Vizag for immunosuppressants and peptide facility in Bengaluru were commissioned during FY23, with validation batches at both sides expected to be completed by the first half of"
- 44 | 2023-05-24 line 21 | UNS | Biologics 'on a $1 billion dollar trajectory as per our guidance': a run rate, FX not held; management's own claim that a guide was met | "Biocon Biologics recorded revenues of ₹2,102 crores for Q4, ending the year on $1 billion dollar trajectory as per our guidance."
- 46 | 2023-05-24 line 21 | RES:G11 | restates 'normalize to around 12%' | "The R&D spend we expect will normalize to around 12% in the coming quarters."
- 47 | 2023-05-24 line 21 | UNS | study completion dates (Ustekinumab end-2023, Denosumab end-2024): no filed completion date | "• We continue to progress our pipeline with biosimilar Denosumab, Ustekinumab and Pertuzumab and we are on track to complete the studies for Ustekinumab and Denosumab by the end of"
- 51 | 2023-05-24 line 21 | ROW:G12 | scored row | "We expect a mid-teen growth trajectory for the Generics business driven by enhanced capacities in our API business, volume growth in our base business, and new launches in generic formulations"
- 52 | 2023-05-24 line 25 | RES:G11 | 'we would like to be at a 12% of revenue level'; the same speaker says most R&D is Biologics | "And as we said, we would like to be at a 12% of revenue level."
- 55 | 2023-05-24 line 99 | ROW:G14+G15 | scored row | "**Kiran Mazumdar-Shaw, Executive Chairperson, Biocon Limited:** I think we have guided for mid-30%s to 40% margins."
- 56 | 2023-05-24 line 101 | RES:G14 | '35% to 40% is the range we've given': a stated number for G14 and G15; under it G14's 34% is a miss (the narrower window) | "**Kiran Mazumdar-Shaw, Executive Chairperson, Biocon Limited:** Well, 35% to 40% is the range we've given."
- 58 | 2023-05-24 line 111 | NEW:G25 | scored row | "**Siddharth Mittal, CEO & Managing Director, Biocon Limited:** So, generics R&D will be around 10% of segment revenues."
- 61 | 2023-11-10 line 22 | UNS | Vizag commercial supplies from FY25: a date; no filed first-supply date | "We now expect commercial supplies to begin in FY'25, post qualification of the site by global regulators."
- 63 | 2023-11-10 line 22 | NEW:G22+G23 | two guides in one sentence: Biologics US$1 billion and Syngene mid-teens | "Finally, and looking ahead to the full year, we remain on track to deliver US$1 billion revenue for Biocon Biologics, mid- Transcript - Biocon Limited Q2 FY24 Earnings Call Page"
- 66 | 2023-11-10 line 104 | ROW:G13 | scored row | "But on an overall basis, the guidance that I had given last year of mid-teens might be more titrated down to low teens to high single digits."
- 68 | 2024-02-09 line 22 | UNS | facility operational in H2 FY25 'subject to regulatory approvals': a date, no filed outcome read | "The facility is expected to be operational in the second half of FY '25, subject to regulatory approvals."
- 74 | 2024-05-16 line 22 | UNS | US facility to begin commercial operations in FY25: a date, no filed outcome read | "The acquisition of this FDA-approved facility, our first in the United States, will strategically enhance and complement Biocon’s existing manufacturing capabilities and is expected to begin commercial operations in fiscal"
- 76 | 2024-05-16 line 22 | NEW:G24 | scored row | "Behind this, we will continue to invest in advancing and building a highly competitive global pipeline and expect R&D investments to be in the 8% to 9% of revenues range."
- 78 | 2024-05-16 line 22 | UNS | facility qualification expected in H2 FY25: a date, no filed outcome read | "The completion of the facility modifications and qualification remain on track and are expected in the second half of fiscal ‘25."
- 80 | 2024-05-16 line 22 | ROW:G21 | scored row | "Syngene's guidance for fiscal '25 includes revenue growth at single digit to low double digits on a constant currency basis."
- 89 | 2024-05-16 line 86 | UNS | Liraglutide contributing from FY26: a date with no number, no filed outcome | "So, I think Peter also alluded to the fact that we expect Liraglutide to meaningfully start contributing to the growth from FY'26."
- 92 | 2024-08-09 line 20 | UNS | facility repurposing in H2 FY25: a date, as hit 78 | "The repurposing of the Biologics Manufacturing facility acquired from Stelis Biopharma remains on track for completion of qualification and facility modifications in the second half of fiscal 2025."
- 97 | 2024-08-09 line 44 | NEW:G27 | scored row | "For the overall year, we still expect like a high single-digit kind of growth levels for the business."
- 103 | 2025-01-31 line 30 | ROW:G17 | scored row | "And we continue to invest in R&D in that 6%, 7% to 9% range that we have guided."
- 109 | 2025-01-31 line 120 | ROW:G16 | scored row | "And directionally, what I have guided for is an EBITDA margin of 10% to 12%."
- 116 | 2025-05-09 line 73 | RES:G17 | 'For the full year, we had given a guidance of 7% to 9%' | "For the full year, we had given a guidance of 7% to 9%."
- 117 | 2025-05-09 line 75 | UNS | Biologics capex about US$100 million over the next couple of years: not due; only group capex is printed | "On the Capex side, like what you said, Surya, we expect to spend about USD 100 million over the next couple of years."
- 119 | 2025-05-09 line 99 | RES:G19 | scored row | "So these are the 5 products we expect to launch in that 12-to-18-month window."
- 120 | 2025-05-09 line 101 | UNS | 'a product a year from 25 to 30': a cadence to FY30, not due | "**Shreehas Tambe, Chief Executive Officer & Managing Director, Biocon Biologics Limited:** Nitin, in the past, we've said that -- I mean, apart from the bunching up that has happened in"
- 121 | 2025-08-08 line 21 | UNS | GLP-1 injectables commercial supply from FY27: a date, not due | "Facility Expansions and Strategic Capability Building • Our injectables facility primarily focused on GLP-1s has been commissioned with commercial supply expected to begin in FY '27."
- 123 | 2025-08-08 line 21 | UNS | Syngene 'FY26 guidance': the sentence has no number; the decks and releases say only 'on track' (searched calls 2025-05-09, 2025-08-08, 2025-11-12, the Q4 FY25 to Q4 FY26 releases and decks), so the numeric guide is not held | "Despite macroeconomic uncertainties, Syngene sees robust demand from large and midsized pharma clients and remains on track to deliver FY '26 guidance."
- 130 | 2025-08-08 line 97 | RES:G19 | scored row | "We've got five products ready for launch in the next 12 to 18 months is what we had guided."
- 135 | 2025-11-12 line 16 | RES:G19 | management's tally of the launches delivered | "• In Q4 FY '25, we had guided to launch five biosimilar products over the next 12 to 18 months, and I'm pleased to report that we have delivered on"
- 137 | 2025-11-12 line 16 | UNS | Syngene 'maintaining its annual guidance for FY26': numeric guide not held (see hit 123) | "The performance in the first half has been in line with expectations, and Syngene is maintaining its annual guidance for FY '26."
- 138 | 2025-11-12 line 28 | ROW:G20 | scored row | "**Shreehas Tambe, Chief Executive Officer & Managing Director, Biocon Biologics Limited:** We've said, Tushar, that we would be in that 7% to 9% of revenues for R&D, and we continue"
- 139 | 2025-11-12 line 30 | NEW:G28 | scored row | "And I expect it to be in a similar trajectory of 8% to 10% of revenues."
- 141 | 2026-02-13 line 25 | ROW:G18 | scored row | "In fact, you will see that those margins have been higher than what our guidance has been in the mid-20s."
- 142 | 2026-02-13 line 73 | UNS | drug-product facility commercial in FY27, substance expansion 1 to 1.5 years later: dates, not due | "If that is your question, then the drug product is expected to go commercial in the coming fiscal, which is fiscal '27, and the drug substance expansion, which is also"
- 150 | 2026-08-06 line 21 | UNS | Syngene FY27: single-digit revenue degrowth and margin back to mid-20s; FY27 ends 2027-03-31, so the outcome is not due | "While revenues are expected to decline in the first half, performance should improve in the second half, resulting in a single-digit revenue degrowth in rupee terms for the full year"
- 152 | 2026-08-06 line 33 | UNS | 'in the mid-20s, and it will ramp up': entity and year not stated in the sentence; FY27 not due | "**Shreehas Tambe, Chief Executive Officer & Managing Director, Biocon Limited:** We have always directed this to say we will be in the mid-20s, and it will ramp up."

Hits that are not numeric guides (OUT reports an outcome of a scored guide; NOT is excluded by the rule): hit number, call date, line, tag, reason, quote.

- 2 | 2022-11-15 line 23 | NOT | partner's trial data date | "The study continues to enroll patients, with top line data expected in mid-2023."
- 10 | 2023-02-15 line 22 | NOT | the only digits are a page number | "Transcript - Biocon Limited Q3FY23 Earnings Call Page 3 of 32 There are several upcoming launches, including biosimilar"
- 11 | 2023-02-15 line 22 | NOT | the only digits are a page number; no number target | "With respect to our Visakhapatnam project, we continue to make progress in terms of our greenfield Transcript -"
- 13 | 2023-02-15 line 22 | NOT | the only digits are a page number | "On the regulatory front, the US FDA has accepted our CAPA plan pertaining to the pre-approval inspections of"
- 14 | 2023-02-15 line 22 | NOT | a partner's data date | "Enrolment also continues in the Phase 1b clinical study of Itolizumab for Lupus Nephritis and Equillium expects to"
- 15 | 2023-02-15 line 22 | NOT | no number target ('healthy growth') | "Concluding Remarks I would like to conclude by saying that we expect to end FY23 on a strong"
- 19 | 2023-02-15 line 94 | NOT | payors' plans, not a company target | "Each of the payors have said that they will have at least a biosimilar plus 1 or plus"
- 21 | 2023-02-15 line 102 | NOT | a shareholding level, not a result target | "**Siddharth Mittal, CEO & Managing Director, Biocon Limited:** I wouldn't call it as a one-off, our shareholding is"
- 23 | 2023-02-15 line 138 | NOT | no number target (digits from a page header) | "From SG&A point Transcript - Biocon Limited Q3FY23 Earnings Call Page 19 of 32 of view, the Viatris"
- 24 | 2023-02-15 line 140 | NOT | a current prescription share, an observation | "Going forward, what we really see, and you're seeing that in the indices that you mentioned, which is"
- 25 | 2023-02-15 line 146 | NOT | no number target (the digits are a year) | "So, what was a steeper price erosion last year, we're seeing normalizing trend and I also mentioned that"
- 26 | 2023-02-15 line 156 | NOT | an analyst's words inside the block, restating the Serum guide of hit 9 | "Nithya Balasubramanian: One last quick one, if I may, on the SII deal, I think your guidance was"
- 27 | 2023-02-15 line 156 | NOT | an analyst's words inside the block (margin guidance of 35%) | "Now we know that the COVID vaccine demand has come off so I'm Transcript - Biocon Limited Q3FY23"
- 28 | 2023-02-15 line 160 | NOT | a market size | "We see a huge opportunity in peptide I mean today the peptide market is growing to US$ 15"
- 29 | 2023-02-15 line 160 | NOT | a third party's launch timing | "But from whatever at least is available in public domain, we have heard that the launch is expected"
- 31 | 2023-02-15 line 166 | NOT | '181' is the 181-day rule, not a target | "We're of course late to be in NCE minus one ﬁler but we do expect to ﬁle in"
- 32 | 2023-02-15 line 166 | NOT | a market size | "The other drug that we are working on and again at different stages of development is Tirzepatide, as"
- 35 | 2023-02-15 line 196 | NOT | no number target | "So, I do not expect any signiﬁcant impact in FY '24 from these large facilities or OpEx coming"
- 38 | 2023-02-15 line 206 | NOT | no target | "We are down to 54.9% but we do not have any plans."
- 39 | 2023-05-24 line 21 | NOT | a contract's value (a third-party contract) | "Syngene delivered a strong performance led by its manufacturing services business, which includes the signing of a 10-year"
- 40 | 2023-05-24 line 21 | NOT | no number target | "We remain on track to integrate a major part of the acquired biosimilars business, region-wise, in a phased"
- 41 | 2023-05-24 line 21 | NOT | a fund-raise with no amount | "Whilst the present debt level can be comfortably serviced, we plan to raise additional equity at the BBL"
- 42 | 2023-05-24 line 21 | OUT:G5 | reports Generics 13% 'in line with our guidance' | "For the full-year, the Generics segment recorded an operating revenue of ₹2,637 crores, delivering a growth of 13%"
- 45 | 2023-05-24 line 21 | OUT:G1 | reports Biologics R&D 16% against 'our guidance of 12%' | "Net R&D spend for the year was at 16%, which is higher than our guidance of 12% on"
- 48 | 2023-05-24 line 21 | NOT | no number target (Phase 1b) | "The Phase 1b clinical study for Lupus Nephritis also remains on track."
- 49 | 2023-05-24 line 21 | NOT | a partner's data date | "Equillium expects to report top-line data from the EQUALISE study on Lupus Nephritis in the first half of"
- 50 | 2023-05-24 line 21 | NOT | a holding level after a third party's financing | "It is expected to reduce to a little over 23% post receipt of the full amount from the"
- 53 | 2023-05-24 line 69 | NOT | no number target (an inspection) | "So hopefully in FY '24, we are expecting to be inspected and approved."
- 54 | 2023-05-24 line 83 | NOT | a third party's financing | "I think once the Bicara raises the remaining $70 million, which is expected sometime this quarter, Biocon would"
- 57 | 2023-05-24 line 103 | NOT | a holding floor | "**Kiran Mazumdar-Shaw, Executive Chairperson, Biocon Limited:** So, we've already indicated we do not plan to reduce below this"
- 59 | 2023-05-24 line 117 | NOT | a partner's trial | "**Siddharth Mittal, CEO & Managing Director, Biocon Limited:** Well, the clinical trial is ongoing for acute graft-versus-host disease,"
- 60 | 2023-05-24 line 117 | NOT | a partner's filing date | "As I mentioned, the filing is expected somewhere in CY25, followed by a review process."
- 62 | 2023-11-10 line 22 | OUT:G14 | 34% 'in line with our mid-30s guidance' | "This has translated into a core EBITDA of ₹660 crores with margins of 34%, in line with our"
- 64 | 2023-11-10 line 38 | NOT | market timing, no company result target | "We had obviously guided for a slower 2023 with pick up beginning in '24 and '25 being the"
- 65 | 2023-11-10 line 50 | NOT | no number target | "So, once we have clarity on what exactly it is that they expect you to do, we will"
- 67 | 2024-02-09 line 22 | OUT:G15 | 28% 'lower than our guidance of mid-30s' | "This margin is lower than our guidance of mid-30s on account of the series of integration-related expenses and"
- 69 | 2024-02-09 line 36 | NOT | a debt pay-down already done | "As I said earlier, we've reduced that by $200 million in the quarter."
- 70 | 2024-02-09 line 64 | NOT | market timing | "If you note what we had said, even in the past, that we see the market opening up"
- 71 | 2024-02-09 line 64 | NOT | market timing | "And we were expecting to see that anyway in '25."
- 72 | 2024-02-09 line 78 | NOT | a debt pay-down already done | "So, as I said in my opening remarks, I mean, clearly, looking at the balance sheet, it is"
- 73 | 2024-05-16 line 22 | NOT | 35% is an outcome; 'overtake APIs' has no number | "During the fiscal, formulation share of product sales increased to approximately 35% from 25% last year, and it"
- 75 | 2024-05-16 line 22 | NOT | no number target | "As we look ahead, formulations are expected to be the key growth driver for fiscal ‘25, and we"
- 77 | 2024-05-16 line 22 | NOT | a partner's option date | "Their option decision is expected in the second half of CY’24."
- 79 | 2024-05-16 line 22 | NOT | no number target | "biotech is encouraging and is expected to Transcript - Biocon Limited Q4 FY24 Earnings Call Page 9 of"
- 81 | 2024-05-16 line 22 | NOT | no number target | "So, in conclusion, as I said, for Biocon as a group, fiscal'24 has been a year characterized by"
- 82 | 2024-05-16 line 22 | NOT | no number target | "So, looking to fiscal ‘25, we expect it to be a year of both consolidation and of transitional"
- 83 | 2024-05-16 line 32 | NOT | market timing | "And as I said in my commentary, we don't really see the market opening up in calendar '24,"
- 84 | 2024-05-16 line 34 | NOT | market timing | "We are aggressively pursuing these opportunities, and we do see some opportunities lifting and will be in position"
- 85 | 2024-05-16 line 48 | NOT | no number target | "We have had good success and approvals, and we expect to see that momentum continue and that will"
- 86 | 2024-05-16 line 52 | NOT | no number target | "And we would expect that growth momentum to continue during fiscal '25."
- 87 | 2024-05-16 line 52 | NOT | no number target | "But we have seen extremely robust demand for our products, and that’s reflected in very high-volume pickup in"
- 88 | 2024-05-16 line 60 | NOT | no number target | "As I said in my remarks, Surya, I think you'll see -- as you've identified in Q4, a"
- 90 | 2024-08-09 line 20 | NOT | no number target | "In line with our previous guidance, we expect the quarter 1 trends to continue into quarter 2 before"
- 91 | 2024-08-09 line 20 | OUT:G21 | Syngene Q1 'in line with its guidance' | "Overall, Syngene's first quarter performance is in line with its guidance and commentary given in its Q4 fiscal"
- 93 | 2024-08-09 line 30 | NOT | a market timeline | "Amey, if you go back to the commentary that we had shared on how we see this market"
- 94 | 2024-08-09 line 30 | NOT | a market timeline | "2024 is when we set the market, and that was calendar 2024 is when we said market will"
- 95 | 2024-08-09 line 38 | NOT | a regulator's response time | "We expect them to come back typically in the 60 to 90-day time frame, but there is no"
- 96 | 2024-08-09 line 44 | NOT | no number target | "And there are various other markets, which, where we expect to launch the product during this fiscal year.GLP-1"
- 98 | 2024-08-09 line 48 | NOT | no number target | "But the volume of business that we are targeting over the next 5 years, we will have capacities"
- 99 | 2024-08-09 line 76 | NOT | a past fact | "And as I said earlier, I mean, clearly, we have been comfortably servicing the debt for the last"
- 100 | 2024-08-09 line 76 | NOT | a debt pay-down already done | "We took action last year, as I said earlier, with a USD 250 million reduction on the acquisition"
- 101 | 2025-01-31 line 20 | NOT | no number target | "Looking ahead, we expect performance in the fourth quarter and into the next fiscal to build upon the"
- 102 | 2025-01-31 line 30 | NOT | no number target | "We had also said and guided in the past that growth will come from new geographies that we"
- 104 | 2025-01-31 line 82 | NOT | a debt closure already done | "And like we have said, we have been able to close out the entire USD 335 million, USD"
- 105 | 2025-01-31 line 94 | NOT | a customer's tender timing | "And I think we are expecting that tender to open sometime end of this calendar year with supplies"
- 106 | 2025-01-31 line 102 | NOT | a market size | "And if I may add one more thing that we know the volume of the market opportunity for"
- 107 | 2025-01-31 line 104 | NOT | other companies' timing | "We expect even if it's not in 2026, but 2027, 2028, that time period, there will be many"
- 108 | 2025-01-31 line 118 | NOT | no rate stated; '2 to 3 years' is only a horizon | "So, sum total of all, we definitely expect a good growth over the next 2 to 3 years."
- 110 | 2025-05-09 line 23 | NOT | a date fixed by a settlement agreement with a third party | "• The settlement with Regeneron to secure a market entry date for Yesafili™, our biosimilar Aflibercept in the"
- 111 | 2025-05-09 line 23 | NOT | a partner's start date | "We also commenced supplies of Tacrolimus to China, where our partner is expected to initiate commercialization in the"
- 112 | 2025-05-09 line 23 | OUT:G21 | Syngene FY25 growth 4% 'aligning with guidance' | "For FY'25, Revenue from Operations grew 4% to INR 3,642 crores, aligning with guidance following a challenging first"
- 113 | 2025-05-09 line 47 | NOT | a current level | "And as of March,'25, as I said, it's lower than 280."
- 114 | 2025-05-09 line 65 | NOT | a past event | "We have seen the originator product, in this case, stay on longer than expected, which is why you"
- 115 | 2025-05-09 line 71 | NOT | no number target | "So if you look at it, it's more than 20 years and the product continues to grow, and"
- 118 | 2025-05-09 line 83 | NOT | a fund-raise size | "I think what we have announced is that we intend to raise INR 4,500 crores through a combination"
- 122 | 2025-08-08 line 21 | NOT | no number target | "And while these costs impact margins in the near term, these new capacities are expected to deliver strong"
- 124 | 2025-08-08 line 55 | NOT | no number target | "And we want to be in a position, and we believe we will be in a position to"
- 125 | 2025-08-08 line 73 | NOT | a regulator's approval timing | "And we are expecting early approvals in some of the markets where we'll file this quarter by end"
- 126 | 2025-08-08 line 73 | NOT | other companies' timing | "So while the market, as you rightly said, is going to open up in calendar '26, we do"
- 127 | 2025-08-08 line 85 | NOT | a regulator's approval timing | "**Siddharth Mittal, CEO & Managing Director, Biocon Limited:** So as I addressed the previous question that we will"
- 128 | 2025-08-08 line 87 | NOT | a regulator's approval timing | "But as I mentioned that given Health Canada has not approved a single generic GLP-1, we do best"
- 129 | 2025-08-08 line 91 | NOT | no number target | "But as I said, that the impact of all these new launches and increase in gross margin would"
- 131 | 2025-08-08 line 101 | NOT | a past market share | "I talked about it in Q3 of last fiscal where we had said, we have a very good"
- 132 | 2025-08-08 line 101 | NOT | a past growth rate | "And if you look at the recent reported market shares, our Oncology portfolio, led by Abevmy, which is"
- 133 | 2025-11-12 line 16 | NOT | a past result | "Both biosimilars and generics delivered double-digit Y-on-Y growth, while the CRDMO business reported performance in line with plan."
- 134 | 2025-11-12 line 16 | NOT | no number target | "• We have already started to see margin improvement in Q2 following the Goldman Sachs exit, and we"
- 136 | 2025-11-12 line 16 | NOT | no number target | "CRDMO Q2FY26 Update Syngene's performance in Q2 was in line with plan."
- 140 | 2026-02-13 line 21 | NOT | a past result; the tally is listed in G19's evidence | "Over the last 9 months, we have successfully launched Yesintek, which is our biosimilar Ustekinumab, Kirsty, our biosimilar"
- 143 | 2026-05-08 line 20 | OUT:G18 | Syngene's 25% 'in line with revised guidance'; its numeric guide is not held, so this is no longer G18's outcome | "• Operating EBITDA margin at 25% for the year was in line with Syngene's revised full year guidance."
- 144 | 2026-05-08 line 20 | NOT | no number target | "As we look ahead to FY '27, we expect to increasingly benefit from the foundations that have been"
- 145 | 2026-05-08 line 24 | NOT | 'not guided specifically on any numbers' | "And while we've not guided specifically on any numbers, I think the fact that we've got several products"
- 146 | 2026-05-08 line 24 | NOT | no number target | "And we've said that fiscal '27, '28 as we get towards the later part of the year, we'll"
- 147 | 2026-05-08 line 88 | NOT | a description of the mix, not a target | "In the past, we have said North America is about 40%, Europe and a little bit of Japan,"
- 148 | 2026-05-08 line 100 | NOT | a market size | "**Shreehas Tambe, Chief Executive Officer & Managing Director, Biocon Limited:** From a dollar number perspective, I think we"
- 149 | 2026-08-06 line 21 | NOT | no number target | "Q1 performance was broadly in line with our expectations, and we expect momentum to build progressively through the"
- 151 | 2026-08-06 line 21 | NOT | no number target | "These actions are expected to position Syngene for a return to profitable and sustainable growth from FY'28."

### 9. G19: the evidence per launch

G19's guide (2025-05-08): 'positioned to launch 5 new products in the next 12-18 months'. Window end = 2025-05-08 + 18 months = 2026-11-08 (DERIVED). The class 'in line' rests on the END date only: the fifth launch is filed 2026-04-07, and the other four are filed as launched by 2026-02-12 or earlier. Whether each launch also falls AFTER 2025-05-08 (the start of the window) is not tested by the rule and not all of it can be shown:

- bUstekinumab (Yesintek):
  - US launch filed 2025-02-24, BEFORE the 2025-05-08 guide date: data/filings/text/2025-02-24_BioconLtd_24022025170016_Cover_Letter_pressrelease/p002.txt line 8: "Biocon Biologics Launches Yesintek™ (ustekinumab-kfce)"
  - the guide-date release itself calls it the fifth biosimilar launched in the US: data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p007.txt line 47: "The Company has launched its fifth biosimilar product in the U.S., Yesintek™"
  - Europe launch, undated, in the Q1 FY26 release (April to June 2025): data/filings/text/2025-08-07_Biocon2_07082025203305_CoveringLetterPressRelease07082025/p007.txt line 30: "Yesintek™ was launched in key European countries"
- bAspart (Kirsty):
  - US approval, Q1 FY26 release: data/filings/text/2025-08-07_Biocon2_07082025203305_CoveringLetterPressRelease07082025/p007.txt line 41: "FDA approval for Kirsty™"
  - listed as launched, undated, in the Q3 FY26 release filed 2026-02-12: data/filings/text/2026-02-12_BIOCON_12022026194149_Press_Release12022026/p003.txt line 35: "launches of Yesintek (bUstekinumab), Kirsty (bAspart), Jobevne (bBevacizumab), and Yesafili (bAflibercept)"
- bBevacizumab (Jobevne):
  - US approval, FY25 release of 2025-05-08: data/filings/text/2025-05-08_Biocon2_08052025194632_PressRelease/p008.txt line 9: "the U.S. FDA has approved Jobevne™ (bevacizumab-nwgd)"
  - listed as launched, undated, in the Q3 FY26 release filed 2026-02-12 (same line as above): data/filings/text/2026-02-12_BIOCON_12022026194149_Press_Release12022026/p003.txt line 35: "Jobevne (bBevacizumab)"
- bAflibercept (Yesafili):
  - Canada launch scheduled for 2025-07-04 (filed 2025-06-27): data/filings/text/2025-06-27_Biocon2_27062025091834_SEIntimation27062025/p002.txt line 17: "way for the launch of YESAFILI in Canada, scheduled for July 4, 2025"
  - launched in Canada, undated, Q1 FY26 release: data/filings/text/2025-08-07_Biocon2_07082025203305_CoveringLetterPressRelease07082025/p007.txt line 22: "Yesafili™ was launched in Canada"
- bDenosumab (Bosaya):
  - US launch announced 2026-04-07 (the filing's date): data/filings/text/2026-04-07_BIOCON_07042026160635_Pressrelease07042026/p002.txt line 16: "today announced the commercial launch of Bosaya"
  - FY26 release (filed 2026-05-07): data/filings/text/2026-05-07_BIOCON_07052026233651_Covering_Letter_Press_Release/p006.txt line 19: "The Company launched Bosaya™ and Aukelso ™, the Denosumab biosimilars"

Reading: a dated filed launch exists for 1 of 5 (Denosumab, 2026-04-07); Yesafili has a dated schedule (Canada, 2025-07-04) and an undated 'launched'; Aspart and Bevacizumab are filed as launched with no date (2026-02-12 release); Ustekinumab's US launch (2025-02-24) is BEFORE the guide date, so only its undated European launch could fall inside the window. None of the five rests on management's tally alone: every one has a filed statement. The management tally (2025-11-12 line 16, 2026-02-13 line 21) agrees with them and is not needed.

## Still not held
- Calls before 2022-04 (including the FY21 and FY22 earlier quarters).
- The numeric Syngene FY26 guide (calls and decks say only 'on track' or 'maintaining'), so Syngene's FY26 outcome cannot be scored; the 25% margin of 2026-05-08 is no longer paired with any guide.
- Constant-currency Syngene FY24 and FY25 growth (guide basis); only reported growth is held. Dated launches for Aspart, Bevacizumab and Ustekinumab-Europe. Generics-only R&D in FY23 as a filed figure (only a group-minus-BBL bound is held). Generics-only and Biologics-only capex.
- Management words without a number outside the windows above (for example 'ramp up', 'robust') are not scored.
