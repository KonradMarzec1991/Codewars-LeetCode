from collections import defaultdict


def count(string):
    d = defaultdict(lambda: 0)
    for s in string:
        d[s] += 1
    return d if string else {}