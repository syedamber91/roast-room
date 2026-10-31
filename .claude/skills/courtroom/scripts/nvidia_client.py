"""Tiny NVIDIA chat client for the model trial. Key comes from NVIDIA_API_KEY, never printed."""
import json
import os
import time
import urllib.request

URL = "https://integrate.api.nvidia.com/v1/chat/completions"


def chat(model: str, prompt: str, max_tokens: int = 3000, timeout: int = 300) -> dict:
    """One call. Returns {text, seconds, error}. Reasoning models may put text in reasoning_content; we only keep content."""
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": prompt}],
                       "temperature": 0, "max_tokens": max_tokens}).encode()
    req = urllib.request.Request(URL, body, {"Authorization": "Bearer " + os.environ["NVIDIA_API_KEY"],
                                             "Content-Type": "application/json"})
    start = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            msg = json.load(r)["choices"][0]["message"]
        return {"text": (msg.get("content") or "").strip(), "seconds": round(time.time() - start, 1), "error": ""}
    except Exception as e:  # report, never hide
        return {"text": "", "seconds": round(time.time() - start, 1), "error": f"{type(e).__name__}: {str(e)[:120]}"}
