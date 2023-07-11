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
    # after
    wordle = WordleWord(5)
    guess = GuessedWord(
        GuessLetterPosition(0, "a", True, True),
        GuessLetterPosition(1, "f", False, False),
        GuessLetterPosition(2, "t", False, True),
        GuessLetterPosition(3, "e", False, False),
        GuessLetterPosition(4, "r", False, True),
    )
    wordle.guess_a_word(guess)
    first_letter = wordle.wordle_letters[0]
    second_letter = wordle.wordle_letters[1]
    third_letter = wordle.wordle_letters[2]
    fourth_letter = wordle.wordle_letters[3]
    fifth_letter = wordle.wordle_letters[4]

    assert first_letter.true_letter == "a"
    assert second_letter.true_letter == None
    assert third_letter.true_letter == None
    assert fourth_letter.true_letter == None
    assert fifth_letter.true_letter == None

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
