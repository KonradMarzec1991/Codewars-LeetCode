def lcm(*args):
    import functools
    from fractions import gcd
    l = [x for x in args]
    return functools.reduce(lambda x, y: x*y/gcd(x, y), l)


