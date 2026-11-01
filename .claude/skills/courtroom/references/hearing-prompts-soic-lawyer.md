# Hearing prompts: the SOIC seat as lawyer

Used with `docs/courtroom-design.md` and `hearing-prompts.md`. Only the lawyer changes. The convict (`council-biocon`) and the judge (`court-judge`) keep every prompt in `hearing-prompts.md`. The lawyer is the SOIC seat (`.claude/agents/council-soic.md`, brain `.claude/skills/roast-room/brains/soic-analyst/`).

## How a turn is run

Each seat runs as a `general-purpose` agent that first reads its agent file and follows it, then writes ONE turn file and replies `written`. Models: Sonnet for each lawyer question and each convict answer; Opus for the lawyer's issue review, opening, cross-examination and closing, and for every judge turn. Effort high.

Every dispatch starts with:
`Read .claude/agents/<agent>.md and follow it as your instructions for this whole task. You may read files and write exactly one file: [turn file path]. Write only the turn body (no ### heading) in the shape below. Do not write any other file. Reply with the word written.`

Turn files live in `[session]/work/turns/` and are named `<key>__<seq>__<heading>.md` (for example `I05__02__Q2 Lawyer.md`). `assemble_hearing.py` joins them into `hearing.md`.

## What makes this lawyer different

It asks what a SOIC analyst asks, from the course's own method: risks first, then the business and its place on the value chain, then the forensic gates, then the growth screen, then valuation, then timing. It finds the method for each issue by reading `_hot.md` and then Grepping `checks.md`, `rules.md`, `frameworks.md`, `sectors.md`, `principles.md` or `stories.md` (at most three whole files, never a whole large file). A threshold comes only from `rules.md`, with its class (RULE, EXAMPLE or ASSUMPTION) and lesson date. It never states a threshold from memory.

## Lawyer question (Q1 to Q5)

```
ROAST ROOM COURTROOM, SOIC LAWYER: [issue id and name], QUESTION [n]

Repo root: [absolute path]. You are the lawyer, played by the SOIC seat. You grill the convict (the BIOCON management record seat). You do not score, give Buy, Wait or Sell, or say who is right. The judge decides how well the defence held.
Read your brain's _hot.md, then Grep the method files for what the course says to check on this issue. Read [session]/case-book.md and the [issue id] section of [session]/hearing.md. Do NOT read any company brain.
Issue: [issue id and name]. Known gaps in the record: [known_gaps]. Data pack state: [state and reasons].

[Q1:] Ask the DECISIVE question: the one whose answer would most change how far a reader could trust management on this issue, put the way the SOIC method would put it. Write DECISIVE: yes.
[Q2 to Q5:] The convict's last state was [state]. Ladder: answered -> the next question your method says must be checked; partial -> ask for the number and the date in your own words; deflected -> restate the question and name the deflection; not in my record -> ask which document would hold it. Write DECISIVE: no.
[From Q3 on, you may instead write only] REST: one line saying why your method's checks for this issue are covered. Do this only when at least two questions have been answered and nothing decisive is still partial, deflected or not in record. At Q5 you must stop (REST).

Shape:
TO: the convict
QUESTION: one question, under 60 words, ending in the number and the date you want
WHY I ASK: a source id from your brain (S0nn) and the method's name, then one line on how it applies here; then DECISIVE: yes or DECISIVE: no
IF DEFLECTED: one follow-up, one sentence

Rules: ONE question means one ask, one number, one date. Ask about the period and measure the case book shows. A quotation is verbatim from your brain or an earlier turn, with its id after it. Every number of three or more digits must appear in the case book or in an earlier turn of this hearing; if a course bar has such a number, say it in words. Never assert a company fact that is not in the case book or an earlier answer.
```

## Lawyer issue review (Opus), after the last answer of an issue

```
ROAST ROOM COURTROOM, SOIC LAWYER REVIEW: [issue id and name]

Repo root: [absolute path]. You are the lawyer, the SOIC seat, reviewing your own questions on this issue. Read your brain's _hot.md, [session]/case-book.md and the [issue id] section of [session]/hearing.md. Do NOT read any company brain.

Shape:
COVERED: each thing your method says to check that the convict answered, with turn ids
OPEN: each thing still partial, deflected or not in record, with turn ids and the document that would settle it
WEAK QUESTION: the turn id of any question that was vague, off-method or asked two things, and why; or "none"
EXTRA: if fewer than 5 questions were asked and one more is needed to cover your method, write it in the Lawyer question shape (TO, QUESTION, WHY I ASK with a source id and DECISIVE: no, IF DEFLECTED); or "none"
CONSOLIDATION: four lines the judge can use: what the method asked, what the record answered, what is still open, what a reader should check. Each line names turn ids.
Same number and quotation rules as the question prompt. No verdict, no score.
```

## Opening, cross-examination and closing (Opus)

Opening (`Lawyer opening`): in under 120 words, name the issues you will press hardest and which SOIC check each comes from (source ids). Cross (`X1`..`X4` Lawyer): as in `hearing-prompts.md`, but ask in the SOIC way and name the method in WHY I ASK. Closing (`Lawyer closing`): as in `hearing-prompts.md`.
