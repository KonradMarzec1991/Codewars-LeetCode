import math
import itertools


def find_divisors(n):

    if n == 1:
        return [1]

    d = [1]
    threshold = int(math.sqrt(n))
    for i in range(2, threshold + 1):
        if n % i == 0:
            d.append(i)
            d.append(int(n/i))

    if math.sqrt(n) == threshold:
        d.append(threshold)
    d.append(n)

    return sorted(d)


def list_squared(m, n):

    my_list = []

    for i in range(m, n + 1):
        l = find_divisors(i)
        s_pow = sum(list(map(pow, l, itertools.repeat(2))))
        if math.sqrt(s_pow) == int(math.sqrt(s_pow)):
            my_list.append([i, s_pow])

    return my_list
