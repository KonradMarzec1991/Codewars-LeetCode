from collections import Counter


def common(a, b, c):
    return sum(list((Counter(a) & Counter(b) & Counter(c)).elements()))
