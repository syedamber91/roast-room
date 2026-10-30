import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cc", HERE / "check_chapters.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)

PAGE = "Acme makes medicines in three businesses. Sales were 31,681 million in the year. It has 4 plants.\n"
CALL = "On the call the speaker said that growth in the generics business was driven by one very large order from a single customer in the quarter.\n"


def setup(tmp_path):
    ar = tmp_path / "ar"
    ar.mkdir(exist_ok=True)
    (ar / "p013.md").write_text(PAGE, encoding="utf-8")
    (ar / "p014.md").write_text("Acme sells insulin to hospitals.\n", encoding="utf-8")
    brain = tmp_path / "brain"
    brain.mkdir(exist_ok=True)
    (brain / "positions.md").write_text(CALL, encoding="utf-8")
    return ar, brain


GOOD = """## 1. The company in plain words
- Acme makes medicines in three businesses. (AR p13)
- Acme sells insulin to hospitals. (AR p14)
## 2. How it makes money
- Sales were 31,681 million in the year. (AR p13)
## 7. Glossary
- Insulin: a medicine that controls blood sugar. (AR p14)
"""


def run(tmp_path, text):
    ar, brain = setup(tmp_path)
    return cc.check(text, ar, [13, 14], brain)


def fails(problems):
    return [p for p in problems if p[0] == "FAIL"]


def test_a_clean_draft_passes(tmp_path):
    assert fails(run(tmp_path, GOOD)) == []


def test_planted_failure_line_without_a_page_id(tmp_path):
    bad = GOOD.replace("- Acme makes medicines in three businesses. (AR p13)", "- Acme makes medicines in three businesses.")
    assert any("no page id" in p[3] for p in fails(run(tmp_path, bad)))


def test_planted_failure_number_not_on_the_cited_page(tmp_path):
    bad = GOOD.replace("31,681", "41,681")
    assert any("41681" in p[3] for p in fails(run(tmp_path, bad)))


def test_a_number_cited_from_the_wrong_page_fails(tmp_path):
    bad = GOOD.replace("Sales were 31,681 million in the year. (AR p13)", "Sales were 31,681 million in the year. (AR p14)")
    assert any("31681" in p[3] for p in fails(run(tmp_path, bad)))


def test_planted_failure_page_outside_the_business_pages(tmp_path):
    bad = GOOD.replace("(AR p14)\n## 2", "(AR p99)\n## 2")
    assert any("not one of the business pages" in p[3] for p in fails(run(tmp_path, bad)))


def test_planted_failure_forward_looking_or_management_wording(tmp_path):
    bad = GOOD.replace("Acme sells insulin to hospitals.", "Acme will sell insulin to more hospitals.")
    assert any("forward-looking" in p[3] for p in fails(run(tmp_path, bad)))


def test_planted_failure_management_claim_wording(tmp_path):
    bad = GOOD.replace("Acme sells insulin to hospitals.", "Management guided that Acme sells insulin to hospitals.")
    assert any("forward-looking" in p[3] for p in fails(run(tmp_path, bad)))


def test_planted_failure_six_words_from_the_call_record(tmp_path):
    bad = GOOD.replace("Acme sells insulin to hospitals.", "Growth was driven by one very large order from a single customer.")
    assert any("convict's call" in p[3] for p in fails(run(tmp_path, bad)))


def test_long_two_sentence_and_praise_lines(tmp_path):
    long_line = "- " + " ".join(["word"] * 26) + ". (AR p13)\n"
    two = "- Acme makes medicines. It is based in India. (AR p13)\n"
    praise = "- Acme is a leading maker of medicines. (AR p13)\n"
    out = run(tmp_path, GOOD + long_line + two + praise)
    msgs = [p[3] for p in out]
    assert any("limit 25" in m for m in msgs) and any("more than one sentence" in m for m in msgs)
    assert any(p[0] == "warn" and "praise" in p[3] for p in out)


def test_missing_chapter_and_extra_chapter_fail(tmp_path):
    out = fails(run(tmp_path, GOOD.split("## 7.")[0]))
    assert any(p[1] == 7 and "missing" in p[3] for p in out)
    out2 = fails(run(tmp_path, GOOD + "## 5. Extra\n- Something. (AR p13)\n"))
    assert any("only chapters 1, 2 and 7" in p[3] for p in out2)
