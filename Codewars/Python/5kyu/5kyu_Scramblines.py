def scramble(s1, s2):
    return all(x is False for x in [s1.count(c) < s2.count(c) for c in set(s2)])