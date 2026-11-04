# Handoff B: SOIC persona and a stock-framework funnel (read handoff-2026-11-04-master.md first)

Goal: back a sector funnel with the SOIC council seat and the SOIC learning vault: for a sector of about 50 listed companies, show the 2 to 3 that clear the SOIC bars and are worth reading closely, and say why the rest are not. Frame it as a screen shortlist, never buy/sell/hold.

## Hard constraints from the repos
- soic-ladder CLAUDE.md: screen, not advice; thresholds only from rulebook/soic-ladder-rules-v1.yaml; observations never gate; no mechanical sector rule has been shown to beat chance (price rule 5 of 10, growth breadth 4 of 10; stage rule scored PASS marginal 8 of 10 and its EMA leg adds nothing over plain RS52). A pick rate must be compared to a random pick rate (base rate 63.3% grew sales and PAT; Q1 leader test 15 of 20 vs 11.5 by chance).
- council-soic is the SOIC course seat (528 notes, framework list S001), not the instructor; learning-vault-invest holds the gated persona wiki; every quote cited and checked.
- Any ranking claim needs a pre-registered rule, a control, and a scorecard before it is shown.

## What exists
- Ladder gates G0 (sales and profit growth), G1 (leverage), G8 (entry timing); CANDIDATE / WATCH / INSUFFICIENT; 48 CANDIDATE stock sheets; stage board and company layer (docs/idea/stage-board/); Grill Sheet Q1-Q20; Q7 capex, Q8/9/11 valuation, Q15-17 timing; decision-frameworks-v1.md (20 frameworks); sector wiki notes (36 modules).
- BIOCON courtroom as a worked forensic example: seven lamps S1 guidance, S2 growth quality, S3 cash, S4 debt, S5 related parties, S6 governance and promoters, S7 auditor. Lamp scoring caps and Wait position (court_rules.py, build_report.py).

## Loopholes to examine (from this chat)
- Mixed state: growth up, profit down, cash down scored Wait; does the lamp system separate a good business with a bad year from a weak one? Lamps rest on what management states with a date, so a silent management scores low regardless of truth.
- Trust bands untested; model readers below their own check bar.
- Gates use screener fields (Screener vs filing differences: FY25 profit gap 416 crore unexplained).
- Peers are an NSE bucket, not rivals (Q4 mapping trap); Shariah and quality screens not integrated.
- Survivorship: today's constituents only.

## Tasks
1. grill-me the owner on what "worth your time" means (reading time, not return), the sector chosen for the pilot (suggest Healthcare/Pharma, BIOCON peers), and the cut (top 2 to 3 of about 50).
2. Design the funnel on paper: universe (sector) -> hard gates (rulebook) -> forensic lamps (cash, debt, related parties, auditor) -> persona questions from council-soic -> shortlist plus a reasons table for the dropped names. Each step cites rule id or source.
3. Pre-register the rule and the control (random 2 to 3 per sector, shuffled labels), define the scorecard and window, then run offline (no model calls where possible).
4. Use council-soic + learning-vault-invest for the qualitative step; check every cited quote byte-exact; log unverified.
5. Pilot on one sector, publish the shortlist with its scorecard and its limits; do not name sectors or picks as advice.

## Open decisions for the owner
Sector for the pilot; whether the output may rank or only list; how much Shariah screening to integrate (real screen needs Mac + NotebookLM, no VPS job); whether to extend lamps to all 500 names or stop at the pilot.
