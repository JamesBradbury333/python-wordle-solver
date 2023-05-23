from src.main import remove_words_if_in_char_list
from src.main import alphabet_letters_list
from src.main import rank_most_common_letters_in_word_list


def test_remove_words_if_in_char_list():
    jedis = ["yoda", "obi-wan", "anakin", "luke"]
    assert remove_words_if_in_char_list(jedis, ["a"]) == ["luke"]


def test_rank_most_common_letters_in_word_list():
    word_list = ["aaa", "bb", "c"]
    assert rank_most_common_letters_in_word_list(word_list) == {
        "a": 3,
        "b": 2,
        "c": 1,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }


def test_alphabet_letters_list():
    assert alphabet_letters_list() == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
