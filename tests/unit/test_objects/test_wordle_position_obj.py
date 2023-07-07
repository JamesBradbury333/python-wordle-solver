import pytest
from src.main import WordlePosition


def test_assert_guessed_letter_correct_form():
    wordle_letter = WordlePosition(0)
    with pytest.raises(AssertionError):
        wordle_letter.assert_guessed_letter_correct_form("aa")
        wordle_letter.assert_guessed_letter_correct_form(2)
        wordle_letter.assert_guessed_letter_correct_form(";")
        wordle_letter.assert_guessed_letter_correct_form(3.1)
        wordle_letter.assert_guessed_letter_correct_form(["a"])
        wordle_letter.assert_guessed_letter_correct_form(("a"))
        wordle_letter.assert_guessed_letter_correct_form(True)
        wordle_letter.assert_guessed_letter_correct_form(False)


def test_this_position_guessed_correct():
    wordle_letter = WordlePosition(0)
    wordle_letter.is_not_letters.append("a")
    with pytest.raises(ValueError):
        wordle_letter.this_position_guessed_correct("a")


def test_add_letter_might_be():
    wordle_letter = WordlePosition(0)
    wordle_letter.is_not_letters.append("a")
    with pytest.raises(ValueError):
        wordle_letter.add_letter_might_be("a")


def test_letter_guess_not_in_this_position():
    wordle_letter1 = WordlePosition(0)
    wordle_letter1.might_be_letters.append("a")
    wordle_letter1.letter_guess_not_in_this_position("a")
    assert "a" not in wordle_letter1.might_be_letters

    wordle_letter2 = WordlePosition(0)
    wordle_letter2.true_letter = "a"
    with pytest.raises(ValueError):
        wordle_letter2.letter_guess_not_in_this_position("a")
