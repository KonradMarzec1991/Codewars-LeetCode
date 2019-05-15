import functools
from fractions import gcd


def lcm(*args):
    l = [x for x in args]
    return functools.reduce(lambda x, y: x*y/gcd(x, y), l)


