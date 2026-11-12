# Read-held G28 (BIOCON): rows L5-46, L4-48, L4-30, L5-58

Source folder: docs/idea/case-study/BIOCON/data/feed-fetched (groups feed-press, feed-acquisition, feed-newsverif). The 27 older 2021 press releases (data/fetched) were read by g45 and are not redone here. No row is graded or closed by this file. Third-party figures: none used. Thresholds: none applied (L5-46 'Number: none as a rule'; L4-30 'Number: None stated'; L5-58 'Number: none stated'; L4-48's one rule of thumb, target not larger than buyer, is not tested here).

## L5-46

Step ask (FC-L5-T3-S3): each contract, supply or JV announcement: value, customer, start. Done-when: each announcement in the last year has value, share of revenue, customer and start date in one row.

### Tally

- feed-press fetch log: 134 rows = 131 read as text + 2 image-only PDFs not read (FD01_004 CHMP Inpremzia and FD01_007 Abevmy Canada launch, titles taken from the URL only, neither is a contract title) + 1 HTTP error (the 2022-04-26 'Insugen awarded a three-year contract by Ministry of Health Malaysia' release, a clear contract title, 404, NOT read).
- Of the 131 read, 16 are contract, supply, licence or settlement-and-licence announcements (table below), 1 is an MoU with no commercial terms, and the rest by subject line are results, awards, approvals, launches, appointments, ratings, integration steps or fundraising. Acquisitions and the divestment to Eris (FD01_043) are not listed here (acquisitions are under L4-48).
- Among the 16: counterparty named 16 of 16; a contract value stated 1 of 16 (FD01_128 only; a value of 'terms confidential/not disclosed' counts as not stated); a start date stated 3 of 16; share of revenue stated 0 of 16 (no release prints an order value against revenue).
- Not closed: 2 image-only releases and 1 404 release unread; share of revenue not computable from held text (see 'still not held').

### Contract rows

| id | contract | printed date | feed filing time | days printed to feed |
|---|---|---|---|---|
| FD01_013 | Out-licence of bUstekinumab and bDenosumab to Yoshindo (Japan) | 2022-10-17 | 2022-10-17 08:30:57 | 0 |
| FD01_017 | Semi-exclusive partnership with Zentiva (Liraglutide, 30 countries in Europe) | 2022-11-23 | 2022-11-23 22:09:21 | 0 |
| FD01_040 | Partnership agreement with Juno Pharmaceuticals (Liraglutide, Canada) | 2023-10-06 | 2023-10-06 16:04:51 | 0 |
| FD01_050 | Distribution agreement with Sandoz for Adalimumab BS (FKB) in Japan | 2023-12-22 | 2023-12-22 16:01:49 | 0 |
| FD01_053 | Five-year distribution partnership with Sandoz (Trastuzumab, Bevacizumab, Australia) | 2024-02-09 | 2024-02-09 08:00:49 | 0 |
| FD01_057 | Exclusive licensing and supply agreement with Biomm (Semaglutide, Brazil) | 2024-04-17 | 2024-04-17 18:30:10 | 0 |
| FD01_058 | Semi-exclusive distribution and supply deal with Medix (Liraglutide, Mexico) | 2024-05-13 | 2024-05-13 07:53:24 | 0 |
| FD01_061 | Exclusive licensing and supply deal with Handok (Liraglutide, South Korea) | 2024-05-24 | 2024-05-24 08:18:35 | 0 |
| FD01_065 | Licensing and supply agreement with Tabuk (GLP-1 products, Middle East) | 2024-09-26 | 2024-09-26 16:30:53 | 0 |
| FD01_084 | Strategic collaboration agreement with Civica (Insulin Aspart drug substance, US) | 2025-03-06 | 2025-03-06 17:32:30 | 0 |
| FD01_107 | Multi-year private-label Insulin Glargine agreement with Civica (US) | 2025-10-16 | 2025-10-16 15:50:47 | 0 |
| FD01_113 | Settlement and licence agreement on Aflibercept (Regeneron, Bayer) | 2025-12-13 | 2025-12-13 13:40:56 | 0 |
| FD01_116 | Expanded in-licensing of Adalimumab (Hulio) from Fujifilm Kyowa Kirin Biologics | 2025-12-23 | 2025-12-23 09:11:32 | 0 |
| FD01_117 | Out-licensing of Semaglutide to Ajanta (26 countries) | 2025-12-23 | 2025-12-23 17:34:31 | 0 |
| FD01_128 | Malaysian Ministry of Health insulin contracts via Duopharma | 2026-06-24 | 2026-06-24 08:33:42 | 0 |
| FD01_132 | 10-year Pertuzumab supply contract, Brazil (Bahiafarma, Bionovis) | 2026-09-08 | 2026-09-08 08:31:17 | 0 |

(Feed time is the NSE row's sort_date; days = DERIVED as feed date minus printed date. Used again under L5-58.)

#### FD01_013 Out-licence of bUstekinumab and bDenosumab to Yoshindo (Japan)

- Date: FD01_013_BIOCON_17102022083057_Intimation_PressRelease_1710/p002.txt line 13: "Bengaluru, India, October 17, 2022"
- Value: upfront fee and milestones unquantified; terms confidential (next line); the ~USD 700 million in the title is addressable market, not a contract value. Source: FD01_013_BIOCON_17102022083057_Intimation_PressRelease_1710/p002.txt line 24: "development milestones over the next few years. The financial terms of the agreement"
- Customer or counterparty: Yoshindo Inc. (licensee). Source: FD01_013_BIOCON_17102022083057_Intimation_PressRelease_1710/p002.txt line 17: "Japanese pharmaceuticals company Yoshindo Inc. for commercializing two of its pipeline"
- Start: not stated (no start date; 'Once approved' is the only timing words).

#### FD01_017 Semi-exclusive partnership with Zentiva (Liraglutide, 30 countries in Europe)

- Date: FD01_017_BIOCON_23112022220921_Intimation_PressRelease/p002.txt line 9: "Bengaluru, Karnataka, India. November 23, 2022"
- Value: not stated (no value printed).
- Customer or counterparty: Zentiva (distributor). Source: FD01_017_BIOCON_23112022220921_Intimation_PressRelease/p002.txt line 12: "agreement with Zentiva, a leading pharmaceutical company in Europe, for the"
- Start: not stated (no start date printed).

#### FD01_040 Partnership agreement with Juno Pharmaceuticals (Liraglutide, Canada)

- Date: FD01_040_BIOCON_06102023160451_PressRelease_signed/p002.txt line 10: "Bengaluru, Karnataka, India. October- 06, 2023"
- Value: not stated (no value printed; the US $100 million is the market size, not a contract value).
- Customer or counterparty: Juno Pharmaceuticals (distributor). Source: FD01_040_BIOCON_06102023160451_PressRelease_signed/p002.txt line 13: "Juno Pharmaceuticals, a specialty pharmaceutical company in Canada, for the"
- Start: not stated (no start date; Biocon first has to obtain regulatory approval).

#### FD01_050 Distribution agreement with Sandoz for Adalimumab BS (FKB) in Japan

- Date: FD01_050_BIOCON_22122023160149_PressRelease22122023/p002.txt line 11: "Bengaluru, India: December 22, 2023"
- Value: not stated (no value printed).
- Customer or counterparty: Sandoz (distributor). Source: FD01_050_BIOCON_22122023160149_PressRelease22122023/p002.txt line 14: "signed today a Distribution Agreement with Sandoz, granting the"
- Start: Sandoz takes over responsibilities from 2024-02-15 (transition start, as printed). Source: FD01_050_BIOCON_22122023160149_PressRelease22122023/p002.txt line 18: "will gradually assume responsibilities for the product starting February 15, 2024."

#### FD01_053 Five-year distribution partnership with Sandoz (Trastuzumab, Bevacizumab, Australia)

- Date: FD01_053_BIOCON_09022024080050_PressRelease_090224_signed.p/p002.txt line 11: "BENGALURU, Karnataka, India, February 9, 2024"
- Value: not stated (no contract value; the AUD$35 million and AUD$45 million are market values).
- Customer or counterparty: Sandoz AG (distributor). Source: FD01_053_BIOCON_09022024080050_PressRelease_090224_signed.p/p002.txt line 15: "which provides Sandoz the exclusive rights to promote, sell and distribute biosimilar"
- Start: effective 2024-01-01, commercialisation from 2024-02-01 (the year is on the next line). Source: FD01_053_BIOCON_09022024080050_PressRelease_090224_signed.p/p002.txt line 25: "The agreement is effective from January 1, 2024 and commercialisation commenced on February 1,"

#### FD01_057 Exclusive licensing and supply agreement with Biomm (Semaglutide, Brazil)

- Date: FD01_057_BIOCON_17042024183011_PressRelease_170424_signed.p/p002.txt line 10: "Bengaluru, Karnataka, India. April- 17th, 2024"
- Value: not stated (no value printed; the US $580 million is market size).
- Customer or counterparty: Biomm S.A. (licensee). Source: FD01_057_BIOCON_17042024183011_PressRelease_170424_signed.p/p002.txt line 13: "supply agreement with Biomm S.A., a specialty pharmaceutical company in Brazil"
- Start: not stated (no start date printed).

#### FD01_058 Semi-exclusive distribution and supply deal with Medix (Liraglutide, Mexico)

- Date: FD01_058_BIOCON_13052024075324_PressRelease_130524_signed.p/p002.txt line 9: "Bengaluru, Karnataka, India. May- 13, 2024"
- Value: not stated (no value printed; US $37 million is market size).
- Customer or counterparty: Medix (distributor). Source: FD01_058_BIOCON_13052024075324_PressRelease_130524_signed.p/p002.txt line 12: "and supply agreement with Medix, a specialty pharmaceutical company in Mexico"
- Start: not stated (no start date printed).

#### FD01_061 Exclusive licensing and supply deal with Handok (Liraglutide, South Korea)

- Date: FD01_061_BIOCON_24052024081835_PressRelease/p002.txt line 10: "Bengaluru, Karnataka, India. May - 24, 2024"
- Value: not stated (no value printed; US $47 million is market size).
- Customer or counterparty: Handok (licensee). Source: FD01_061_BIOCON_24052024081835_PressRelease/p002.txt line 13: "supply agreement with Handok, a specialty pharmaceutical company in South Korea, for the"
- Start: not stated (no start date printed).

#### FD01_065 Licensing and supply agreement with Tabuk (GLP-1 products, Middle East)

- Date: FD01_065_BIOCON_26092024163054_PressRelease_signed/p002.txt line 8: "Bengaluru, Karnataka, India: September 26, 2024"
- Value: not stated (no value printed).
- Customer or counterparty: Tabuk Pharmaceutical Manufacturing Company (distributor). Source: FD01_065_BIOCON_26092024163054_PressRelease_signed/p002.txt line 10: "agreement with Tabuk Pharmaceutical Manufacturing"
- Start: not stated (no start date printed).

#### FD01_084 Strategic collaboration agreement with Civica (Insulin Aspart drug substance, US)

- Date: FD01_084_BioconLtd_06032025173219_Pressrelease_signed/p002.txt line 12: "March 6, 2025"
- Value: not stated (no value printed).
- Customer or counterparty: Civica, Inc. (customer). Source: FD01_084_BioconLtd_06032025173219_Pressrelease_signed/p003.txt line 36: "Civica is a non-profit generic pharmaceutical company established in 2018"
- Start: not stated (no start date printed).

#### FD01_107 Multi-year private-label Insulin Glargine agreement with Civica (US)

- Date: FD01_107_Biocon2_16102025155008_Cover_Letter_pressrelease.p/p002.txt line 15: "BRIDGEWATER, N.J. and BENGALURU, Karnataka, India: October 16, 2025"
- Value: terms not disclosed (the line before reads 'Additional terms'). Source: FD01_107_Biocon2_16102025155008_Cover_Letter_pressrelease.p/p002.txt line 40: "of the agreement are not disclosed."
- Customer or counterparty: Civica (distributor). Source: FD01_107_Biocon2_16102025155008_Cover_Letter_pressrelease.p/p002.txt line 22: "The multi-year transformational agreement between Biocon Biologics and Civica creates an"
- Start: not stated (no start date; 'multi-year' is the only duration words).

#### FD01_113 Settlement and licence agreement on Aflibercept (Regeneron, Bayer)

- Date: FD01_113_BIOCON_13122025133818_Cover_Letter_pressrelease.pd/p002.txt line 10: "BENGALURU, India: December 13, 2025"
- Value: terms confidential. Source: FD01_113_BIOCON_13122025133818_Cover_Letter_pressrelease.pd/p002.txt line 26: "settlement are confidential."
- Customer or counterparty: Regeneron and Bayer (litigation counterparties, licensors). Source: FD01_113_BIOCON_13122025133818_Cover_Letter_pressrelease.pd/p002.txt line 23: "Biocon Biologics, Regeneron and Bayer executed the agreement to dismiss all pending litigation."
- Start: UK launch enabled from 2026-01; rest of settled countries 2026-03 on the next line. Source: FD01_113_BIOCON_13122025133818_Cover_Letter_pressrelease.pd/p002.txt line 24: "agreement enables the Company to launch YESAFILI in the United Kingdom in January 2026"

#### FD01_116 Expanded in-licensing of Adalimumab (Hulio) from Fujifilm Kyowa Kirin Biologics

- Date: FD01_116_BIOCON_23122025090823_PressRelease_23122025/p002.txt line 9: "Bengaluru, Karnataka, India: December 23, 2025"
- Value: not stated (no value printed).
- Customer or counterparty: Fujifilm Kyowa Kirin Biologics (licensor). Source: FD01_116_BIOCON_23122025090823_PressRelease_23122025/p002.txt line 13: "from Fujifilm Kyowa Kirin Biologics"
- Start: not stated (no start date; 'Commercial production ... will commence' follows tech transfer and approvals).

#### FD01_117 Out-licensing of Semaglutide to Ajanta (26 countries)

- Date: FD01_117_BIOCON_23122025173405_Cover_Letter_pressrelease.pd/p002.txt line 10: "Bengaluru, Karnataka, India. December 23, 2025"
- Value: not stated (no value printed).
- Customer or counterparty: Ajanta (licensee). Source: FD01_117_BIOCON_23122025173405_Cover_Letter_pressrelease.pd/p002.txt line 17: "Ajanta for exclusive marketing in 23 countries and semi- exclusive marketing in 3 countries"
- Start: not stated (no start date printed).

#### FD01_128 Malaysian Ministry of Health insulin contracts via Duopharma

- Date: FD01_128_BIOCON_24062026083309_Pressrelease24062026-signed./p002.txt line 11: "Johor, Malaysia – June 24, 2026"
- Value: over MYR 225 million; parts: three-year ~MYR 155.27 million human insulin, two-year ~MYR 18 million glargine and ~MYR 52.5 million aspart (extra quotes below). Source: FD01_128_BIOCON_24062026083309_Pressrelease24062026-signed./p002.txt line 16: "valued at over MYR 225 million this year"
- Customer or counterparty: Duopharma (M) Sendirian Berhad (customer; end buyer is the Ministry of Health). Source: FD01_128_BIOCON_24062026083309_Pressrelease24062026-signed./p002.txt line 18: "insulin, insulin glargine and in sulin aspart to Duopharma (M) Sendirian Berhad for distribution"
- Start: not stated (no start date printed).
- Extra line: FD01_128_BIOCON_24062026083309_Pressrelease24062026-signed./p002.txt line 22: "The contracts comprise a three-year agreement valued at ~ MYR 155.27 million for human insulin, along"
- Extra line: FD01_128_BIOCON_24062026083309_Pressrelease24062026-signed./p002.txt line 23: "with two 2 -year agreements: ~ MYR 18 million for insulin glargine and ~ MYR 52.5 million for insulin"

#### FD01_132 10-year Pertuzumab supply contract, Brazil (Bahiafarma, Bionovis)

- Date: FD01_132_BIOCON_08092026083042_Pressrelease08092026/p002.txt line 8: "Bengaluru, Karnataka, India: September 8, 2026:"
- Value: not stated (no number; only 'milestone payments and a share of revenues').
- Customer or counterparty: Bahiafarma and Bionovis (consortium partners). Source: FD01_132_BIOCON_08092026083042_Pressrelease08092026/p002.txt line 11: "partnership agreement with Bahiafarma and Bionovis for"
- Start: not stated (no start date; term is 10 years (quote below)).
- Extra line: FD01_132_BIOCON_08092026083042_Pressrelease08092026/p002.txt line 23: "Biocon will receive milestone payments and a share of revenues generated from the Brazil PDP"

#### Partnership or MoU with no commercial terms

- FD01_092 MoU with National Cancer Society Malaysia (patient assistance): date FD01_092_Biocon2_24062025085406_SEPressrelase-24062025/p002.txt line 11: "Johor, Malaysia: June 24, 2025"; line: FD01_092_Biocon2_24062025085406_SEPressrelase-24062025/p002.txt line 27: "The MoU was signed during the National Cancer Congress Malaysia 2025 event, emphasizing a". Value, start: not stated.

DERIVED: FD01_128 parts sum 155.27 + 18 + 52.5 = 225.77 million MYR, consistent with 'over MYR 225 million'. The release does not say they are all the contracts; this is an arithmetic check only.

## L4-48

Step ask (FC-L4-T4-S2): for each deal in five years, target industry, target size against the buyer, funding mix and any later write-down; every new business line marked related or unrelated. Held here: the exchange filings of each acquisition (feed-acquisition) and the matching press releases. Not read here: annual-report notes (no AR quote is used, so none is linked).

- feed-acquisition fetch log: 8 rows = 7 read + 1 HTTP error (the 2025-12-06 board-outcome PDF, 404; the same decision is read through FD01_111 and later filings).

### Viatris biosimilars assets bought by Biocon Biologics (announced 2022-03-02, completed 2022-11-29)

- price as announced. Source: FD09_001_BIOCON_02032022102615_Stock_Exchange_Intimation_Bi/p001.txt line 39: "for up to USD 3.335 billion in Stock and Cash"
- target industry (next line: Pharmaceuticals). Source: FD09_001_BIOCON_02032022102615_Stock_Exchange_Intimation_Bi/p008.txt line 38: "Viatris Inc. is engaged in the business of"
- target revenue estimate (million, next line). Source: FD09_001_BIOCON_02032022102615_Stock_Exchange_Intimation_Bi/p005.txt line 27: "with an estimated revenue of USD 875"
- target EBITDA estimate. Source: FD09_001_BIOCON_02032022102615_Stock_Exchange_Intimation_Bi/p005.txt line 28: "million and EBITDA of USD 200 million for CY 2022 and estimated to exceed USD"
- cash at close. Source: FD09_001_BIOCON_02032022102615_Stock_Exchange_Intimation_Bi/p005.txt line 13: "Viatris will receive cash consideration of USD 2 billion on closing of the transaction and"
- completion: cash paid. Source: FD01_018_BIOCON_29112022183212_PressRelease_29112022/p005.txt line 23: "upfront cash payment of USD 2 billion to Viatris."
- completion: funding, debt part (a Sustainability Linked Loan, next line). Source: FD01_018_BIOCON_29112022183212_PressRelease_29112022/p005.txt line 25: "To fund the upfront payment , Biocon Biologics has secured USD 1.2 billion of"

### Eywa Pharma oral-solid-dose facility, Cranbury NJ (2023-09-01)

- price. Source: FD01_036_BIOCON_02092023145241_SEIntimationPressRelease/p002.txt line 15: "The facility is acquired for a total consideration of US $7.7 million."
- target kind and date (oral solid dosage on the line before). Source: FD01_036_BIOCON_02092023145241_SEIntimationPressRelease/p002.txt line 14: "facility, located in Cranbury, New Jersey, U.S., effective 1st September, 2023."
- capacity potential. Source: FD01_036_BIOCON_02092023145241_SEIntimationPressRelease/p002.txt line 17: "capacity expansion up to 2 billion tablets/capsules per year"

### Pro-zeal Green Power Sixteen, 26% stake, captive solar (2025-08-07)

- stake. Source: FD09_002_Biocon2_07082025205937_SEIntimationAcquisitionFina/p001.txt line 40: "in this connection the Company will be acquiring stake of 26% of paid-up share capital of PGPSPL."
- target size. Source: FD09_002_Biocon2_07082025205937_SEIntimationAcquisitionFina/p002.txt line 27: "The paid-up share capital of PGPSPL is INR 1 Lakh."
- target industry. Source: FD09_002_Biocon2_07082025205937_SEIntimationAcquisitionFina/p003.txt line 31: "PGPSPL is engaged into the business of renewable energy"

### Biocon Biologics minority buyout (board 2025-12-06; closings 2026-01-05, 2026-01-21, 2026-06-29)

- Viatris leg, as announced. Source: FD01_111_BIOCON_06122025101728_Press_Release06122025/p002.txt line 31: "consideration of USD 815 million, of which USD 400 million will be payable in cash and"
- swap price. Source: FD01_111_BIOCON_06122025101728_Press_Release06122025/p002.txt line 28: "at a share price of INR 405.78 per Biocon share"
- 2026-01-05: BBL shares acquired, Biocon shares issued, % of Biocon. Source: FD09_004_BIOCON_05012026220429_SE_disclosure__Biocon_/p002.txt line 19: "TOTAL 26,19,17,480 17,12,79,553 11.36%"
- 2026-01-21: cash leg. Source: FD09_005_BIOCON_21012026195928_SE_Disclosure_-_BBL_share_ac/p001.txt line 35: "way of cash consideration of USD 400 million."
- holding after. Source: FD09_005_BIOCON_21012026195928_SE_Disclosure_-_BBL_share_ac/p001.txt line 41: "Post the aforesaid acquisition, the Company holds ~98% of the paid-up equity share capital of BBL on a fully"
- 2026-06-29: shares issued to 127 holders. Source: FD09_008_BIOCON_29062026225131_SE_Intimation_-_Allotment__P/p001.txt line 43: "issued and allotted 87,86,362 equity shares of the Company of the face"

### AMPIN solar SPV stake (2026-06-10; captive power)

- target industry. Source: FD09_007_BIOCON_10062026194907_Acquisition_AMPIN/p003.txt line 59: "AMPIN is engaged into the business of renewable energy generation."
- amount (Rs 5.4760 crore). Source: FD09_007_BIOCON_10062026194907_Acquisition_AMPIN/p003.txt line 16: "The Company has today invested Rs. 5,47,60,000 (Rupees Five Crores Forty Seven Lakhs"
- stake (percent on the line before). Source: FD09_007_BIOCON_10062026194907_Acquisition_AMPIN/p003.txt line 42: "(on an undiluted basis) as on date"

### Preference shares of two wholly owned subsidiaries (2026-03-03; intra-group, not an outside target)

- target relationship. Source: FD09_006_Bioconlimited_03032026230815_SE_Intimation_-_Acqui/p001.txt line 39: "wholly owned subsidiaries of the Company, respectively."

DERIVED: Eywa USD 7.7 million is a price, not a size ratio; no buyer-size ratio is computed for any deal (the buyer's own figure is not quoted here).

Still not held for L4-48: later write-down of any deal (none searched in held text here); buyer size against target (needs AR figures, not quoted); related or unrelated marks for every new business line since listing; Eywa's funding source; the 2025-12-06 board PDF (404).

## L4-30

Step ask (FC-L4-T2-S6): for each adverse event, the event date, the filing date and the gap between them, plus whether concalls and decks are still published. This file reads only the news-verification letters; it does not cover concall or deck publication.

### Letters read

#### FD08_001 (2022-06)

- exchange query reference and date. Source: FD08_001_BIOCON_22062022104022_BL_Clarification_NSE_Query_J/p001.txt line 25: "Ref: NSE/CM/Surveillance/12022 dated June 21, 2022"
- news item publication date (no clock time printed). Source: FD08_001_BIOCON_22062022104022_BL_Clarification_NSE_Query_J/p001.txt line 28: "which was published by The Hindu on June 21, 2022."
- company statement date. Source: FD08_001_BIOCON_22062022104022_BL_Clarification_NSE_Query_J/p001.txt line 30: "the Company vide its letter dated June 21, 2022 has submitted the Company"
- company's answer on UPSI. Source: FD08_001_BIOCON_22062022104022_BL_Clarification_NSE_Query_J/p001.txt line 36: "We confirm that there is no unpublished price sensitive information available with the Company and there is no"

#### FD08_003 (2026-05)

- exchange query reference and date. Source: FD08_003_BIOCON_06052026213647_Clarification_Letter/p001.txt line 33: "NSE letter reference no. NSE/CM/Surveillance/16970 dated May 06, 2026"
- price movement date (no clock time printed). Source: FD08_003_BIOCON_06052026213647_Clarification_Letter/p001.txt line 41: "of the Company on May 06, 2026."
- company's answer. Source: FD08_003_BIOCON_06052026213647_Clarification_Letter/p001.txt line 43: "continues to serve as the Executive Chairperson of"

#### FD08_002 (2022-11)

- The PDF is image-only (fetch log: extraction pending, OCR not installed): NOT read. Only the exchange feed's own row text is known (below).

### Exchange rows (feed sort_date, to the second)

| news caption (feed text) | rows (time, has file) | DERIVED gap first to last row |
|---|---|---|
| BIOCON : The Exchange has sought clarification from Biocon Limited with respect to recent news item captioned  | 2022-06-21 17:44:32 (query); 2022-06-22 10:40:23 (reply) | 16h 55m 51s |
| BIOCON : The Exchange has sought clarification from Biocon Limited with respect to recent news item captioned  | 2022-11-16 17:53:54 (query); 2022-11-17 18:00:15 (reply) | 1d 0h 6m 21s |
| Biocon Limited has informed the Exchange about Rumour Verification - Regulation 30(11) [separate item 2025-11- | 2025-11-14 08:30:29 (reply) | single row |
| The Exchange has sought clarification from Biocon Limited with respect to recent news item captioned Biocon s  | 2026-05-06 12:53:44 (query); 2026-05-06 21:38:06 (reply) | 8h 44m 22s |
| Biocon Limited has informed the Exchange about Rumour Verification - Regulation 30(11) [separate item 2026-05- | 2026-05-06 21:33:51 (reply) | single row |

Feed text is the exchange's own caption (labelled FEED, not a line of a held PDF).

Event date versus filing date, from these letters: the news item date is printed (2022-06-21, The Hindu; 2026-05-06 price movement) and equals the exchange query date, but no clock time of the article or the price move is printed. So the gap between the news and the exchange query cannot be computed; the only gaps held are query row to reply row (table above).

Still not held: the alleged event's own date (the bribery allegation of 2022; a succession report of 2026 is a report, not an event); article or wire times; the FD08_002 letter text; whether concalls and decks are still published (not read here); the 2025-11-14 and 2026-05-06 rumour-verification PDFs (not in the folder).

## L5-58

Step ask (FC-L5-T4-S4), the part this read answers: whether material news in the last year came first through an exchange filing. One-to-one guidance and dodged questions are not read here.

- Contract press releases: each was filed on the exchange the same day or later than its printed date (days column in the L5-46 table, DERIVED). The press release is the exchange filing itself (the PDF is the filed attachment), so a release that appears elsewhere first cannot be shown or ruled out from held files; no other outlet's time is held.
- News verifications: in each case the exchange raised the query on the news item first (rows above); the company's reply followed. This shows the exchange learned of the item from the press, not that the company filed it first. Whether the company filed anything before the article is not held (no article clock time).

Not closable from held files: the question needs the first public time of each material item, and no press, wire or website time is held.

## Still not held (all rows)

- Share of revenue for any contract (release prints no order value against revenue).
- 2 image-only press PDFs, 1 press 404, 1 acquisition 404, FD08_002 image-only.
- Any later write-down, buyer-size ratio and concall/deck publication status.
