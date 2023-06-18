import copy


def main():

    inital_guess = "adieu"
    possible_letters = alphabet_letters_list()

    wordle = "flyby"

    with open("../5-letter-words.txt") as file:
        possible_words = file.read().split("\n")

    reduced_words = remove_words_if_in_char_list(possible_words, list(inital_guess))
    normalised_letter_score_dict = rank_most_common_letters_in_word_list(reduced_words)
    remaining_word_scores = score_remaining_words(
        reduced_words, normalised_letter_score_dict
    )
    # TODO: In 2 picks we remove all possible words from word pool. Algo needs to decide 
    # What to do if letter in wordle
    new_word = max(remaining_word_scores, key=remaining_word_scores.get)
    print(new_word)
    print(len(reduced_words))
    reduced_words = remove_words_if_in_char_list(reduced_words, list(new_word))
    print(reduced_words)

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
        if number_of_letters_in_wordle > 0 and number_of_letters_in_wordle < 10:
            raise ValueError(
                f"A wordle can only be 5 letters long,"
                f"not {number_of_letters_in_wordle} letters long."
            )
        self.wordle_letters = []
        for i in range(0, number_of_letters_in_wordle):
            self.wordle_letters.append(WordlePosition(i))


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


if __name__ == "__main__":
    main()
