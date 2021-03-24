from string import ascii_lowercase

VOWELS = 'aeuio'
LETTERS = ascii_lowercase[-5:] + ascii_lowercase + ascii_lowercase[:9]


def vowel_back(st):
    new_st = ''
    for ch in st:
        idx = LETTERS.index(ch)
        if ch in 'co':
            new_idx = idx - 1
        elif ch == 'd':
            new_idx = idx - 3
        elif ch == 'e':
            new_idx = idx - 4
        elif ch in VOWELS:
            new_idx = idx - 5
        else:
            new_idx = idx + 9
        if LETTERS[new_idx] in 'code':
            new_idx = idx

        new_st += LETTERS[new_idx]
    return new_st


# Solution from CW
def vowel_back_v2(st):
    return st.translate(
        str.maketrans(
            "abcdefghijklmnopqrstuvwxyz",
            "vkbaafpqistuvwnyzabtpvfghi"
        )
    )
