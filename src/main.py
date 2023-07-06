import copy

FIRST_GUESS = "adieu"
SECRET_WORDLE_WORD = "flyby"


def main():
    wordle_word = WordleWord(5)

    with open("../5-letter-words.txt") as file:
        possible_words = file.read().split("\n")

    first_guess = FIRST_GUESS
    first_guess = GuessResults()

    wordle = WordleWord(5)
    wordle.guess_a_word(first_guess)

    print("Unique Pos ID:")
    for j, wordle_pos in enumerate(wordle.wordle_letters):
        print(wordle.wordle_letters[j].unique_position_id)

    print("True Letters:")
    for j, wordle_pos in enumerate(wordle.wordle_letters):
        print(wordle.wordle_letters[j].true_letter)

    print("could_be_letters:")
    for j, wordle_pos in enumerate(wordle.wordle_letters):
        print(wordle.wordle_letters[j].could_be_letters)

    print("is_not_letters:")
    for j, wordle_pos in enumerate(wordle.wordle_letters):
        print(wordle.wordle_letters[j].is_not_letters)

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

    def guess_a_word(self, guessed_word):
        for i, wordle_position in enumerate(self.wordle_letters):
            if guessed_word.guess_letters[i].letter_is_correct == True:
                wordle_position.true_letter = guessed_word.guess_letters[i].guess_letter

            elif guessed_word.guess_letters[i].letter_in_wordle == True:
                wordle_position.is_not_letters = guessed_word.guess_letters[
                    i
                ].guess_letter
                for pos in self.wordle_letters:
                    if pos.unique_position_id != wordle_position.unique_position_id:
                        wordle_position.could_be_letters.append(
                            guessed_word.guess_letters[i].guess_letter
                        )

            else:
                for pos in self.wordle_letters:
                    pos.is_not_letters.append(
                        guessed_word.guess_letters[i].guess_letter
                    )


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


class GuessResults:
    def __init__(self):
        self.guess_letters = []
        for i in range(5):
            letter_idx = i
            guess_letter = input(f"Letter idx {letter_idx} is:")
            letter_is_correct = input(
                "Letter is in the correct position (True or False):"
            )
            if letter_is_correct == "True":
                letter_is_correct = True
            else:
                letter_is_correct = False
            if letter_is_correct:
                letter_in_wordle = True
            else:
                letter_in_wordle = input("Letter is in the wordle (True or False):")
                if letter_in_wordle == "True":
                    letter_in_wordle = True
                else:
                    letter_in_wordle = False

            self.guess_letters.append(
                GuessLetterPosition(
                    letter_idx, guess_letter, letter_is_correct, letter_in_wordle
                )
            )


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
