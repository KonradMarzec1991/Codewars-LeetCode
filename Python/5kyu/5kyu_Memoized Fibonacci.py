fibonnachi_cache = {1: 1, 2: 1, 3: 2}


def fibonacci(n):
    if n in fibonnachi_cache:
        return fibonnachi_cache[n]
    value_n = fibonacci(n - 1) + fibonacci(n - 2)
    fibonnachi_cache[n] = value_n
    return value_n
