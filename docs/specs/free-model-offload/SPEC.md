# Spec: move courtroom phases to free models (written 2026-10-31 from the grill in brainstorms/2026-10-31-courtroom-offload-to-free-models.md)

Issue tracker: none is configured for this repo, so tickets are the files in this folder; a ticket is closed when its `Status:` line says `done` and its work is merged to the integration branch.

## Goal
More companies at the same quality (owner, Q1). Paid Claude stays only where no code can check the work.

## Decisions (owner, 2026-10-31)
- Phases: 1 fetch/extract, 2 brain + case book, 3 lawyer, 4 convict, 5 judge note/close, 6 judge final, 7 report/publish. Move 4 first, then 3, then 1-2 to the cheapest option. 5-6 only after a separate test.
- Quality check: guard on every turn; Sonnet spot-check of 5 random answers per company; owner reads a sample for companies 1-3 only.
- Where: trials in the cloud container, production as unattended VPS jobs.
- Failure policy: retry 2x with the guard's notes fed back, then escalate that one turn to Sonnet. Drop a model for a phase if its escalation rate is above a threshold set from trial data (30% placeholder).
- Judge trial bar (pre-register before any run): position Wait, trust within 2 of Sonnet's, each section within 1.
- Scale order: finish BIOCON trials, then PIIND, then a third company (owner has not named it).
- Privacy: public filings only go to NVIDIA hosted models; seats built from SOIC course text stay on Claude.
- Fix the S1 and S5 rule wording first so Claude and free judges are measured against one rule.

## Known facts (2026-10-31)
- build.nvidia.com catalog: 85 models; 8 answered a chat call; Kimi K2.6 404, Kimi K2 410, no Qwen. Reasoning models need max_tokens about 12000 (Mistral Large 4 used 2,999 of 3,000 tokens thinking and returned nothing).
- Trial 1 bars: docs/courtroom-model-trial-prereg.md. Harness: scripts/model_trial.py, scripts/nvidia_client.py.

## Tickets and graph
- T1 score trial 1 and pick convict model(s)            blocked by: trial runs finishing
- T2 fix S1 and S5 rule wording (+ tests)               blocked by: none
- T3 convict loop module: call, guard one turn, retry 2x, escalate flag, escalation log   blocked by: none
- T4 lawyer-turn trial: pre-register, then extend the harness   blocked by: none
- T5 judge trial pre-registration (bar above)           blocked by: T2
- T6 VPS job `courtroom-convict`                        blocked by: T1, T3
- T7 Sonnet spot-check script (5 random answers per company)    blocked by: T3
Frontier now: T2, T3, T4. T1 opens when the runs end.
