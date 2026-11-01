import json

from make_cards import build
from next_steps import steps_for


def session(tmp_path, turns):
    (tmp_path / "work" / "turns").mkdir(parents=True)
    case = {"company": "ACME", "issues": [{"id": "I1", "name": "Why profit moved", "known_gaps": ["gap"], "state": "examinable", "convict_files": ["a.md", "b.md"]}]}
    (tmp_path / "case.json").write_text(json.dumps(case))
    for name, body in turns.items():
        (tmp_path / "work" / "turns" / f"I01__{name}.md").write_text(body)
    return tmp_path


def test_a_fresh_issue_needs_the_first_question(tmp_path):
    assert steps_for(session(tmp_path, {}), "I01") == [("lawyer_q", "1")]


def test_an_unanswered_question_needs_the_convict(tmp_path):
    s = session(tmp_path, {"01__Q1 Lawyer": "TO: the convict"})
    assert steps_for(s, "I01") == [("convict_a", "A1")]


def test_an_answered_question_needs_the_next_question(tmp_path):
    s = session(tmp_path, {"01__Q1 Lawyer": "TO: x", "02__A1 Convict": "ANSWER: y"})
    assert steps_for(s, "I01") == [("lawyer_q", "2")]


def test_rest_leads_to_review_then_judge_note_then_both_why_answers_then_close(tmp_path):
    s = session(tmp_path, {"01__Q1 Lawyer": "TO: x", "02__A1 Convict": "a", "03__Q2 Lawyer": "REST: covered"})
    assert steps_for(s, "I01") == [("review", "")]
    s = session(tmp_path / "b", {"11__Lawyer review": "COVERED"})
    assert steps_for(s, "I01") == [("judge_note", "")]
    s = session(tmp_path / "c", {"11__Lawyer review": "x", "12__Judge note": "n"})
    assert steps_for(s, "I01") == [("convict_a", "WA1"), ("convict_a", "WA2")]
    s = session(tmp_path / "d", {"11__Lawyer review": "x", "12__Judge note": "n", "13__WA1 Convict": "a", "14__WA2 Convict": "b"})
    assert steps_for(s, "I01") == [("judge_close", "")]
    s = session(tmp_path / "e", {"15__Judge close": "done"})
    assert steps_for(s, "I01") == []


def test_cards_name_the_turn_file_the_agent_must_write(tmp_path):
    s = session(tmp_path, {})
    card, out = build(s, "lawyer_q", "I01", "2")
    assert out.name == "I01__03__Q2 Lawyer.md"
    assert "council-soic.md" in card.read_text() and "biocon-management" in card.read_text()   # the lawyer is told not to open the company brain
    card, out = build(s, "convict_a", "I01", "WA1")
    assert out.name == "I01__13__WA1 Convict.md" and "a.md, b.md" in card.read_text()
