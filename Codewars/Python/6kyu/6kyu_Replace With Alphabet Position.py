def alphabet_position(text):
    import string
    import itertools
    text = "".join(x for x in text if x.isalpha()).lower()
    alphabet = dict(zip(string.ascii_lowercase,
                        itertools.count(start=0, step=1)))
    my_list = []

    for letter in text:
        my_list.append(alphabet[letter] + 1)

    return " ".join(str(num) for num in my_list)
