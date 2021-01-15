from itertools import combinations
from functools import reduce
import operator


# brute force
def product_sum_brute(a, m):
    counter = 0
    for comb in combinations(a, m):
        counter += reduce(operator.mul, comb)
    return counter


def product_sum(a, m):
    pass