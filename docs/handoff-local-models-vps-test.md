# Handoff: test local (self-hosted) models on the VPS for the courtroom

Written 2026-10-31 for a new Claude Code cloud session. Owner's decision: try downloading free open models (a Qwen or similar) on the VPS to do the courtroom's convict (and later lawyer) turns. Owner has not seen any local-model result yet.

## Goal
Find out, by measurement, whether a model running on the VPS can write convict turns that pass the same pre-registered bars the hosted models were held to. Stop at the first failed gate; report plainly.

## Read first (in this repo, branch `integration/free-model-offload`)
- `docs/specs/free-model-offload/SPEC.md` and `docs/superpowers/specs/2026-10-31-free-model-offload-design.md` (the plan, approach C).
- `docs/courtroom-model-trial-prereg.md` (the bars) and `docs/courtroom-model-trial-1-results.md` (hosted results, incl. the retry-loop follow-up).
- Scripts in `.claude/skills/courtroom/scripts/`: `model_trial.py` (run/score/table), `convict_loop.py` (retry twice with guard notes, then escalate), `loop_trial.py` (runs the loop on 15 turns), `nvidia_client.py` (hosted client; a local one must return the same `{text, seconds, error}`), `check_hearing.py` (the guard).
- Session data: `sessions/2026-10-30-court-biocon-live-example/` (hearing.md = Sonnet's answers, case-book.md, work/model-trial/ = every trial answer so far).

## The task
15 turns (issues I5-I7, turns A1 A2 A3 WA1 WA2). Each prompt is about 55,000 tokens (see `build_prompt`). The guard scores each answer; bars are in the prereg.

## Facts already measured (hosted NVIDIA models)
- Sonnet baseline: 7 guard FAIL notes over the 15 turns.
- Best: Nemotron 3 Ultra 550B + retry loop: 7 fail notes, 1 invented quote, 9 of 15 states match Sonnet, 4 of 15 turns escalated (27%). Still FAIL (bars: 0 invented quotes, 12 of 15 states).
- Super VL + loop: 6 of 15 escalated. Lightning 30B + loop: 10 of 15 escalated, 2 states match.
- Small models do worse; a local 7-14B model will very likely do worse than Lightning 30B. Treat success as unlikely and say so if the numbers show it.
- Mistral, MiniMax, Step 5, GLM: inconclusive (connection drops / refused).

## Unknown, check first (nothing about the VPS was verified from the cloud)
1. VPS hardware: `nproc; free -g; lspci | grep -i -E "nvidia|amd"; df -h ~`. soic-ladder's CLAUDE.md says 4 cores; GPU and RAM not recorded.
2. How a cloud session reaches the VPS. soic-ladder uses a self-hosted GitHub Actions runner (`soic-run.yml`, jobs run by `git push origin HEAD:run/<job>/<name>` or workflow dispatch; a NEW job name must be on `main` and one run of any job must complete first). It is UNCHECKED whether `syedamber91/roast-room` has a runner or whether the test must go through soic-ladder's runner or by the owner running commands in tmux on the VPS. Ask the owner if unclear.
3. Exact current Qwen model names and licences: look them up; do not rely on memory.

## Plan (stop at the first failed gate)
1. Hardware check. No GPU and under 16 GB RAM: stop and report; hosted models are bigger and free.
2. Install llama.cpp or Ollama; load one Qwen in the 7-14B class (4-bit).
3. Time ONE real 55,000-token prompt. Over 5 minutes: stop and report.
4. Add a local client with the same return shape as `nvidia_client.chat`; run the 15-turn trial with `loop_trial.py`-style retries; score with `model_trial.py score`.
5. Write the bars BEFORE the run (copy the hosted prereg; add the 5-minute speed bar) and commit them first.
6. Write results to `docs/courtroom-model-trial-2-local-results.md`; commit and push.

## Safety rules
- CPU: the VPS was host-throttled to 20% CPU on 2026-09-26 after sustained heavy load, and the un-throttle works once per 7 days. Cap any long run (for example `systemd-run --scope -p CPUQuota=200%` or `nice` plus `cpulimit`), run in tmux, and watch `vmstat` steal. Do not run it beside a soic-ladder heavy job.
- Privacy: this courtroom uses public filings only, so hosted models are fine; local is only needed for private data. Say so in the results.
- NVIDIA API key is read from the environment and never printed.
- No PR unless the owner asks. Commit with the attribution lines. Keep replies short and plain.
- Do not edit the hosted-trial results already recorded.

## Open owner questions
Target number of companies per month; the third company after PIIND; whether T1/T5/T6/T7 proceed after this test.
