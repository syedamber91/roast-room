# Design: courtroom phases on free models, hybrid handoff (approved by the owner 2026-10-31)

Source notes: brainstorms/2026-10-31-courtroom-offload-to-free-models.md (local, gitignored). Tickets: docs/specs/free-model-offload/.

## Goal
More companies at the same quality. Paid Claude stays only where no code can check the work.

## Approach chosen: C, hybrid
A VPS job drafts phases 3 and 4 on free models. A short Claude session finishes the rest.

## Pieces
1. **Draft (per company).** A session folder in today's shape: `case-book.md`, `case.json`, `hearing.md` with the lawyer and convict turns that passed the guard. Plus `escalations.jsonl` (one line per turn: model, issue, turn, tries, escalated, seconds) and `draft-status.json` (turns heard, passed first try, escalated, models used). An escalated turn is left as a marked gap (`### A2 Convict` then `ESCALATED`), never as a half-passing answer.
2. **VPS job `courtroom-draft`.** Runs phases 3-4 on the models that passed their pre-registered trials. Retry twice with the guard's notes, then mark the turn escalated (convict_loop.py, T3). Per-model fallback for timeouts and disconnects. Public filings and the company brain only; never a seat built from SOIC course text. Network-bound, so no CPU lock; the guard runs on a copy. New job name must be on main and one run of any job must complete before the first dispatch.
3. **Handoff.** A short Claude session: Sonnet answers only the escalated turns; judge notes, close and final run on Claude; spot-check 5 random free-model answers; build and publish the report. For companies 1 to 3 the owner reads a sample first.

## Rules carried over
- Trials come before use. Bars are pre-registered before any run: docs/courtroom-model-trial-prereg.md (convict), docs/courtroom-lawyer-trial-prereg.md (lawyer), and a judge-trial pre-registration (T5) with the bar: position Wait, trust within 2 of Sonnet's, each section within 1.
- A model is dropped for a phase when its escalation rate is above a threshold set from trial data (30% is a placeholder).
- Escalation rate per company is the cost number to track.
- Judge phases stay on Claude until the judge trial passes.
- S1 and S5 wording fixed first (T2) so Claude and free judges are scored by one rule.

## Out of scope
Moving the judge phases; building seats for new companies (PIIND next, third company not named) until the BIOCON trials finish.

## Testing
Offline unit tests with fake chat and fake guard functions (no network, no key). One trial per phase on BIOCON against the Sonnet baseline. A first VPS dispatch on BIOCON only, compared with the Sonnet hearing already published.
