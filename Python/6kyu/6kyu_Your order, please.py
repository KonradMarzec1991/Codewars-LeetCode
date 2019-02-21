def order(sentence):

    if len(sentence) == 0:
        return ""

    words = {}
    my_sentence_split = ("" + sentence).split()

    for word in my_sentence_split:
        for item in word:
            if item.isdigit():
                words[int(item)] = word

    final_list = [words[key] for key in sorted(words.keys())]
    return " ".join(final_list)
