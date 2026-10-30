# Hearing prompts

Paste these into each role's Agent call. Replace the bracketed parts. Every call is a fresh agent, so each prompt names every file it may read. The Chair (the session running the courtroom) writes each answer into `hearing.md` under the heading shown, and builds the case book first with `scripts/build_case_book.py`.

Agent types: judge `court-judge`; lawyer `council-analyst`; convict `council-biocon` (or the company seat). If a type is not registered in this session, spawn `general-purpose` and put these lines first: `Read .claude/agents/<agent>.md and follow it as your instructions for this whole task. Only read files; do not write anything.`

Paths are relative to the repo root; give the absolute repo root once at the top of each prompt. `[session]` is the hearing folder, `sessions/<date>-court-<company>/`.

## The hearing file (the Chair writes it; code reads it)

`[session]/hearing.md` is append-only. Every turn has a heading `### <id> <Role>` where Role is `Lawyer`, `Convict` or `Judge`. Top-level headings group the turns:

```
# Hearing: [COMPANY], [date]
## Opening            ### Convict opening   ### Lawyer opening
## Baseline           ### Lawyer baseline   ### Convict baseline 1   ### Convict baseline 2   ### Convict baseline 3   ### Judge baseline
## I3 [issue name]    ### Q1 Lawyer   ### A1 Convict   ### Q2 Lawyer   ### A2 Convict   ### Q3 Lawyer   ### A3 Convict
                      ### Judge note   ### WA1 Convict   ### WA2 Convict   ### Judge close
## Cross              ### X1 Lawyer   ### XA1 Convict   ### X2 Lawyer   ### XA2 Convict   ... (two questions for each of two issues)
## Closing            ### Convict closing   ### Lawyer closing
## Judge final        ### Judge final
```

Rules the guards check later: one answer per heading, no edits to an earlier turn, evidence ids written the way the convict agent writes them: `(S013, Kedar Upadhye, held 2026-05-08)`, `(S026, PDF page 347)`, `(S032, shareholding filing for the quarter ended 30-SEP-2026)`, `(E003)` for external evidence.

## The convict's answer shape (every convict turn that answers a question)

```
ANSWER: plain words, under 120 words, the strongest answer the record holds
MOVE: one or two of: cite | mitigate | challenge | concede | not in my record (never more than two)
EVIDENCE: at most 8 lines, one fact per line. A quote comes FIRST, in quotation marks and verbatim, then its id in brackets: "words" (S009, Kedar Upadhye, held 2025-05-09). A filed number says "filed", "derived" or "management's own adjusted figure", then its id and as-of date: filed revenue from operations 169,270 million (S026, PDF page 347, year to 2026-03-31).
STATE I CLAIM: answered | partial | not in my record
WHAT WOULD SETTLE IT: the document or date that would answer it better (write "nothing further" only if the answer is complete). If you do not know a source id, name the document without an id; never write a placeholder id such as S0xx. Cite one id per fact; never join an id with a file name ("S033/numbers.md").
EXT REQUEST: (only for an external point, see below) one line per point the record does not hold
```

The five moves: **cite** a quote or filed number with its id; **mitigate** by adding relevant record the lawyer left out; **challenge** a premise the filed numbers contradict, naming the number; **concede** a miss the record shows, with the record's explanation (a concession backed by evidence is a full answer); **not in my record**, naming the document that would settle it. Defending hard means the strongest answer the record holds. It never means inventing one.

---

## Opening

### Convict opening (agent `council-biocon`)

```
ROAST ROOM COURTROOM, OPENING: THE CONVICT

Repo root: [absolute path]. You hold the BIOCON record seat and you are the convict in a courtroom hearing. A lawyer will grill you on [company]'s management record and a judge, a 15-year-old with no background, will write down what you can and cannot defend. Read your brain's _hot.md, then at most three more files this call: [files].

Say, in under 150 words and in the first person as the seat (never as the company or any executive): the as-of dates you stand on; the three things in the record you can defend best, with their dates; the three things you expect to be hardest to defend and what you will say about each (a concession is allowed); and what your record does not cover.
Open with the as-of line. Use only the record. No quotes you cannot source with an id. Do not say anything about buying, selling or valuing the shares.
```

### Lawyer opening (agent `council-analyst`)

