def longest_word(string_of_words):
    return sorted([s for s in string_of_words.split(' ')], key=len)[-1]


print(longest_word('one two three'))