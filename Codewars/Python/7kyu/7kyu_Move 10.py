from string import ascii_lowercase


def move_ten(st):
    alphabet = ascii_lowercase + 'abcdefghij'
    return ''.join([alphabet[alphabet.index(ch) + 10] for ch in st])
