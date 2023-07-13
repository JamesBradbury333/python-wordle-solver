import pytest
from src.main import WordleWord, GuessedWord, GuessLetterPosition


def test_5_letters_in_wordle():
    with pytest.raises(ValueError):
        WordleWord(0)
        WordleWord(1)
        WordleWord(4)
        WordleWord(6)
        WordleWord(-1)
        WordleWord("a")
        WordleWord([5])
        WordleWord((2))


def test_guess_a_word():
    word_to_guess = "apart"
    first_guessed_word = "after"
    wordle = WordleWord(5)
    first_guess = GuessedWord(  # guessed word is "after"
        GuessLetterPosition(0, "a", True, True),
        GuessLetterPosition(1, "f", False, False),
        GuessLetterPosition(2, "t", False, True),
        GuessLetterPosition(3, "e", False, False),
        GuessLetterPosition(4, "r", False, True),
    )
    wordle.guess_a_word(first_guess)
    first_letter = wordle.wordle_letters[0]
    second_letter = wordle.wordle_letters[1]
    third_letter = wordle.wordle_letters[2]
    fourth_letter = wordle.wordle_letters[3]
    fifth_letter = wordle.wordle_letters[4]

    assert first_letter.true_letter == "a"
    assert second_letter.true_letter is None
    assert third_letter.true_letter is None
    assert fourth_letter.true_letter is None
    assert fifth_letter.true_letter is None

    assert first_letter.might_be_letters == ["t", "r"]
    assert second_letter.might_be_letters == ["a", "t", "r"]
    assert third_letter.might_be_letters == ["a", "r"]
    assert fourth_letter.might_be_letters == ["a", "t", "r"]
    assert fifth_letter.might_be_letters == ["a", "t"]

    assert first_letter.is_not_letters == ["f", "e"]
    assert second_letter.is_not_letters == ["f", "e"]
    assert third_letter.is_not_letters == ["f", "t", "e"]
    assert fourth_letter.is_not_letters == ["f", "e"]
    assert fifth_letter.is_not_letters == ["f", "e", "r"]

    # # Second guess letter
    second_guessed_word = "agape"
    # word_to_guess = "apart"
    second_guess = GuessedWord(
        GuessLetterPosition(0, "a", True, True),
        GuessLetterPosition(1, "g", False, False),
        GuessLetterPosition(2, "a", True, True),
        GuessLetterPosition(3, "p", False, True),
        GuessLetterPosition(4, "e", False, False),
    )
    wordle.guess_a_word(second_guess)

    assert first_letter.true_letter == "a"
    assert second_letter.true_letter is None
    assert third_letter.true_letter == "a"
    assert fourth_letter.true_letter is None
    assert fifth_letter.true_letter is None

    assert first_letter.might_be_letters == ["t", "r", "a", "p"]
    assert second_letter.might_be_letters == ["a", "t", "r", "p"]
    assert third_letter.might_be_letters == ["a", "r", "p"]
    assert fourth_letter.might_be_letters == ["a", "t", "r"]
    assert fifth_letter.might_be_letters == ["a", "t", "p"]

    assert first_letter.is_not_letters == ["f", "e", "g"]
    assert second_letter.is_not_letters == ["f", "e", "g"]
    assert third_letter.is_not_letters == ["f", "t", "e", "g"]
    assert fourth_letter.is_not_letters == ["f", "e", "g", "p"]
    assert fifth_letter.is_not_letters == ["f", "e", "r", "g"]


def test_true_letter_cannot_be_in_in_is_not_letters():
    wordle = WordleWord(5)
    wordle_first_letter = wordle.wordle_letters[0]
    wordle_first_letter.is_not_letters.append("a")

    guess = GuessedWord(
        GuessLetterPosition(0, "a", True, True),
        GuessLetterPosition(1, "a", True, True),
        GuessLetterPosition(2, "a", True, True),
        GuessLetterPosition(3, "a", True, True),
        GuessLetterPosition(4, "a", True, True),
    )
    # Check logic works in top level method
    with pytest.raises(ValueError):
        wordle.guess_a_word(guess)
    # Check logic works at lower level method
    with pytest.raises(ValueError):
        wordle.set_true_letter_for_guess_wordle_position("a", wordle_first_letter)


# TODO: May decide to purge might be and can't be letters once true letter is assigned
def test_is_not_letters_cant_same_as_be_true_letter():
    wordle = WordleWord(5)
    wordle_first_letter = wordle.wordle_letters[0]
    wordle_first_letter.true_letter = "a"

    with pytest.raises(ValueError):
        wordle.add_letter_to_all_is_not_lists("a")


# TODO: Need a test to check that a letter cant be added to might_be list if it is part of the is_not list
def test_not_in_might_be_and_is_not_list():
    wordle = WordleWord(5)
    wordle_first_letter = wordle.wordle_letters[0]
    wordle_second_letter = wordle.wordle_letters[1]
    wordle_first_letter.is_not_letters.append("a")

    wordle.add_guess_letter_to_is_not_list_for_other_wordle_positions(
        "a", wordle_second_letter
    )
    assert "a" not in wordle_first_letter.might_be_letters


def test_is_not_letter_removed_from_might_be_list():
    wordle = WordleWord(5)
    wordle_first_letter = wordle.wordle_letters[0]
    wordle_first_letter.might_be_letters.append("a")
    assert "a" in wordle_first_letter.might_be_letters

    wordle.add_letter_to_all_is_not_lists("a")
    assert "a" not in wordle_first_letter.might_be_letters

    wordle_first_letter.might_be_letters.append("a")
    assert "a" in wordle_first_letter.might_be_letters
    wordle.add_guess_letter_to_is_not_list_for_other_wordle_positions(
        "a", wordle.wordle_letters[3]
    )
    assert "a" not in wordle_first_letter.might_be_letters
