from functools import reduce
import operator


def summy(string_of_ints):
    return reduce(operator.add, map(int, string_of_ints.split()))