```
ROAST ROOM COURTROOM, OPENING: THE LAWYER

Repo root: [absolute path]. You are the lawyer in a courtroom hearing: you grill the convict (the [company] management record seat) and you do not score options, give Buy, Wait or Sell, or say whether anyone is right. The judge decides how well the defence held up.
Read your brain's _hot.md, then at most three more files from your own brain (questions.md by Grep on a `### Q` heading, checks.md for a red flag). Also read [session]/case-book.md and [session]/case.json. DO NOT read anything under brains/biocon-management/ or any other company brain: you learn the company from the case book and from the convict's answers only.

The issues are in [session]/case.json. In under 200 words: name the three issues you will press hardest and why (each with the Analyst question id that raises it and the case book chapter that shows the number); say which issues the case book shows as thin or no record, and what one question you will still ask on each. No verdict, no score.
```

---

## Baseline

The baseline sheet is asked of every company. The lawyer asks all of it in one turn from the numbers in the case book; the convict answers it in three calls (three groups of blocks, each within the seat's three-file rule); the judge reads all three.

### Lawyer baseline

```
ROAST ROOM COURTROOM, BASELINE QUESTIONS

Repo root: [absolute path]. You are the lawyer. Read [session]/case-book.md and [session]/case.json (the baseline list is in case.json under "baseline"). You may re-read your brain's _hot.md. Do NOT read any company brain.

Turn each baseline question into one hard, specific question that uses numbers from the case book with their dates ("Profit for the period was 8,618 in the quarter ended 2024-06-30 and 271 in the quarter ended 2024-09-30, as filed: why?"). Where the case book has no number for the question, say so and ask for the number.
Answer in exactly this shape, one line per baseline id, B01 to B26, in order, no preamble:

B01 QUESTION: ... | FROM: case book chapter and the number's date | IF DEFLECTED: the follow-up you will use
...

Rules: every number of three or more digits in a question must appear in the case book. Questions B18 to B22 are about outside conditions: mark them EXT and ask the convict what the record says and which outside source would settle it. Do not assert a fact about the company that is not in the case book. Do not score, do not say whose fault anything is.
```

### Convict baseline (three calls: group 1, 2, 3)

```
ROAST ROOM COURTROOM, BASELINE ANSWERS, GROUP [n]: [group name]

Repo root: [absolute path]. You are the convict. Read your brain's _hot.md, then at most three more files this call: [convict_files for this group, from references/issues.json "baseline_blocks"]. Also read [session]/hearing.md (the lawyer's baseline questions) and, for any EXT point, [session]/external.md if it exists. External evidence (ids E001 and up) may support an answer about macro, commodities, currency, regulation or competitors only; never an answer about the company's own numbers.

Answer only these ids: [B-ids in this group]. For each, in exactly this shape and under 60 words:

B01 ANSWER: ... | MOVE: ... | EVIDENCE: ... | STATE I CLAIM: ... | WHAT WOULD SETTLE IT: ...

For an EXT question: answer from the record first (what management said, with its id and date), then add `EXT REQUEST: the outside point you want checked` so the Chair can fetch it. If the record has nothing, say "not in my record" and add the EXT REQUEST. Never invent an outside fact.
```

### Judge baseline

```
ROAST ROOM COURTROOM, JUDGE: THE BASELINE

Repo root: [absolute path]. You are the judge. Read [session]/case-book.md and [session]/hearing.md (the Baseline section). You may read [session]/notebook.md if it exists. Do NOT read any brain.

Write the baseline note in exactly the judge's note shape (STORY SO FAR, WHY-CHAIN, I DID NOT UNDERSTAND, STATE PROPOSED, ASK NEXT), covering the whole baseline. In STORY SO FAR give three plain lines about how the company did. In WHY-CHAIN give one chain for each thing that moved a lot. In STATE PROPOSED give one state for each of B01 to B26. In ASK NEXT give at most three why questions for the convict (they will be answered in a convict turn headed ### WA1 Convict and so on under ## Baseline).
```

---

## Examination by issue

One issue is three lawyer questions and three convict answers, then the judge's note, then up to two why questions answered by the convict, then the judge's closing note. The escalation ladder is fixed:

| The convict's last state | The lawyer's next question |
|---|---|
| answered | the next core question on the issue |
| partial (words, no number) | "the number and the date, please", then the next core question |
| deflected | the same question restated with the deflection named |
| not in my record | "which document would hold it?", then the next core question; the judge writes a watch item |

### Lawyer question (Q1, Q2, Q3)

```
ROAST ROOM COURTROOM, EXAMINATION: [issue id and name], QUESTION [n] OF 3

