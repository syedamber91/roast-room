# Stock rating mode (council-owned trust table)

Used only when the decision is a rating call on one listed Indian stock: the options are A Buy (or add), B Wait, C Sell (or do not buy), and the India Market Analyst seat is at the table. The Chair turns it on in Step 2 and says so in `brief.md`. Any other decision runs the normal flow and ignores this file.

**The rule that matters:** the section numbers belong to the whole council, not to the Analyst. The Analyst proposes the first numbers and carries the questions. Every seat can agree, dispute or move a number, and the Chair publishes the council's final numbers. No seat's number is final by itself.

## What is rated: trust in management's word

The table rates how far management's word can be trusted. It does not rate price. Price is judged by the option scores, mainly by Buffett and SOIC when seated. The Analyst card states "valuation not scored here".

Seven sections, each scored 0 to 3. No weights.

| ID | Section (questions.md) | Lender set |
|---|---|---|
| S1 | Guidance versus delivery (section 1) | same |
| S2 | Earnings quality and accounting (section 2) | same |
| S3 | Cash, receivables, working capital (section 3) | replaced by lender asset quality (section 8) |
| S4 | Debt and funding (section 4) | read as funding: deposit quality and covenants only |
| S5 | Related parties and group companies (section 5) | same |
| S6 | Promoter: pledge, selling, succession (section 6) | same |
| S7 | Board, auditors, independent directors (section 10) | same |

Regulation (section 9) and capital allocation (section 7) are not scored. They only raise or clear a gate (below). Sections 11 and 12 of questions.md are not scored either.

**The 0 to 3 ladder (the same for every seat):**
- 3: every core question in the section is answered with a number and its date in the brief, and no red flag from checks.md fires.
- 2: answered with numbers, and one flag fires with a reason stated in the brief.
- 1: partial (words but no number), or a flag with no stated reason.
- 0: deflected, declined, or the brief has nothing.

Each number carries a state word: `answered`, `partial`, `deflected`, `no data` or `unverified`. A 0 for "no data" and a 0 for "declined on three calls" mean different things and both stay visible.

**The `unverified` state.** A fact whose only source is a web page, an aggregator, a news item or a recollection, and which has not been read against the filing, does not earn points. A section that rests on such a fact alone scores 0 with the state `unverified (source)`; the brief line names the source and what filing would settle it. When the filing is read the state changes and the section can be re-scored. A fact from a seat's own brain is not unverified if its source id is a filing or a dated transcript.

A company that states a no-guidance policy: S1 scores 2 if it gives another numeric anchor, 1 if it gives none (questions.md Q1.7).

**Evidence rule.** Company facts come only from the brief. A seat may score a section only from a line in the brief or a dated source in its own brain, and must name which. A fact that came from the seat's own brain and not from the brief is listed in the trust table as `added in debate` and does not count toward coverage. No seat may lift a number because its pillar likes the company.

**Who may score which section (competence map).** A seat outside its competence writes `-` for that section. It may still argue in debate and dispute a number, but it gives no number, and the median ignores it.

| Section | Seats that may score it |
|---|---|
| S1 Guidance versus delivery | Analyst, the company seat |
| S2 Earnings quality and accounting | Analyst, the company seat, SOIC |
| S3 Cash, receivables, working capital | Buffett, the company seat, Analyst |
| S4 Debt and funding | Buffett, the company seat, Analyst |
| S5 Related parties | Analyst, the company seat, SOIC |
| S6 Promoter | Analyst, the company seat, SOIC |
| S7 Board, auditors, independent directors | Analyst, the company seat, SOIC |

"The company seat" is the seat built for the stock being rated (for BIOCON, the BIOCON seat); with none seated the section has the other named seats only. The Chair may add a seat to a section for this run with one line of reason in `brief.md`; the default map is the seat's own, not from any source. S1 has two named seats, so it will often be marked `thin`; that is the honest state.

## Before Round 1: the data pack and the completeness gate

The Chair builds the data pack with `scripts/build_data_pack.py` (it reads the company's data-pack spec and the seat's brain, computes derived figures and marks stale lines) and puts it at the top of `brief.md`. The first lines of the pack are the gate:

