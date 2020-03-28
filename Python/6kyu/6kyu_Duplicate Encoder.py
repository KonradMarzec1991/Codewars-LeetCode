def duplicate_encode(word):
    return ''.join(['(' if word.lower().count(w) == 1 else ')' for w in word.lower()])