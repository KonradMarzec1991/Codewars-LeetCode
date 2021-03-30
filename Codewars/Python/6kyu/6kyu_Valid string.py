def valid_word(seq, word):
    seq = sorted(seq, reverse=True)
    for s in seq:
        if s in word:
            word = word.replace(s, '')
    return len(word) == 0