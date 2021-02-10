def sum_divisors(num):
    if num == 1:
        return 1
    if num == 2:
        return 3
    s = 0
    for i in range(1, int(num ** .5)+1):
        if num % i == 0:
            if num // i == i:
                s += i
            else:
                s += i
                s += num / i
    return int(s)


def base():
    from collections import defaultdict
    from fractions import Fraction
    d = defaultdict(list)
    for i in range(1, 2001):
        d[Fraction(sum_divisors(i), i)].append(i)
    return [v for k, v in d.items() if len(v) > 1]


def solve(a, b):
    pairs = [[t for t in pair if a <= t < b] for pair in base()]
    return sum([pair[0] for pair in pairs if len(pair) > 1])


