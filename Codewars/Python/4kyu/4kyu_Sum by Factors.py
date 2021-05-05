from collections import defaultdict


def sum_for_list(lst):
    d = defaultdict(lambda: 0)
    for item in lst:
        primes = find_prime_divisors(item)
        for prime in primes:
            d[prime] += item
    output = []
    for k in sorted(d):
        output.append([k, d[k]])
    return output


def find_prime_divisors(n):
    temp = set()
    n = abs(n)
    sq_root = int(n ** .5) + 1

    while n % 2 == 0:
        n //= 2
        temp.add(2)
    for i in range(3, sq_root, 2):
        while n % i == 0:
            n //= i
            temp.add(i)
    if n > 1:
        temp.add(n)
    return temp
