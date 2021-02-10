def factorial(n):
    import functools
    import operator
    return functools.reduce(operator.mul, [x for x in range(1, n+1)]) if n > 0 else 1