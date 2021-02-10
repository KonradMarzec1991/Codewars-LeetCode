def count(n):
    from math import log10, floor, e, pi
    if n == 1:
        return 1
    return floor(n * log10(n / e) + log10(2 * pi * n)/ 2.0) + 1