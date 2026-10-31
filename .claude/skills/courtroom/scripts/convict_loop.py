#!/usr/bin/env python3
"""Convict loop: one free-model answer for one turn, checked by the guard, retried twice, else flagged to escalate.

    run_turn(model, issue, turn, hearing, log_path)  ->  {text, tries, escalate, seconds}

Steps for one turn:
  1. ask the model            2. clean the answer
  3. guard that turn alone    4. if it fails, ask again with the guard's notes added (2 retries at most)
  5. still failing? escalate=True (the caller sends this one turn to Sonnet)
  6. write one line to the escalation log
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from model_trial import build_prompt, clean, guard_notes, swap_turn  # noqa: E402
from nvidia_client import chat  # noqa: E402

RETRIES = 2


def turn_label(issue: str, turn: str) -> str:
    return f"{issue} {turn} Convict"


def notes_for_answer(text, issue, turn, hearing, guard_fn) -> list:
    """Plain-text notes that say why this answer failed. An empty list means it passed."""
    if not text:
        return ["The answer was empty."]
    problems = guard_fn(swap_turn(hearing, issue, turn, text))
    mine = [p for p in problems if p.turn == turn_label(issue, turn)]
    return [p.message for p in mine]


def retry_prompt(prompt: str, notes: list) -> str:
    bullets = "\n".join(f"- {n}" for n in notes)
    return f"{prompt}\n\nYour last answer failed the checker. Fix these and answer again:\n{bullets}\n"


def log_turn(log_path, model, issue, turn, tries, escalated, seconds) -> None:
    row = {"model": model, "issue": issue, "turn": turn, "tries": tries, "escalated": escalated, "seconds": round(seconds, 1)}
    with open(log_path, "a") as f:
        f.write(json.dumps(row) + "\n")


def run_turn(model, issue, turn, hearing, log_path, chat_fn=chat, prompt_fn=build_prompt, guard_fn=guard_notes) -> dict:
    base = prompt_fn(issue, turn)
    prompt, text, seconds = base, "", 0.0
    for tries in range(1, RETRIES + 2):
        res = chat_fn(model, prompt, max_tokens=12000, timeout=900)
        seconds += res["seconds"]
        text = clean(res["text"]) if res["text"] else ""
        notes = [res["error"]] if res["error"] else notes_for_answer(text, issue, turn, hearing, guard_fn)
        if not notes:
            break
        prompt = retry_prompt(base, notes)
    escalate = bool(notes)
    log_turn(log_path, model, issue, turn, tries, escalate, seconds)
    return {"text": text, "tries": tries, "escalate": escalate, "seconds": round(seconds, 1)}
