"""Offline tests for convict_loop. A fake chat function stands in for the network; a fake guard stands in for check_hearing."""
import json
import sys
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
import convict_loop as cl  # noqa: E402

LABEL = "I5 A1 Convict"
HEARING = "## I5 Test\n### A1 Convict\n\nold\n\n"


def fail(msg):
    return SimpleNamespace(turn=LABEL, severity="FAIL", message=msg)


def make_chat(replies):
    """Returns a chat function that hands out the replies in order, and a list of the prompts it saw."""
    seen = []

    def fake(model, prompt, **kw):
        seen.append(prompt)
        return replies[len(seen) - 1]
    return fake, seen


def ok(text="ANSWER: fine"):
    return {"text": text, "seconds": 1.0, "error": ""}


def guard_says(*per_call):
    """Guard that returns the given note lists, one per call."""
    calls = iter(per_call)
    return lambda hearing: next(calls)


def run(tmp_path, replies, guard):
    fake, seen = make_chat(replies)
    log = tmp_path / "esc.jsonl"
    res = cl.run_turn("m/x", "I5", "A1", HEARING, log, chat_fn=fake, prompt_fn=lambda i, t: "PROMPT", guard_fn=guard)
    return res, seen, log


def test_pass_first_try(tmp_path):
    res, seen, log = run(tmp_path, [ok()], guard_says([]))
    assert res["escalate"] is False and res["tries"] == 1 and res["text"] == "ANSWER: fine"
    assert len(seen) == 1 and seen[0] == "PROMPT"


def test_pass_on_retry_feeds_guard_notes_back(tmp_path):
    res, seen, _ = run(tmp_path, [ok("bad"), ok("good")], guard_says([fail("quote not found")], []))
    assert res["escalate"] is False and res["tries"] == 2 and res["text"] == "good"
    assert "quote not found" in seen[1] and seen[1].startswith("PROMPT")


def test_escalate_after_two_retries(tmp_path):
    notes = [fail("still wrong")]
    res, seen, log = run(tmp_path, [ok("a"), ok("b"), ok("c")], guard_says(notes, notes, notes))
    assert res["escalate"] is True and res["tries"] == 3 and res["text"] == "c"
    assert len(seen) == 3


def test_empty_answer_counts_as_a_failed_try(tmp_path):
    res, seen, _ = run(tmp_path, [ok(""), ok("fine")], guard_says([]))
    assert res["tries"] == 2 and res["escalate"] is False
    assert "empty" in seen[1].lower()


def test_api_error_retries_then_escalates(tmp_path):
    err = {"text": "", "seconds": 0.5, "error": "HTTPError: 500"}
    res, seen, _ = run(tmp_path, [err, err, err], guard_says())
    assert res["escalate"] is True and res["tries"] == 3 and res["text"] == ""
    assert "HTTPError: 500" in seen[1]


def test_only_this_turns_notes_count(tmp_path):
    other = SimpleNamespace(turn="I6 A2 Convict", severity="FAIL", message="not mine")
    res, _, _ = run(tmp_path, [ok()], guard_says([other]))
    assert res["escalate"] is False and res["tries"] == 1


def test_log_gets_one_line_per_turn(tmp_path):
    _, _, log = run(tmp_path, [ok()], guard_says([]))
    lines = log.read_text().splitlines()
    assert len(lines) == 1
    row = json.loads(lines[0])
    assert set(row) == {"model", "issue", "turn", "tries", "escalated", "seconds"}
    assert row["model"] == "m/x" and row["escalated"] is False and row["seconds"] == 1.0


def test_log_appends_and_adds_up_seconds(tmp_path):
    notes = [fail("x")]
    _, _, log = run(tmp_path, [ok(), ok(), ok()], guard_says(notes, notes, notes))
    run(tmp_path, [ok()], guard_says([]))
    rows = [json.loads(line) for line in log.read_text().splitlines()]
    assert len(rows) == 2 and rows[0]["escalated"] is True and rows[0]["seconds"] == 3.0
