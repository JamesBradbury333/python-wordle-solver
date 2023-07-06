import pytest
from src.main import GuessLetterPosition


def test_guess_letter_position_show_basic_functionality():
    letter_idx = 0
    guess_letter = "a"
    letter_is_correct = True
    letter_in_wordle = True
    first_guess = GuessLetterPosition(
        letter_idx, guess_letter, letter_is_correct, letter_in_wordle
    )

    assert first_guess.letter_idx == 0
    assert first_guess.guess_letter == "a"
    assert first_guess.letter_is_correct is True
    assert first_guess.letter_in_wordle is True


@pytest.mark.parametrize("bad_letter_idx", [-1, -2, 5, 6, 7, 8, 9, 0.5, -1.5, 2.2, 3.6])
def test_guess_letter_position_raises_errors(bad_letter_idx):
    guess_letter = "a"
    letter_is_correct = True
    letter_in_wordle = True
    with pytest.raises(ValueError):
        GuessLetterPosition(
            bad_letter_idx, guess_letter, letter_is_correct, letter_in_wordle
        )


@pytest.mark.parametrize("bad_guess_letter", ["A", "B", 1, 3.2, "HELLO", "%", "@"])
def test_guess_letter(bad_guess_letter):
    letter_idx = 0
    letter_is_correct = True
    letter_in_wordle = True
    with pytest.raises(ValueError):
        GuessLetterPosition(
            letter_idx, bad_guess_letter, letter_in_wordle, letter_is_correct
        )


def test_guess_letter_true_false_conditions():
    letter_idx = 0
    guess_letter = "a"

    letter_is_correct_1 = True
    letter_in_wordle_1 = True

    letter_is_correct_2 = False
    letter_in_wordle_2 = True

    letter_is_correct_3 = True
    letter_in_wordle_3 = False

    letter_is_correct_4 = False
    letter_in_wordle_4 = False

    GuessLetterPosition(
        letter_idx, guess_letter, letter_is_correct_1, letter_in_wordle_1
    )
    GuessLetterPosition(
        letter_idx, guess_letter, letter_is_correct_2, letter_in_wordle_2
    )
    with pytest.raises(ValueError):
        GuessLetterPosition(
            letter_idx, guess_letter, letter_is_correct_3, letter_in_wordle_3
        )
    GuessLetterPosition(
        letter_idx, guess_letter, letter_is_correct_4, letter_in_wordle_4
    )