- `BRIEF COMPLETE`, or `BRIEF INCOMPLETE: missing <lines>; stale <lines>`. A required line with no source is missing. A line older than its limit is stale.
- When incomplete, the Chair says so in one line to the user before Round 1 and asks whether to fetch first or run knowing the holes. If the user says run, the holes stay written at the top of `brief.md` and in the report.
- If S5, S6 or S7 data is missing, the Analyst writes "brief incomplete" before scoring those sections, and each scores 0 `no data`. Nobody fills a hole with an assumption.
- Web-sourced lines in the pack carry `unverified` and the filing that would settle them.

## How the council sets the numbers

- **Round 1.** Every seat's card adds `SECTION SCORES: S1 n (state) · S2 n (state) ...`, and `-` for any section where it has no basis. The Analyst fills all seven and names the brief line or source behind each. It also adds `GATES RAISED:` (a gate letter, the document and its stage, or `none`).
- **Chair notes after Round 1.** The Chair builds the trust table: for each section, every seat's number, the median and the spread. Any section with spread 2 or more is a candidate crux. The Chair puts the widest ones (at most three in all, counting the ordinary cruxes) into the Round 2 prompt.
- **Round 2.** Each seat answers `SECTION DISPUTES:` for each disputed section: its number, the evidence (brief line or source id) and what would move it. A seat moves a number only for a better argument or a new fact, and says which. The Analyst also states which of its questions got answered.
- **Round 3.** `draft-resolution.md` carries the table as it stands. A seat may add `SECTION AMENDMENT: Sn x to y, one line` or dissent from a number. Dissent on a section is reported, not hidden.
- **Final number per section.** The median of the numbers given in the last round by seats that are competent for the section (a `-` is ignored; a number from a seat outside the map is not taken). With an even count, take the lower of the two middle numbers. If fewer than three seats scored a section, it is marked `thin`. If only the Analyst scored it, it is marked `analyst only`. The Chair computes and never invents a number.

Why the median: one enthusiastic or one hostile seat cannot move it alone. Why the lower middle: the cost of trusting too early is higher than the cost of waiting.

## Chair checks before anything is published

- **Arithmetic.** Every number the Chair puts into a draft resolution or the report is recomputed (by code in the data pack, or by hand with the working shown) and marked `checked`. A wrong share in an earlier round (53% where 50.9% was right) was caught only because a seat noticed.
- **Base year.** Any base-year figure a verdict leans on (a "fell 62%" line) is re-derived from the data pack before it reaches the report. If the base year is not in the pack, the line is dropped or marked `base year not on record`.

## Gates (they override the total)

Any seat can raise a gate in writing, with the document and its stage. A gate stands when the Analyst or at least two other seats confirm the stage from the brief. A gate that stands is applied after the table, whatever the total.

| Gate | Trigger | Effect |
|---|---|---|
| G-A | A regulator finding (final or confirmatory order) of diversion or misstatement | Sell leans 7 or more |
| G-B | Auditor resigned before term, reasons not read or citing non-cooperation | Sell leans 7 or more |
| G-C | Pledge invoked, or above the SEBI reason line with no stated reason | Sell leans 7 or more |
| G-D | Related-party flows well above the approved ceiling | Sell leans 7 or more |
| G-E | Interim order or show cause notice only, or a first loss estimate still unvalidated | Caps at Wait |

An interim order is an allegation, not a finding. Keep the two apart (frameworks.md section 3).

## Coverage and bands

