def gen(n, iterable):
    from itertools import cycle
    it = cycle(iterable)
    result = tuple(next(it) for _ in range(n))
    while True:
        yield result
        result = result[1:] + (next(it), )