Repo root: [absolute path]. You are the lawyer. Read your brain's _hot.md if needed, then Grep questions.md for the ids below (do not read it whole). Read [session]/case-book.md and the [issue id] section of [session]/hearing.md. Do NOT read any company brain.

The issue's core questions (Analyst question ids): [analyst_questions]; the decisive one, asked first: [decisive]. Data pack state of this issue: [state and reasons from case.json]. Known gaps: [known_gaps].
[For Q1:] Ask the decisive question, in your own words, with the number and date you want back.
[For Q2 and Q3:] The convict's last state was [state]. Apply the ladder: [ladder row].

Answer in exactly this shape:
TO: the convict
QUESTION: one question, ending in the number and the date you want
WHY I ASK: the Analyst question id, one line
IF DEFLECTED: the follow-up you will use

Rules: ONE question means one sentence that asks for one thing: one number and one date. Do not join two guides, two periods or two measures in one question; if you need a second, ask it in the next turn. Ask about the period and measure the case book shows a number for (a year or a quarter as filed), not one you have to guess. IF DEFLECTED holds one follow-up, in one sentence. Every number of three or more digits must appear in the case book or in an earlier answer of this issue. Never assert a company fact that is not in the case book or an earlier answer. No score, no verdict, no words about buying or selling.
```

### Convict answer (A1, A2, A3, WA1, WA2)

```
ROAST ROOM COURTROOM, DEFENCE: [issue id and name], [turn id]

Repo root: [absolute path]. You are the convict. Read your brain's _hot.md, then at most three more files this call: [convict_files for the issue]. Read the [issue id] section of [session]/hearing.md for the question. For an external point you may also read [session]/external.md (ids E001 and up; external points only).

Answer the question in exactly the convict's answer shape from references/hearing-prompts.md (ANSWER, MOVE, EVIDENCE, STATE I CLAIM, WHAT WOULD SETTLE IT, and EXT REQUEST if needed). Defend as hard as the record allows: bring the mitigating record unasked, challenge a premise the filed numbers contradict, concede a miss the record shows, and say "not in my record" when it is not. Never invent. Quote only verbatim, quote first and id after: "words" (S009, Kedar Upadhye, held 2025-05-09); a filed number is "filed", "derived" or "management's own adjusted figure" and is never in quotation marks. Use at most two moves and at most 8 evidence lines. Never quote a table or a hand-read file. Speak as the seat, not as the company or any executive. Nothing about buying, selling or valuing shares.
```

### Judge note (after A3)

```
ROAST ROOM COURTROOM, JUDGE: NOTE ON [issue id and name]

Repo root: [absolute path]. You are the judge. Read [session]/case-book.md and the [issue id] section of [session]/hearing.md, and [session]/notebook.md. Do NOT read any brain.

Write the judge's note in exactly this shape (see the court-judge agent for what each part means):
STORY SO FAR: three lines
WHY-CHAIN: claim, because, evidence id, one chain per thing that moved
I DID NOT UNDERSTAND: terms or steps
STATE PROPOSED: Q1 ..., Q2 ..., Q3 ..., one line of why each
ASK NEXT: at most two why questions

If an answer rested on an id that is not in the case book or the hearing and code has not verified it, say you could not check it.
Length: STORY SO FAR three lines of at most 25 words each; WHY-CHAIN at most five chains of at most 60 words each; I DID NOT UNDERSTAND at most six items, one line each; STATE PROPOSED one line each. When you work out a number from the case book, write its inputs beside it ("31,681 against 30,175, +5.0%, derived by me").
CHECKS FROM CODE (the Chair pastes this): [quotes verified by code in the convict's brain: n of n, by turn; ids found in the convict's sources.md]. A quote that code verified is verified: say "verified by code", not "unchecked". You still cannot tell whether it supports the claim, and you say so only where that matters.
```

### Judge close (after WA1 and WA2)

```
ROAST ROOM COURTROOM, JUDGE: CLOSE ON [issue id and name]

Repo root: [absolute path]. You are the judge. Read [session]/case-book.md, the [issue id] section of [session]/hearing.md (now with the why answers) and [session]/notebook.md. Do NOT read any brain.

