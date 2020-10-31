from hashlib import sha1
from string import ascii_lowercase
from itertools import product


def password_cracker(hash):
    for num in range(6):
        for comb in product(ascii_lowercase, repeat=num):
            word = ''.join(comb)
            if sha1(word.encode()).hexdigest() == hash:
                return word
