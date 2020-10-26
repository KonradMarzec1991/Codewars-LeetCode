def reverse(n):
    from math import log10
    if n < 10:
        return n
    return n % 10 * 10 ** int(log10(n)) + reverse(n // 10)