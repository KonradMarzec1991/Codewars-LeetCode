def anagrams(word, words):

    my_anagrams = []
    for my_word in words:
        if check_if_anagram(word, my_word):
            my_anagrams.append(my_word)

    return my_anagrams


def check_if_anagram(word1, word2):

    word1_list = list(word1)
    word2_list = list(word2)

    word1_list.sort()
    word2_list.sort()

    return word1_list == word2_list