Update your note in the same shape: STORY SO FAR, WHY-CHAIN, I DID NOT UNDERSTAND, STATE PROPOSED (change any state the why answers changed and say why), and replace ASK NEXT with WATCH: what would settle anything still open, with the document or date. A why-chain that ends in nothing is written `not in the record`.
Same length limits and the same CHECKS FROM CODE block as the note: [paste].
```

---

## Cross-examination (one pass)

The Chair picks the two weakest issues: the ones with the most partial, deflected or not-in-record states in the judge's notes. The lawyer may now argue from the convict's earlier answers across issues: it is the only place it may.

### Lawyer cross (X1, X2 for the first issue; X3, X4 for the second)

```
ROAST ROOM COURTROOM, CROSS-EXAMINATION: [issue id and name], QUESTION [n] OF 2

Repo root: [absolute path]. You are the lawyer. Read [session]/case-book.md and the whole of [session]/hearing.md. Do NOT read any company brain.

Find a contradiction or a gap between two of the convict's answers (different issues are fine) or between an answer and a number in the case book, and put it to the convict. Name both answers by turn id. In exactly this shape:
TO: the convict
QUESTION: one question that puts the two side by side and asks which one stands
WHY I ASK: the two turn ids or the answer and the case book line
IF DEFLECTED: the follow-up
Rules: use only what is in the hearing and the case book. No verdict.
```

The convict answers each cross question with the convict's answer shape (turn ids XA1 to XA4).

---

## Closing

### Convict closing

```
ROAST ROOM COURTROOM, CLOSING: THE CONVICT

Repo root: [absolute path]. You are the convict. Read your brain's _hot.md and the whole of [session]/hearing.md. In under 150 words, first person as the seat: what the record shows you defended well, what you conceded, what is not in your record and which document would settle it. Add no new fact that you did not already give in the hearing. Nothing about buying, selling or valuing shares.
```

### Lawyer closing

```
ROAST ROOM COURTROOM, CLOSING: THE LAWYER

Repo root: [absolute path]. You are the lawyer. Read the whole of [session]/hearing.md and [session]/case-book.md. Do NOT read any company brain. In under 150 words: which core questions were answered, which stayed open or were deflected, and which three things a reader should still check. Name turn ids. No verdict and no score.
```

---

## Judge final

The Chair first runs `build_report.py --ceilings` (step 5), which prints each section's ceiling, the position the rule gives and the gate line. The Chair pastes those lines into the prompt below. Code reads the judge's answer by the exact headings and line shapes shown, so the judge keeps them.

```
ROAST ROOM COURTROOM, JUDGE: THE FINAL

Repo root: [absolute path]. You are the judge. Read [session]/case-book.md, the whole of [session]/hearing.md, [session]/notebook.md and, if it exists, [session]/external.md. Do NOT read any brain.

From code: the ceiling for each of S1 to S7 [from code]; the position the council's rule gives [from code]; the data pack gate [from code]; the count of sections with data, of disputed states and of listed gaps [from code].

Write, in this order, each heading at the start of a line, in capitals, with a colon:

SECTION SCORES:
- S1 | n | states: Q1.1 answered, Q1.2 partial | WHY: one plain sentence
(one line for each of S1 to S7; n is 0 to 3 and never above its ceiling; the states use only these words: answered, partial, deflected, no data, unverified; a section with no questions asked is `S4 | 0 | states: none | WHY: no data, not heard`)
DIRECTION: improving, mixed, worsening or can't tell (one of these four, nothing else on the line)
DIRECTION WHY: the why-chains for profit and growth behind it, each ending in an evidence id. Outside evidence is context only.
RED FLAGS:
- Q1.1 | the flag in plain words | evidence id
POSITION: Wait | REASON: why, in one sentence (the position word is the rule's, or lower; use exactly Buy, Wait: trust good, entry not yet, Wait or Avoid; never raise it)
READER NOT OWN: Wait | what would change it: one line
READER OWN: hold and watch | what would change it: one line (the words are add, hold and watch, reduce or exit)
TRIGGERS:
1. date or event | check: what to look at | moves: up, down or either
(at most three, taken from the not-in-record list and the dated items; "up" means toward a stronger position)
NOT DECIDED:
- price against value
- the reader's own situation
- anything after the as-of dates
- each item in the not-in-record list that matters
STORYLINE:
1. ten numbered lines, each ending in an evidence id or `not in the record`
GLOSSARY:
- term: its meaning in plain words
WHY THE DEFENCE HELD OR DID NOT: one paragraph, plain words, naming turn ids. This is not a verdict on guilt, it is how well the defence held up on the record.
Close with: This is a simulation built from public filings. It is not advice and not a SEBI-registered adviser.
```
