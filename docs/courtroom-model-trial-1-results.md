# Trial 1 results: convict turns on free models (2026-10-31)

Bars: docs/courtroom-model-trial-prereg.md (fixed before any answer was read). 15 turns (I5, I6, I7 x A1-A3, WA1, WA2), 2 runs per model, scored by `check_hearing.py`. Sonnet's own answers on the same 15 turns: 7 guard FAIL notes.

**All 8 models FAIL the pre-registered bars. 4 of the 8 are also inconclusive because most calls never returned.**

| Model | Calls dropped by the network (of 30) | Empty answers (run1/run2, of 15) | Guard FAIL notes (run1/run2) | Invented quotes | States = Sonnet (of 15) | Verdict |
|---|---|---|---|---|---|---|
| nvidia/nemotron-3-ultra-550b | 1 | 1 / 0 | 58 / 48 | 5 / 5 | 8 / 7 | FAIL |
| nvidia/nemotron-3.5-super-vl-120b | 2 | 5 / 8 | 27 / 48 | 0 / 0 | 5 / 3 | FAIL |
| nvidia/nemotron-3.5-lightning-30b | 0 | 6 / 5 | 44 / 38 | 1 / 1 | 4 / 3 | FAIL |
| openai/gpt-oss-20b | 2 | 6 / 8 | 83 / 79 | 18 / 8 | 3 / 2 | FAIL (invents quotes) |
| mistralai/mistral-large-4-1t | 22 | 11 / 11 | 66 / 66 | 0 / 0 | 2 / 3 | INCONCLUSIVE |
| minimaxai/minimax-m3.1-flash | 29 | 15 / 14 | 90 / 84 | 0 / 0 | 0 / 1 | INCONCLUSIVE |
| stepfun-ai/step-5-preview | 29 | 15 / 14 | 90 / 84 | 0 / 0 | 0 / 0 | INCONCLUSIVE |
| z-ai/glm-5.3-flash | 30 | 15 / 15 | 90 / 90 | 0 / 0 | 0 / 0 | INCONCLUSIVE |

Why the four are inconclusive: "Remote end closed connection" or connection reset on 22 to 30 of 30 calls. I ran 8 models at once with a 55,000-token prompt each, so the load may be mine. They must be re-run one at a time before anyone says they are bad. Kimi K2.6 (404), Kimi K2 (410), DeepSeek V4.1 Flash (timeout) and Gemma 4 31B (503) never answered at all.

What the failures were made of (run 1, guard type):
- Nemotron 3 Ultra: number-date 21, no-speech-id 16, quote-source 12, turn-shape 8. It reads the record but mis-dates figures and cites ids that carry no speech.
- Nemotron 3.5 Super VL: turn-shape 23, has-evidence 4, nothing else. 10 of 15 turns had zero notes. Its trouble is format, which a retry with the guard's notes (T3) may fix.
- Nemotron 3.5 Lightning: turn-shape 30.
- Sonnet: number-date 6, quote-source 1.

Reading: no free model matches Sonnet on a first attempt today. Super VL is the one worth a retry test, because its failures are format only. Ultra is the strongest on substance (states match Sonnet on 7 to 8 of 15) but invents quotes.

Not claimed: that any figure in these answers is right. Only the guard's checks were run.

## Follow-up (2026-10-31): retry loop and sequential re-run

Retry loop = `convict_loop.run_turn` (2 retries with the guard's notes, then escalate). One run of 15 turns each.

| Model | Turns escalated | Guard fail notes (Sonnet: 7) | Invented quotes | States match Sonnet (of 15) | Verdict |
|---|---|---|---|---|---|
| Nemotron 3 Ultra 550B + loop | 4 (27%) | 7 | 1 | 9 | FAIL (quote, state bar 12) |
| Nemotron 3.5 Super VL 120B + loop | 6 (40%) | 35 (6 empty turns count against it) | 0 | 4 | FAIL |
| Nemotron 3.5 Lightning 30B + loop | 10 (67%) | 55 | 0 | 2 | FAIL |

- Retries cut Ultra's guard failures from 58/48 to 7, equal to Sonnet's 7. Only Ultra is under the 30% placeholder escalation rate.
- Mistral was stopped by the owner (most calls dropped after 300 s even one at a time). Mistral, MiniMax, Step 5 and GLM remain INCONCLUSIVE: the sequential re-run ended with 88 "Connection refused" errors from the container and 1 answer returned, so no verdict can be drawn.
- The trial container's network failed late in the re-run; re-test those four from a clean session or the VPS.
