import copy
from collections import namedtuple


def main():

    inital_guess = "adieu"
    possible_letters = alphabet_letters_list()


    with open("5-letter-words.txt") as file:
        possible_words = file.read().split("\n")

    reduced_words = remove_words_if_in_char_list(possible_words, list(inital_guess))
    most_common_letters = rank_most_common_letters_in_word_list(reduced_words)
    

    return


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

    return letters_dict


def alphabet_letters_list():
    return list(map(chr, range(97, 123)))


class WordleWord:
    
    def __init__(self):
        self.position_0 = self.alphabet_letters_dict()
        self.position_1 = self.alphabet_letters_dict()
        self.position_2 = self.alphabet_letters_dict()
        self.position_3 = self.alphabet_letters_dict()
        self.position_4 = self.alphabet_letters_dict()

        self.letters_in_word = []

    def alphabet_letters_list(self):
        return list(map(chr, range(97, 123)))
    
    def alphabet_letters_dict(self):
        return dict.fromkeys(self.alphabet_letters_list(), "maybe")
    
    def update_positions(self, LetterGuess):
        if LetterGuess.position == 0:
            if LetterGuess.correct_position:
                self.position_0[LetterGuess.letter] = True
            else:
                self.position_0[LetterGuess.letter] = False
                if LetterGuess.in_word:
                    self.letters_in_word.append(LetterGuess.letter)


class LetterGuess:
    def __init__(self, letter: str, position: int ,correct_position: bool, in_word: bool):
        self.letter = letter
        self.positon = position
        self.correct_posiiton = correct_position
        self.in_word = in_word


        

if __name__ == "__main__":
    main()
