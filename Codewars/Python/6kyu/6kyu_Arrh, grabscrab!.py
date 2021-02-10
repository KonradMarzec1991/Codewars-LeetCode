def grabscrab(word, possible_words):
    word, arr = ''.join(sorted(word)), []
    for possible in possible_words:
        ordered = ''.join(sorted(possible))
        if word == ordered:
            arr.append(possible)
    return arr
