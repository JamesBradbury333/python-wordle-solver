import copy

FIRST_GUESS = "adieu"
SECRET_WORDLE_WORD = "flyby"


def main():
    wordle_word = WordleWord(5)

    with open("../5-letter-words.txt") as file:
        possible_words = file.read().split("\n")
    # possible_words = possible_words.sort()
    possible_words.sort()
    print(possible_words)

    first_guess = FIRST_GUESS


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

    def guess_a_word(self, guessed_word):
        for i, wordle_position in enumerate(self.wordle_letters):
            guess_position = guessed_word.guess_word_positions[i]
            guess_letter = guess_position.guess_letter

            if guess_position.letter_is_correct == True:
                self.set_true_letter_for_guess_wordle_position(
                    guess_letter, wordle_position
                )

            if (
                guess_position.letter_is_correct is False
                and guess_position.letter_in_wordle is True
            ):
                self.add_guess_letter_to_other_wordle_positions_might_be_list(
                    guess_letter, wordle_position, self.wordle_letters
                )

            if (
                guess_position.letter_is_correct is False
                and guess_position.letter_in_wordle is False
            ):
                self.add_letter_to_is_not_list(guess_letter)

    def set_true_letter_for_guess_wordle_position(self, true_letter, wordle_position):
        wordle_position.true_letter = true_letter

    def add_guess_letter_to_other_wordle_positions_might_be_list(
        self, guess_letter, this_wordle_position, all_wordle_positions
    ):
        this_wordle_position.is_not_letters.append(guess_letter)
        for wordle_position in all_wordle_positions:
            if (
                wordle_position.unique_position_id
                == this_wordle_position.unique_position_id
            ):
                pass
            else:
                wordle_position.might_be_letters.append(guess_letter)

    def add_letter_to_is_not_list(self, is_not_letter: str):
        for position in self.wordle_letters:
            position.is_not_letters.append(is_not_letter)


class WordlePosition:
    """Represents an index of a letter in the wordle word"""

    def __init__(self, unique_position_id: int):
        self.unique_position_id = unique_position_id
        self.true_letter = None
        self.might_be_letters = []
        self.is_not_letters = []

    def assert_guessed_letter_correct_form(self, guessed_letter):
        assert isinstance(guessed_letter, str)
        assert len(guessed_letter) == 1
        assert guessed_letter in list(map(chr, range(97, 123)))

    def this_position_guessed_correct(self, guessed_letter: str):
        self.assert_guessed_letter_correct_form(guessed_letter)
        if guessed_letter in self.is_not_letters:
            raise ValueError(
                "The correct letter cannot be in the list of is_not_letters."
            )
        self.true_letter = guessed_letter
        # TODO: Potentially later remove all letters from might_be_letters and add all others to _is_not_lettters
        # This may help improve deciding on next set of letters to pick? For debugging purposes it may be useful
        # to see the state up to the point that the correct letter was guessed?

    def add_letter_might_be(self, guessed_letter: str):
        self.assert_guessed_letter_correct_form(guessed_letter)
        if guessed_letter in self.is_not_letters:
            raise ValueError("A maybe letter cannot be in the list of is_not_letters.")
        self.might_be_letters.append(guessed_letter)

    def letter_guess_not_in_this_position(self, guessed_letter: str):
        self.assert_guessed_letter_correct_form(guessed_letter)
        if guessed_letter == self.true_letter:
            raise ValueError(
                "Letter cannont be in list of not letters as it has been assigned to true letter for this idx"
            )
        self.is_not_letters.append(guessed_letter)
        if guessed_letter in self.might_be_letters:
            self.might_be_letters.remove(guessed_letter)


class GuessedWord:
    def __init__(
        self,
        guess_letter_0,
        guess_letter_1,
        guess_letter_2,
        guess_letter_3,
        guess_letter_4,
    ):
        self.guess_word_positions = [
            guess_letter_0,
            guess_letter_1,
            guess_letter_2,
            guess_letter_3,
            guess_letter_4,
        ]


class GuessLetterPosition:
    def __init__(
        self,
        letter_idx: int,
        guess_letter: str,
        letter_is_correct: bool,
        letter_in_wordle: bool,
    ):
        if not isinstance(letter_idx, int):
            raise ValueError("letter_id must be an integer")
        if letter_idx < 0 or letter_idx > 4:
            raise ValueError("Guess letter index must be between 0 and 4")
        if not isinstance(guess_letter, str):
            raise ValueError("guess letter must be a string")
        if len(guess_letter) > 1:
            raise ValueError("letter must be a single lowercase letter")
        if guess_letter not in list(map(chr, range(97, 123))):
            raise ValueError("The guessed letter must be a lowercase letter a-z")
        if letter_is_correct and not letter_in_wordle:
            raise ValueError("If letter is correct it must be in wordle")

        self.letter_idx = letter_idx
        self.guess_letter = guess_letter
        self.letter_is_correct = letter_is_correct
        self.letter_in_wordle = letter_in_wordle


if __name__ == "__main__":
    main()
