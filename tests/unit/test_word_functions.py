from pytest import approx

from src.main import (
    remove_words_if_in_char_list,
    alphabet_letters_list,
    rank_most_common_letters_in_word_list,
    score_remaining_words,
)


def test_remove_words_if_in_char_list():
    jedis = ["yoda", "obi-wan", "anakin", "luke"]
    assert remove_words_if_in_char_list(jedis, ["a"]) == ["luke"]

    words = ["abcde", "aaaaa", "defgh", "zzzzz"]
    assert remove_words_if_in_char_list(words, list("aaa")) == ["defgh", "zzzzz"]


def test_score_remaining_words():
    remaining_words_list = ["jedis", "cat", "z"]
    normalised_letter_score_dict = {
        "a": 2,
        "b": 0,
        "c": 2,
        "d": 1,
        "e": 1,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 1,
        "j": 1,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 1,
        "t": 2,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    assert score_remaining_words(
        remaining_words_list, normalised_letter_score_dict
    ) == {"jedis": 5, "cat": 6, "z": 0}


def test_rank_most_common_letters_in_word_list():
    word_list = ["aaa", "bb", "c"]
    assert rank_most_common_letters_in_word_list(word_list) == {
        "a": approx(100 * 3 / 6),  # 50% letters are a
        "b": approx(100 * 2 / 6),  # 33.3% letters are b
        "c": approx(100 * 1 / 6),  # 16.7% letters are c
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
