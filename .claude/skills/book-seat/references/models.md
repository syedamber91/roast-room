# Models (all free NVIDIA endpoints, called from the VPS)

| Role | Default | Notes |
|---|---|---|
| Extractor (T3, re-looks, number-rule asks) | `nvidia/nemotron-3-ultra-550b-a55b`, thinking off, via `seat_orchestrator.client.nemotron_chat` | The super-120b endpoint answered 404 |
| Second reader / filler (T4) | `openai/gpt-oss-20b`, system prompt "Reasoning: low", max_tokens 6000, timeout 240s | Long reasoning used to empty the answer; empty answers are never cached |
| Independent scorer (T4) | first that answers of `google/gemma-4-31b-it`, `deepseek-ai/deepseek-v4.1-flash`, `moonshotai/kimi-k2.6`, `z-ai/glm-5.3-flash`, `mistralai/mistral-large-4-1t-a52b` | Must differ from extractor and reader. Moves on only on 404/410 (retired), never on a slow or empty reply. `meta/llama-3.3-70b-instruct` (410) and `mistralai/mistral-large-2-instruct` (404) were retired though listed |
| Public brain (T6) | Claude, from verified items only | Writer agents never read the book |

`/v1/models` lists retired names, so a model can be listed and still answer 404 or 410. Code: soic-ladder
`scripts/book_seat/models.py`. A book may swap a model at T0 (DECISIONS.md).
