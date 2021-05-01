def prime(n):
    if n <= 1:
        return []
    primes = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p] is True:
            for i in range(p * 2, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False
    return [x for x, y in zip(range(n+1), primes) if y]
