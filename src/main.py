import copy


def main():

    inital_guess = "adieu"
    with open("../5-letter-words.txt") as file:
        possible_words = file.read().split("\n")

    print(len(possible_words))

    # for word in possible_words:
    #     for char in inital_guess:
    #         if char not in word:
    #             possible_words.remove(word)

    # print(len(possible_words))
    test_list = ["adieu", "cat", "dog", "zzz"]
    copy_list = copy.deepcopy(possible_words)

    for word in possible_words:
        for char in inital_guess:
            if char in list(word):
                copy_list.remove(word)
                break
    print(len(copy_list))

    return


if __name__ == "__main__":
    main()


def remove_words_if_in_char_list(word_list, char_list):
    copy_word_list = copy.deepcopy(word_list)

    for word in word_list:
        for char in char_list:
            if char in list(word):
                copy_word_list.remove(word)
                break

    return copy_word_list
