def solve(a, b):
    from math import gcd
    c = gcd(a, b)
    while c > 1:
        b //= c
        c = gcd(a, b)
    return b == 1
