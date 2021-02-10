def choose(n, k):
    from math import factorial
    if k > n:
        return 0
    return factorial(n)//(factorial(k)*factorial(n-k))