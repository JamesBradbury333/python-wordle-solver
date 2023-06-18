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
    def __init__(self):
        self.position_0 = self.alphabet_letters_dict()
        self.position_1 = self.alphabet_letters_dict()
        # self.position_2 = self.alphabet_letters_dict()
        # self.position_3 = self.alphabet_letters_dict()
        # self.position_4 = self.alphabet_letters_dict()
        self.letters_in_word = set()
        self.letters_not_in_word = set()
        self.possible_letters = self.alphabet_letters_list()

    def alphabet_letters_list(self):
        return list(map(chr, range(97, 123)))

    def alphabet_letters_dict(self):
        return dict.fromkeys(self.alphabet_letters_list(), "maybe")

    def guess_a_letter(self, letter: str, in_word: bool, in_correct_position: bool):
        if in_correct_position:
            self.position_0[letter] = True
            self.letters_in_word.add(letter)
        if in_word:
            self.position_0[letter] = False
            self.letters_in_word.add(letter)
        else:
            self.letters_in_word.add(letter)


if __name__ == "__main__":
    main()
