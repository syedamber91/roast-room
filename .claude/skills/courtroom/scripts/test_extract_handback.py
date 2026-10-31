import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("eh", HERE / "extract_handback.py")
eh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eh)


def task_file(tmp_path, report):
    rows = [{"message": {"content": [{"type": "text", "text": "thinking"}]}},
            {"message": {"content": [{"type": "tool_use", "name": "SubagentHandback", "input": {"message": "old report"}}]}},
            {"message": {"content": [{"type": "tool_use", "name": "SubagentHandback", "input": {"message": report}}]}}]
    f = tmp_path / "t.output"
    f.write_text("\n".join(json.dumps(r) for r in rows) + "\nnot json\n", encoding="utf-8")
    return f


def test_the_last_report_is_taken_and_a_bare_bold_label_gets_its_colon_and_its_line(tmp_path):
    report = "**ANSWER**\nFirst line of the answer.\n\n**MOVE**\ncite\n\n**EVIDENCE**\n- one fact\n\n**STATE I CLAIM**\npartial\n\n**WHAT WOULD SETTLE IT**\nThe page."
    out = eh.plain_labels(eh.last_handback(task_file(tmp_path, report)))
    assert "ANSWER: First line of the answer." in out and "MOVE: cite" in out and "STATE I CLAIM: partial" in out
    assert "EVIDENCE:\n- one fact" in out and "WHAT WOULD SETTLE IT:\nThe page." in out and "old report" not in out


def test_a_report_already_in_label_colon_shape_is_left_alone(tmp_path):
    report = "ANSWER: Already fine.\nMOVE: cite\nEVIDENCE:\n- a\nSTATE I CLAIM: answered\nWHAT WOULD SETTLE IT: nothing"
    assert eh.plain_labels(report) == report
