from verify_plain import check_flags, check_line, check_rows

FLAGS = [{"id": "A1", "who": "analyst", "qid": "Q1", "flag": "Cash fell to 19,940 million", "evidence": "I5"},
         {"id": "S1", "who": "soic", "qid": "Q3", "flag": "Operating cash fell from 40,612 to 19,940", "evidence": "I5"}]


def merged(**over):
    m = {"id": "F1", "members": ["A1", "S1"], "found_by": "both", "text": "Cash fell to 19,940 million", "kid": "The money coming in got much smaller", "teen": "Cash from running the business fell to 19,940 million."}
    m.update(over)
    return [m]


def test_a_clean_merge_passes():
    assert check_flags(FLAGS, merged()) == []


def test_text_must_be_copied_exactly_and_every_flag_used_once():
    assert any("copied exactly" in p for p in check_flags(FLAGS, merged(text="Cash fell sharply")))
    assert any("appears 0 times" in p for p in check_flags(FLAGS, merged(members=["A1"], found_by="analyst")))


def test_found_by_must_match_the_members():
    assert any("found_by" in p for p in check_flags(FLAGS, merged(found_by="analyst")))


def test_kid_lines_have_no_digits_and_teen_figures_come_from_the_source():
    assert check_line("x", "It fell by 5 coins", 12, True, "") != []
    assert check_line("x", "It fell to 19,940 million", 30, False, "cash 19,940") == []
    assert any("not in the source" in p for p in check_line("x", "It fell to 21,000", 30, False, "cash 19,940"))


def test_advice_words_are_refused_and_rows_must_all_be_present():
    assert any("buy, sell or hold" in p for p in check_line("x", "You should buy it", 20, False, ""))
    assert any("missing" in p for p in check_rows([{"key": "I1-soic", "question": "", "answer": "", "watch": ""}], []))
