"""Offline tests for lawyer_trial.py: no model, no network. Pure functions get small strings; three tests read the real committed files."""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("lt", HERE / "lawyer_trial.py")
lt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lt)

SECTION = """## I5 Cash and working capital

### Q1 Lawyer

TO: the convict

QUESTION: Old Q1?

WHY I ASK: Q3.1, why is cash low

IF DEFLECTED: Give the line.

### A1 Convict

ANSWER: text.

STATE I CLAIM: partial

### Q2 Lawyer

TO: the convict

QUESTION: Old Q2?

WHY I ASK: Q12.2, capex

IF DEFLECTED: Give the multiple.

### A2 Convict

ANSWER: more.

STATE I CLAIM: Not in my record.

### Q3 Lawyer

TO: the convict

QUESTION: Old Q3?

WHY I ASK: Q3.4

IF DEFLECTED: x

### A3 Convict

ANSWER: end.

STATE I CLAIM: answered

## I6 Other
### Q1 Lawyer
TO: the convict
"""

NEW_Q = "TO: the convict\nQUESTION: New one?\nWHY I ASK: Q3.1, reason\nIF DEFLECTED: Again."
ISSUE = {"id": "I5", "name": "Cash", "analyst_questions": ["Q3.1"], "decisive": "Q3.1",
         "known_gaps": ["gap one"], "state": "examinable", "reasons": ["why"]}


def test_history_for_q1_is_empty_and_for_q2_ends_at_the_answer_before_it():
    assert lt.history_before(SECTION, 1).strip() == "## I5 Cash and working capital"
    h = lt.history_before(SECTION, 2)
    assert "### A1 Convict" in h and "Old Q1?" in h
    assert "Old Q2?" not in h and "### Q2 Lawyer" not in h


def test_the_last_convict_state_is_read_from_the_history_and_normalised():
    assert lt.last_state(lt.history_before(SECTION, 2)) == "partial"
    assert lt.last_state(lt.history_before(SECTION, 3)) == "not in my record"
    assert lt.last_state(lt.history_before(SECTION, 1)) == ""


def test_the_ladder_table_comes_from_the_prompts_file_not_from_this_module():
    ladder = lt.ladder_rows((lt.HERE.parent / "references" / "hearing-prompts.md").read_text())
    assert set(ladder) == {"answered", "partial", "deflected", "not in my record"}
    assert "number and the date" in ladder["partial"]


def test_ladder_instruction_is_fixed_by_state_for_q2_q3_and_absent_for_q1():
    ladder = {"partial": "ask for the number", "answered": "next question"}
    assert lt.ladder_instruction(1, "", ladder).startswith("Ask the decisive question")
    out = lt.ladder_instruction(2, "partial", ladder)
    assert "partial" in out and "ask for the number" in out


def test_question_sections_pastes_only_the_named_ids():
    qmd = "# t\n### Q3.1 Why low?\nbody one\n### Q3.2 Days?\nbody two\n### Q3.4 Other?\nbody four\n"
    out = lt.question_sections(qmd, ["Q3.1", "Q3.4"])
    assert "body one" in out and "body four" in out and "body two" not in out


def test_question_sections_names_an_id_it_cannot_find():
    assert "Q9.9" in lt.question_sections("### Q3.1 x\nbody\n", ["Q9.9"])  # missing is loud, never silent


def test_swap_replaces_only_the_named_lawyer_turn_of_the_named_issue():
    out = lt.swap_lawyer_turn(SECTION, "I5", 2, NEW_Q)
    assert "New one?" in out and "Old Q2?" not in out
    assert "Old Q1?" in out and "Old Q3?" in out and "### A2 Convict" in out
    assert out.count("### Q1 Lawyer") == 2  # the I6 section is untouched


def test_first_question_id_and_word_count_read_the_lawyers_fields():
    assert lt.first_question_id(NEW_Q) == "Q3.1"
    assert lt.first_question_id("QUESTION: x") == "missing"
    assert lt.question_words(NEW_Q) == 2


class P:
    def __init__(self, turn, guard, message, severity="FAIL"):
        self.turn, self.guard, self.message, self.severity = turn, guard, message, severity


def test_counts_use_only_lawyer_turns_of_the_trial_and_split_number_notes():
    problems = [P("I5 Q1 Lawyer", "lawyer-number", "999 is in neither"), P("I5 Q2 Lawyer", "turn-shape", "missing TO"),
                P("I5 A1 Convict", "turn-shape", "x"), P("I9 Q1 Lawyer", "turn-shape", "y"),
                P("I5 Q1 Lawyer", "turn-shape", "warn only", "warn")]
    assert lt.count_for(problems, {"I5 Q1 Lawyer", "I5 Q2 Lawyer"}) == (2, 1)


def test_verdict_applies_all_four_bars_and_fails_on_any_one():
    good = {"sonnet_fail_notes": 3, "self_agreement": 7,
            "runs": {"run1": {"fail_notes": 3, "number_notes": 0, "max_question_words": 40},
                     "run2": {"fail_notes": 1, "number_notes": 0, "max_question_words": 59}}}
    assert lt.verdict(good) == "PASS"
    for key, bad in [("fail_notes", 4), ("number_notes", 1), ("max_question_words", 60)]:
        r = {**good, "runs": {**good["runs"], "run2": {**good["runs"]["run2"], key: bad}}}
        assert lt.verdict(r) == "FAIL", key
    assert lt.verdict({**good, "self_agreement": 6}) == "FAIL"
    assert lt.verdict({k: v for k, v in good.items() if k != "self_agreement"}) == "FAIL"  # one run cannot show stability


def test_the_prompt_carries_the_rules_the_ladder_row_the_history_and_the_pasted_files():
    prompt = lt.build_prompt_from_parts(rules="RULES\nQUESTION [n] OF 3", issue=ISSUE, n=2, state="partial", ladder={"partial": "ask for the number"},
                                        hot="HOT", questions="QSEC", case_book="BOOK", history="HIST")
    for part in ("RULES", "HOT", "QSEC", "BOOK", "HIST", "ask for the number", "gap one", "QUESTION 2 OF 3", "You cannot open files"):
        assert part in prompt


def test_the_real_template_is_filled_with_no_placeholder_left_and_no_company_brain():
    prompt = lt.build_prompt("I5", 2)
    for placeholder in ("[n]", "[issue id", "[session]", "[analyst_questions]", "[decisive]", "[known_gaps]", "[state"):
        assert placeholder not in prompt
    assert "### A1 Convict" in prompt and "Q3.1" in prompt
    assert "brains/biocon-management" not in prompt  # no company brain path reaches the lawyer
    assert "### Q2 Lawyer" not in prompt  # the answer being asked for is never in the prompt


def test_the_real_hearing_gives_a_sonnet_baseline_for_every_trial_turn():
    base = lt.sonnet_questions()
    assert set(base) == {(i, n) for i in lt.ISSUES for n in (1, 2, 3)}
    assert all("QUESTION:" in v for v in base.values())
