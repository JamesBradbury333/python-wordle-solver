from src.main import remove_words_if_in_char_list


def test_remove_words_if_in_char_list():
    jedis = ["yoda", "obi-wan", "anakin", "luke"]
    assert remove_words_if_in_char_list(jedis, ["a"]) == ["luke"]
