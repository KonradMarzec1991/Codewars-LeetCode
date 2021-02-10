# Recursive solution too slow
def squared_digits_series(n):
    from math import log2
    if n == 0:
        return 0
    pow = int(log2(n))
    return 10 * 2 ** pow + 1 + squared_digits_series(n-1)
