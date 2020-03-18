def nth_fib(n):
    i, k, l = 1, 0, 1
    while i < n:
        k, l = l, k + l
        i += 1
    return k