import json

from assemble_hearing import assemble


def test_turn_files_join_in_hearing_order_under_the_right_headings(tmp_path):
    (tmp_path / "work" / "turns").mkdir(parents=True)
    (tmp_path / "case.json").write_text(json.dumps({"company": "ACME", "issues": [{"id": "I1", "name": "Why profit moved"}, {"id": "I2", "name": "Growth"}]}))
    turns = tmp_path / "work" / "turns"
    (turns / "I02__01__Q1 Lawyer.md").write_text("TO: the convict")
    (turns / "I01__02__A1 Convict.md").write_text("ANSWER: x")
    (turns / "I01__01__Q1 Lawyer.md").write_text("TO: the convict")
    (turns / "opening__01__Lawyer opening.md").write_text("Pressing I1.")
    text = assemble(tmp_path)
    order = [text.index(h) for h in ["## Opening", "## I1 Why profit moved", "### Q1 Lawyer", "### A1 Convict", "## I2 Growth"]]
    assert order == sorted(order)
    assert text.count("### Q1 Lawyer") == 2


def test_a_rest_turn_is_not_headed_as_a_question(tmp_path):
    (tmp_path / "work" / "turns").mkdir(parents=True)
    (tmp_path / "case.json").write_text(json.dumps({"company": "ACME", "issues": [{"id": "I1", "name": "Why"}]}))
    (tmp_path / "work" / "turns" / "I01__07__Q4 Lawyer.md").write_text("REST: the method's checks are covered.")
    text = assemble(tmp_path)
    assert "### Lawyer rest" in text and "Q4 Lawyer" not in text
