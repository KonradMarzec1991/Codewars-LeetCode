from itertools import product
from functools import reduce
import operator


def get_divisors(num):
    if num == 1:
        return [1]
    if num == 2:
        return [1, 2]
    res = []
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            if num / i == i:
                res.append(i)
            else:
                res.append(i)
                res.append(num/i)
    return sorted(map(int, res))


# This code works, but it is too slow
def multiply(n, k):
    if k == 1:
        return 1
    p = set()
    divs = get_divisors(n)
    for i in product(divs, repeat=k):
        if reduce(operator.mul, i) == n:
            p.add(i)
    return len(p)

