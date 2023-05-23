import copy


def main():

    inital_guess = "adieu"
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


if __name__ == "__main__":
    main()