- **Coverage** = sections with any data in the brief out of 7, counted from the brief (the data pack) only, never from a seat's own brain. A section whose only evidence was brought in by a seat counts as no coverage and is listed `added in debate`. Print it beside the rating, never inside it: `Trust 14/21, coverage 5/7, gates standing: none`.
- **Bands** (the seat's own, uncalibrated, not from any source): 18 to 21 answered and clean; 12 to 17 answered with open flags; 7 to 11 mostly partial; 0 to 6 unanswered or declined. A gate overrides the band.
- Every printed band carries the words: `seat's own bands, not from any source, uncalibrated`. This stays until the pre-registered check below has been run and passed.
- Most briefs will land in the low bands. The Analyst's own corpus shows only 60 of 269 analyst questions got a direct answer (questions.md section 13). That is the honest result. Do not tune the ladder to push scores up.

## How the rating feeds the Buy, Wait and Sell call

- The option scores come from the seat cards as usual (scoring.md). Trust is a separate number and is never an option score.
- **Trust cap (override, applied with the others in scoring.md).** The Chair may not recommend A Buy when a gate stands, when the trust rating is below the 18 to 21 band, or when the brief has no current price and latest results. The Chair then recommends B Wait and uses the WAIT label, naming the trigger that turns it into Buy and the date.
- **Wait list.** A stock with trust 12 or more, no gate standing, held at Wait only because price or results are missing, is printed as `Wait list: trust good, entry not yet`. This is a printed label, not a new number.
- The report prints the final table (template below) and says which sections moved in debate.

## Report block (goes in verdict.md after the Scorecard)

```markdown
## Trust table (council numbers)

| Section | Final | State | Seat numbers | Spread | Moved? |
|---|---|---|---|---|---|
| S1 Guidance | 2 | answered | Analyst 2, Buffett 2, SOIC 3, Bezos - | 1 | no |

Trust 14/21 · Coverage 5/7 · Gates standing: none · Seat's own bands, not from any source, uncalibrated
Brief gate: BRIEF INCOMPLETE (missing D09, D10) · Added in debate: S3 receivable days (BIOCON seat brain) · Unverified: S6 pledge line (web)
```

The room's JSON files have no field for this, so the table lives in `verdict.md` only. Put one line about any standing gate in `verdict.json` `override_note`.

## Pre-registered check (run 2026-10-29, result below)

Take the 10 governance cases in `brains/india-market-analyst/stories.md` (A1 to A10). Score each on the 0 to 3 ladder from its "What was visible earlier" lines only, blind to the outcome paragraph, and write the predicted band down first. Pass bar: at least 7 of the 10 land at 11 or below, or hit a gate, on the earlier data. Fail means the bands are not usable and the card drops them.

Limits to state with the result: those cases were chosen because they went wrong, so a pass shows the rating notices trouble, not how often it raises a false alarm. A second check after three real councils: the Chair lists each seat's rating next to the verdict, and if the table and the Round 2 cruxes disagree on which section was the problem in two of three, the sections are mis-scoped.

### Result of the first run (2026-10-29)

Method: a fresh agent scored 14 anonymized cases from their "What was visible earlier" lines only, in shuffled order, not told which were trouble cases. The 9 scorable cases from A1 to A10 plus 5 comparison cases (stories 15, 16, 18, 19, 20: calls with no enforcement outcome in the notes). Case A5 (DHFL branch audit) has no "visible earlier" line and could not be scored. Names were removed; the model may still recognise some cases.

- **Pre-registered bar, on the letter: passed.** 9 of the 9 scorable trouble cases landed at 11 or below or hit a gate (9 of 10 if A5 counts as a miss). Bar was 7 of 10.
- **It does not show the bands work.** All 14 cases landed in the 0 to 6 band, including all 5 comparison cases. Average total: trouble cases 2.9, comparison cases 1.6. The comparison cases scored lower than the trouble cases, the wrong way round. The text for each case is a few lines, so most sections read "no data" and every case scores near zero. The bar is met by thin evidence alone.
- **Hindsight leaks.** The "visible earlier" lines for Gensol, Satyam and IndusInd cite later orders. The only gates that fired were Satyam's G-A (from a Tribunal finding) and IndusInd's G-E (from a SEBI order). Gensol scored highest (6) because its text includes the order record.
- **What this means:** the check cannot separate good from bad on this material, so the 12 to 17 and 18 to 21 bands are untested. Until a test with fuller briefs exists, treat the table, the coverage figure and the gates as the output, and print the bands only with the uncalibrated label. A better test needs full-length briefs for several companies where the outcome is known afterwards, scored before the outcome is read.

