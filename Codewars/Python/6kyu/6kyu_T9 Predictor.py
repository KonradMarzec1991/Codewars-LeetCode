import string

t9 = "22233344455566677778889999"


def letter_to_digit(x):
    assert 'a' <= x <= 'z'
    return t9[ord(x) - ord('a')]


def code_word(word):
    return ''.join(map(letter_to_digit, word))


def T9(words, seq):
    alphabet = string.ascii_lowercase
    matches = []
    for w in words:
        if code_word(w.lower()) == seq:
            matches.append(w)
    if not matches:
        letters = ''
        for ch in seq:
            letters += alphabet[t9.index(str(ch))]
        matches = [letters]
    return matches


# Other attempt - found on CW
FROM = "abc def ghi jkl mno pqrs tuv wxyz".split()
TO_NUM = "222 333 444 555 666 7777 888 9999".split()

TABLE_TO_NUM = str.maketrans(*map(''.join, (FROM, TO_NUM)) )
TABLE_TO_CHAR = str.maketrans(*map(lambda lst: ''.join(x[0] for x in lst), (TO_NUM, FROM)))


def T9_1(words, seq):
    return ([w for w in words if seq == w.lower().translate(TABLE_TO_NUM)] or [seq.translate(TABLE_TO_CHAR)])
