import copy
from collections import namedtuple


def main():

    inital_guess = "adieu"
    possible_letters = alphabet_letters_list()

    wordle = "boats"


    with open("5-letter-words.txt") as file:
        possible_words = file.read().split("\n")

    # make an inital guess
    guess_letter = "a"

    if guess_letter not in wordle:
        possible_letters.remove(guess_letter)
    

    reduced_words = remove_words_if_in_char_list(possible_words, list(inital_guess))
    most_common_letters_list, letter_count_dict = rank_most_common_letters_in_word_list(reduced_words)

    pick_a_guess_word(most_common_letters_list, letter_count_dict, reduced_words)



    return


def pick_a_guess_word(most_common_letters_list, letter_count_dict, reduced_words):
    most_common_letters = most_common_letters_list[:6]
    possible_words = copy.deepcopy(reduced_words)
    for word in reduced_words:
        for letter in most_common_letters_list:
            if letter not in list(word):
                possible_words.remove(word)
                break

    print(possible_words)


def remove_words_if_in_char_list(word_list, char_list):
    copy_word_list = copy.deepcopy(word_list)

    for word in word_list:
        for char in char_list:
            if char in list(word):
                copy_word_list.remove(word)
                break
    return copy_word_list


def rank_most_common_letters_in_word_list(word_list):
    letters_dict = dict.fromkeys(alphabet_letters_list(), 0)
    for word in word_list:
        for letter in list(word):
            letters_dict[letter] += 1
    
    most_common_letters_list = sorted(letters_dict, key=letters_dict.get ,reverse=True)
    return most_common_letters_list, letters_dict


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
