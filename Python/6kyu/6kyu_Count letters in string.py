def letter_count(s):
    s = ''.join(sorted(s))
    letters = dict()
    for ch in s:
        if ch not in letters:
            letters[ch] = 1
        else:
            letters[ch] += 1
    return letters
