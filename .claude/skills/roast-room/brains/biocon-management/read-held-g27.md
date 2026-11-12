# Read-held g27 (BIOCON): L5-3, L5-57, L5-16

Source folders: /home/user/soic-ladder/docs/idea/case-study/BIOCON/data/feed-fetched/feed-calls and feed-agm. Every quote below was checked in code to sit on the named line. No grading, no row closed here.

## L5-3  Call text for Q1 FY24 and Q2 FY25
Step ask (FINAL-STATUS.csv): 'Call text for Q1 FY24 and Q2 FY25' (feeds FC-L5-T1-S1: the last 3-4 call transcripts, dated).

- **Q1 FY24 (Apr-Jun 2023 results call)**: FULL TRANSCRIPT. 28 page files, 80,335 characters (heuristic: >= 20,000 characters and moderator question lines present; this script's own cut), 13 'next/last question' lines.
  - Subject: FD02_053_BIOCON_21082023134622_EarningsCallTranscript_signe/p001.txt line 33: "Transcript of Earnings Call Q1 FY24"
  - Held: FD02_053_BIOCON_21082023134622_EarningsCallTranscript_signe/p001.txt line 36: "held on August 11 , 202 3,"
- **Q2 FY25 (Jul-Sep 2024 results call)**: FULL TRANSCRIPT. 27 page files, 78,044 characters (heuristic: >= 20,000 characters and moderator question lines present; this script's own cut), 14 'next/last question' lines.
  - Subject: FD02_125_BIOCON_07112024212744_TranscriptEarningsCallQ2FY25/p001.txt line 33: "Transcript of Earnings Call Q2 FY25"
  - Held: FD02_125_BIOCON_07112024212744_TranscriptEarningsCallQ2FY25/p001.txt line 36: "held on October 30, 2024,"

Earlier held (not new): the old data/calls folder has no Q1 FY24 and no Q2 FY25 file (it lists q2fy23, q3fy23, q4fy23, q2fy24, q3fy24, q4fy24, q1fy25, q3fy25).
Match of dates: Q1 FY24 results call held August 11, 2023 (letter dated August 21, 2023); Q2 FY25 call held October 30, 2024 (letter dated November 07, 2024).

Still not held: nothing for these two quarters. The call VIDEO and the presentation shown on the call are not part of this text.
Row status is the grader's call; this note only records what is held.

## L5-57  Call ended early; sceptical against friendly analysts
Step ask (framework.md FC-L5-T4-S4 Check): did management end the call early or avoid questions on a problem? Does it let sceptical analysts ask, or only friendly ones?

Full transcripts held: 14 calls, Q4 FY23 to Q1 FY27 (Q1 FY24 and Q2 FY25 included; Q2 FY24 and Q4 FY24 etc. also present).

- **Transcript of Earnings Call Q4 FY23**, held on May 24, 2023,: 85,749 chars, 11 question-intro lines, 11 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Cyndrella Carvalho, Tushar Manudhane, Prakash Agarwal, Damayanti Kerai, Harith Ahamed, Shyam Srinivasan, Surya Patra, Neha Manpuria, Ishita Jain, Nithya Balasubramanian, Sandeep Joshi
  - first intro: FD02_040_BIOCON_31052023171455_TranscriptEarningsCall_signe/p009.txt line 32: "first question is from Cyndrella Carvalho"
  - last-question line: FD02_040_BIOCON_31052023171455_TranscriptEarningsCall_signe/p030.txt line 4: "This was the last question for today's call"
  - lines with 'no response / not able to hear / time constraint / out of time / unanswered / given the timelines / take them offline': 0 found
- **Transcript of Earnings Call Q1 FY24**, held on August 11 , 202 3,: 80,335 chars, 13 question-intro lines, 13 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Harith Ahamed, Surya Patra, Neha Manpuria, Shyam Srinivasan, Parth Shah, Tarang Agrawal, Yash Tanna, Masira Vasanwala, Cyndrella Carvalho, Vishal Manchanda, Nitin Agarwal, Ishita Jain, Sai Priyanka
  - first intro: FD02_053_BIOCON_21082023134622_EarningsCallTranscript_signe/p010.txt line 27: "next question from Harith Ahamed from Avendus"
  - last-question line: FD02_053_BIOCON_21082023134622_EarningsCallTranscript_signe/p028.txt line 6: "Ladies and gentlemen, that's was the last question for today's call"
  - closing line: FD02_053_BIOCON_21082023134622_EarningsCallTranscript_signe/p028.txt line 8: "With this, we will conclude"
  - lines with 'no response / not able to hear / time constraint / out of time / unanswered / given the timelines / take them offline': 0 found
- **Transcript of Earnings Call Q2 FY24**, held on November 10, 2023,: 71,173 chars, 6 question-intro lines, 6 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Yash Tanna, Surya Patra, Jainil Shah, Nithya Balasubramanian, Shyam Srinivasan, Rumel Dahiya
  - first intro: FD02_071_BIOCON_20112023214334_TranscriptEarningCall_101120/p011.txt line 7: "next question is from Yash Tanna."
  - last-question line: FD02_071_BIOCON_20112023214334_TranscriptEarningCall_101120/p024.txt line 10: "Ladies and gentlemen, this was the last question"
  - lines with 'no response / not able to hear / time constraint / out of time / unanswered / given the timelines / take them offline': 0 found
- **Transcript of Earnings Call Q3 FY24**, held on February 9 , 202 4,: 60,351 chars, 6 question-intro lines, 6 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Damayanti Kerai, Shyam Srinivasan, Vipul Kumar, Tushar Manudhane, Pranav, Harith Ah
  - first intro: FD02_084_BIOCON_16022024221949_Transcript_160224_signed/p009.txt line 24: "next question from Damayanti Kerai from HSBC."
  - last-question line: FD02_084_BIOCON_16022024221949_Transcript_160224_signed/p020.txt line 23: "That was the last question of the day"
  - lines with 'no response / not able to hear / time constraint / out of time / unanswered / given the timelines / take them offline': 0 found
- **Transcript of Earnings Call Q4 FY24**, held on May 16, 2024,: 60,630 chars, 5 question-intro lines, 5 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Jainil Shah, Surya Patra, Neha Manpuria, Ankush Mahajan, Nitin Agarwal
  - first intro: FD02_097_BIOCON_23052024151509_CoverLetter_TranscriptEarnin/p013.txt line 27: "next question from Jainil Shah from JM Financial."
  - last-question line: FD02_097_BIOCON_23052024151509_CoverLetter_TranscriptEarnin/p020.txt line 11: "That was the last question of the day given the"
  - no-response/time/unanswered phrase: FD02_097_BIOCON_23052024151509_CoverLetter_TranscriptEarnin/p020.txt line 12: "timelines we are at. For the question that will remain unanswered, I request the"
  - no-response/time/unanswered phrase: FD02_097_BIOCON_23052024151509_CoverLetter_TranscriptEarnin/p020.txt line 13: "to please send us an e-mail, and we will be happy to take them offline."
- **Transcript of Earnings Call Q1 FY25**, held on August 09, 2024 ,: 53,268 chars, 10 question-intro lines, 10 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Amey Chalke, Tushar Manudhane, Neha Manpuria, Surya Patra, Manoj Bahety, Kunal Randeria, Ashish Thavkar, Jamsheed, Rahul Jeewani, Dhaval Bhalodia
  - first intro: FD02_111_BIOCON_19082024172815_CoverLetter_TranscriptEarnin/p008.txt line 23: "first question from Amey Chalke. Please go ahead."
  - last-question line: FD02_111_BIOCON_19082024172815_CoverLetter_TranscriptEarnin/p019.txt line 13: "Saurabh Paliwal: Ladies and gentlemen, that was the last question for the day"
  - lines with 'no response / not able to hear / time constraint / out of time / unanswered / given the timelines / take them offline': 0 found
- **Transcript of Earnings Call Q2 FY25**, held on October 30, 2024,: 78,044 chars, 14 question-intro lines, 14 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Harith Ahamed, Surya Patra, Neha Manpuria, Damayanti Kerai, Palak Shah, Amey Chalke, Jamsheed, Niraj Jain, Naman Bagrecha, Tushar Manudhane, Yash Darak, Kapil Agarwal, Rumel Dahiya, Harshit Dhoot
  - first intro: FD02_125_BIOCON_07112024212744_TranscriptEarningsCallQ2FY25/p009.txt line 6: "first question from Harith Ahamed from Spark Capital. Please go"
  - last-question line: FD02_125_BIOCON_07112024212744_TranscriptEarningsCallQ2FY25/p027.txt line 2: "That was the last question for this call"
  - lines with 'no response / not able to hear / time constraint / out of time / unanswered / given the timelines / take them offline': 0 found
- **Transcript of Earnings Call Q3 FY25**, held on January 31, 2025,: 75,452 chars, 8 question-intro lines, 8 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Damayanti Kerai, Neha Manpuria, Shyam Srinivasan, Amey Chalke, Love Sharma, Surya Patra, Vivek Agrawal, Bharat Sheth
  - first intro: FD02_141_BioconLtd_07022025154443_SIGNEDSELetterTranscript./p009.txt line 9: "first question from Damayanti Kerai from HSBC. Please go ahead."
  - last-question line: FD02_141_BioconLtd_07022025154443_SIGNEDSELetterTranscript./p025.txt line 17: "Saurabh Paliwal: Ladies and gentlemen, that is the last question for the day"
  - lines with 'no response / not able to hear / time constraint / out of time / unanswered / given the timelines / take them offline': 0 found
- **Transcript of Earnings Call Q4 FY25**, held on May 09, 2025,: 50,787 chars, 8 question-intro lines, 8 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Neha Manpuria, Harith Ahamed, Surya Patra, Prapti Gupta, Amey Chalke, Tushar Manudhane, Nitin Agarwal, Love Sharma
  - first intro: FD02_146_Biocon2_15052025223549_SETranscriptEarningsCall.pd/p009.txt line 19: "next question from Neha Manpuria from Bank of America Securities."
  - last-question line: FD02_146_Biocon2_15052025223549_SETranscriptEarningsCall.pd/p018.txt line 34: "Saurabh Paliwal: That was the last question for the day"
  - closing line: FD02_146_Biocon2_15052025223549_SETranscriptEarningsCall.pd/p019.txt line 3: "This concludes the call"
  - lines with 'no response / not able to hear / time constraint / out of time / unanswered / given the timelines / take them offline': 0 found
- **Transcript of Earnings Call Q1 FY26**, held on August 08, 2025,: 65,769 chars, 8 question-intro lines, 8 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Surya Patra, Neha Manpuria, Harith Ahamed, Shyam Srinivasan, Tushar Manudhane, Neha Kharodia, Vipulkumar Shah, Nitin Agarwal
  - first intro: FD02_150_Biocon2_14082025194801_Cover_Letter_Transcript_Ear/p010.txt line 26: "next question from Surya Patra from Philip Capital."
  - last-question line: FD02_150_Biocon2_14082025194801_Cover_Letter_Transcript_Ear/p024.txt line 22: "Saurabh Paliwal: That was our last question, ladies and gentlemen, for this call"
  - lines with 'no response / not able to hear / time constraint / out of time / unanswered / given the timelines / take them offline': 0 found
- **Transcript of Earnings Call Q2 FY26**, held on November 12, 2025,: 48,559 chars, 8 question-intro lines, 8 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Tushar Manudhane, Harith Ahamed, Sidharth Negandhi, Love Sharma, Surya Patra, Abdulkader Puranwala, Imtiaz Shefuddin, Nitin Agarwal
  - first intro: FD02_158_Biocon2_18112025165746_Cover_Letter_Transcript_Ear/p009.txt line 11: "first question is from Tushar Manudhane."
  - closing line: FD02_158_Biocon2_18112025165746_Cover_Letter_Transcript_Ear/p020.txt line 27: "concludes this conference"
  - lines with 'no response / not able to hear / time constraint / out of time / unanswered / given the timelines / take them offline': 0 found
- **Transcript of Earnings Call Q3 FY26**, held on February 13, 2026,: 57,824 chars, 9 question-intro lines, 8 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Neha Manpuria, Damayanti Kerai, Surya Patra, Tushar Manudhane, Harshit Dhoot, Sachin Jain, Siddharth Negandhi, Vishal Manchanda
  - first intro: FD02_165_BIOCON_17022026171942_Cover_Letter_Transcript_Earn/p010.txt line 7: "first question is from Neha Manpuria. Please introduce yourself and proceed with your"
  - last-question line: FD02_165_BIOCON_17022026171942_Cover_Letter_Transcript_Earn/p023.txt line 8: "Moderator: As that was the last question for today, I would now like to hand the conference over to"
  - closing line: FD02_165_BIOCON_17022026171942_Cover_Letter_Transcript_Earn/p023.txt line 13: "Limited, that concludes this conference"
  - no-response/time/unanswered phrase: FD02_165_BIOCON_17022026171942_Cover_Letter_Transcript_Earn/p023.txt line 11: "questions unanswered, please get in touch with the IR team. Thank you."
- **Transcript of Earnings Call Q4 FY26**, held on May 08, 2026,: 54,123 chars, 10 question-intro lines, 9 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Neha Manpuria, Surya Patra, Sanjay Kohli, Avnish Burman, Sidharth Negandhi, Tushar Manudhane, Imtiaaz Shefuddin, Vishal Manchanda, Nitin Agarwal
  - first intro: FD02_171_BIOCON_14052026162935_Cover_Letter_Transcript_Earn/p008.txt line 20: "first question is from Neha Manpuria. Please introduce"
  - last-question line: FD02_171_BIOCON_14052026162935_Cover_Letter_Transcript_Earn/p022.txt line 2: "Moderator: Ladies and gentlemen, that was the last question for today"
  - no-response/time/unanswered phrase: FD02_171_BIOCON_14052026162935_Cover_Letter_Transcript_Earn/p010.txt line 18: "The next question is from Surya Patra. As there is no response, we will move on to the"
- **Transcript of Earnings Call Q1 FY27**, held on August 06, 2026,: 50,889 chars, 8 question-intro lines, 8 distinct names named by the moderator/IR host.
  - names (as captured by regex, check against lines): Neha Manpuria, Surya Patra, Shyam Srinivasan, Damayanti Kerai, Sidharth Negandhi, Ankit Shah, Chin, Vipul Shah
  - first intro: FD02_179_BIOCON_11082026200302_Cover_Letter_Transcript_Earn/p010.txt line 14: "Next question is from line of Neha Manpuria. Kindly announce"
  - closing line: FD02_179_BIOCON_11082026200302_Cover_Letter_Transcript_Earn/p021.txt line 12: "On behalf of Biocon Limited, that concludes this conference"
  - no-response/time/unanswered phrase: FD02_179_BIOCON_11082026200302_Cover_Letter_Transcript_Earn/p021.txt line 8: "questions that are unanswered or any other questions, please reach out to the IR team,"

What the text does and does not show:
- Calls whose text carries a no-response, 'unanswered' or timelines phrase (quoted above, read the line): 4 of 14 (Q4 FY24, Q3 FY26, Q4 FY26, Q1 FY27). The Q4 FY24 host says the last question was taken 'given the timelines' and that unanswered questions go by e-mail; that is the one place the text itself ties the close to time. The others are a standing invitation to e-mail the IR team or one analyst who did not respond; none says management cut the call.
- The planned length of each call is not stated in the held text, so 'ended early' against a schedule is not measurable here.
- 'Sceptical' versus 'friendly' is NOT classified: it needs each question's wording read and judged, and no tone is inferred without a quoted question. The counts above give who asked and how many, not how hard. Names are as a regex captured them from the host's line; a name split by a PDF space or line wrap (for example 'Harith Ah amed') is cut short.

Not closable because: 'ended early' needs the scheduled length (not held) and 'sceptical against friendly' needs a per-question judgement that this note does not make.
Still not held: the scheduled call length, the audio, and any analyst whose line the transcript editor dropped (each transcript prints 'edited to improve accuracy and readability').

## L5-16  AGM proceedings, Q&A or webcast
Step ask (framework.md FC-L5-T1-S5 Open): 'AGM (annual general meeting) records' to judge how often the company speaks and through which channel.

- **46th AGM, 9 Aug 2024** (proceedings summary, 6 page files, 13,192 chars)
  - FD03_013_BIOCON_09082024183732_AGMProceedingssigned/p001.txt line 30: "Proceedings of the 46th Annual General Meeting (‘AGM’) of t"
  - FD03_013_BIOCON_09082024183732_AGMProceedingssigned/p004.txt line 31: "the floor was made open for those Members to ask questions or express their"
  - FD03_013_BIOCON_09082024183732_AGMProceedingssigned/p004.txt line 34: "clarified all the members’ queries."
- **47th AGM, 8 Aug 2025** (proceedings summary, 6 page files, 12,931 chars)
  - FD03_022_Biocon2_08082025184012_SEAGMProceedings/p001.txt line 30: "Proceedings of the 47th Annual General Meeting (‘AGM’) of t"
  - FD03_022_Biocon2_08082025184012_SEAGMProceedings/p004.txt line 42: "the floor was made open for those Members to ask questions or express their"
  - FD03_022_Biocon2_08082025184012_SEAGMProceedings/p004.txt line 45: "clarified all the Members’ queries."
- **48th AGM, 6 Aug 2026** (proceedings summary, 10 page files, 20,773 chars)
  - FD03_031_BIOCON_06082026204223_Biocon_AGM_Proceedings_and_C/p001.txt line 16: "Proceedings of the 48th Annual General Meeting of the Compa"
  - FD03_031_BIOCON_06082026204223_Biocon_AGM_Proceedings_and_C/p004.txt line 46: "the floor was made open for those Members to ask questions or express their"
  - FD03_031_BIOCON_06082026204223_Biocon_AGM_Proceedings_and_C/p005.txt line 4: "clarified all the Members’ queries."
- 48th AGM file also encloses the Chairperson's speech: FD03_031_BIOCON_06082026204223_Biocon_AGM_Proceedings_and_C/p001.txt line 25: "Speech delivered at the 48th AGM of the Company.". Its pages p007-p010 extracted as scrambled characters (font map), so the speech text is NOT read.
- 48th AGM voting results (held, readable, 32,250 chars): FD03_032_BIOCON_08082026215336_Voting_Results_and_Scrutiniz/p001.txt line 24: "Voting results and Scrutinizer’s report of the 48th Annual General Meeting (‘A"
- 46th AGM voting results letter (held): FD03_014_BIOCON_13082024192705_SEIntimation_signed/p001.txt line 30: "Voting results and scrutinizers’ report of the 46th Annual General Meeting (‘A"

What the held extracts are: a regulator-filed SUMMARY of proceedings (a paragraph saying the floor was opened and queries clarified), plus voting results. They contain NO question text, no speaker names and no answers.

Still not held: Q&A text or webcast for any AGM; the 45th AGM (2023) and earlier proceedings (FD03_007 is a voting-results file, image-only, extraction pending in fetch-log.json); the 2026 AGM notice file FD03_030 (image-only, pending).
Not closable from held files on the 'Q&A or webcast' part: the held AGM documents summarise the Q&A in one sentence and the webcast is not a held file.
