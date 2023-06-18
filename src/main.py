import copy
from collections import namedtuple

FIRST_GUESS = "adieu"


def main():
    possible_letters = alphabet_letters_list()

    secret_wordle_word = "flyby"

    wordle_word = WordleWord(5)

    with open("../5-letter-words.txt") as file:
        possible_words = file.read().split("\n")

    first_guess = FIRST_GUESS

    return


# TODO: test this func
def score_remaining_words(remainig_words_list, normalised_letter_score_dict):
    word_score_dict = dict.fromkeys(remainig_words_list, 0)
    for word in word_score_dict:
        letters_parsed_so_far = []
        for letter in list(word):
            if letter not in letters_parsed_so_far:
                word_score_dict[word] += normalised_letter_score_dict[letter]
            else:
                word_score_dict[word] += (
                    normalised_letter_score_dict[letter] * 0.2
                )  # TODO: Decide how to weight letter repeats, placeholder 0.2 for now?
            letters_parsed_so_far.append(letter)
    # print(word_score_dict)
    return word_score_dict


# TODO: Re-write tests for this
def remove_words_if_in_char_list(word_list, char_list):
    copy_word_list = copy.deepcopy(word_list)

    for word in word_list:
        print(word)
        for char in char_list:
            if char in list(word):
                copy_word_list.remove(word)
                break
    return copy_word_list


# TODO: test this func
def rank_most_common_letters_in_word_list(word_list):
    """Returns a dict with normalised scores for each letter in remaining word dict.
    Higer occurrance of a letter grants a higher score."""
    letters_dict = dict.fromkeys(alphabet_letters_list(), 0)
    total_score_counter = 0
    for word in word_list:
        for letter in list(word):
            letters_dict[letter] += 1
            total_score_counter += 1
    normailsed_letter_score_dict = copy.deepcopy(letters_dict)
    for key in normailsed_letter_score_dict:
        normailsed_letter_score_dict[key] = (
            letters_dict[key] / total_score_counter
        ) * 100
    return normailsed_letter_score_dict


def alphabet_letters_list():
    return list(map(chr, range(97, 123)))


class WordleWord:
    """The Wordle Word, made up of indexes recording what a letter is/isn't/could be."""

    def __init__(self, number_of_letters_in_wordle: int):
        if number_of_letters_in_wordle != 5:
            raise ValueError(
                f"A wordle can only be 5 letters long,"
                f"not {number_of_letters_in_wordle} letters long."
            )
        self.wordle_letters = []
        for i in range(0, number_of_letters_in_wordle):
            self.wordle_letters.append(WordlePosition(i))

    # TODO: Method for updating wordle following a guess

    # TODO: Method for updating remaining words following a guess


class WordlePosition:
    """Represents an index of a letter in the wordle word"""

    def __init__(self, unique_position_id: int):
        self.unique_position_id = unique_position_id
        self.true_letter = None
        self.could_be_letters = []
        self.is_not_letters = []

    def this_position_guessed_correct(self, guessed_letter: str):
        self.true_letter = guessed_letter

    def add_letter_might_be(self, guessed_letter: str):
        self.could_be_letters.append(guessed_letter)

    def letter_guess_not_in_this_position(self, guessed_letter: str):
        self.is_not_letters.append(guessed_letter)
        if guessed_letter in self.could_be_letters:
            self.could_be_letters.remove(guessed_letter)


class WordleGuessedWord:
    """Records the details of a guessed word"""

    def __init__(self, guessed_word):
        wordle_guess_letters = []
        if len(guessed_word) != 5:
            raise ValueError("Guessed word can only be 5 chars long")
        guessed_word = list(guessed_word)
        for i, char in enumerate(guessed_word):
            letter_in_correct_pos = char == FIRST_GUESS[i]
            letter_in_wordle = char in guessed_word
            wordle_guess_letters.append(
                WordleGuessedWordPosition(
                    i, char, letter_in_correct_pos, letter_in_wordle
                )
            )


class WordleGuessedWordPosition:
    """Records the details of a letter in a guessed word"""

    def __init__(
        self,
        unique_position_id: int,
        letter_guessed: str,
        letter_in_correct_pos: bool,
        letter_in_wordle: bool,
    ):
        if letter_in_correct_pos and not letter_in_wordle:
            raise AssertionError(
                "If a letter is in the correct place it must also be in the wordle"
            )
        self.unique_position_id = unique_position_id
        self.letter_guessed = letter_guessed
        self.letter_in_correct_pos = letter_in_correct_pos
        self.letter_in_wordle = letter_in_wordle


if __name__ == "__main__":
    main()
