from collections import defaultdict


def make_change(amount):
    coins = (50, 25, 10, 5, 1)
    symbols = ('H', 'Q', 'D', 'N', 'P')

    combs = defaultdict(lambda: 0)
    index = 0
    curr = coins[index]
    while amount > 0:
        while amount >= curr:
            amount -= curr
            combs[symbols[index]] += 1
        index += 1
        if index >= len(coins):
            break
        curr = coins[index]
    return combs


# Great CW solution of FArekkusu
BASE = {"H": 50, "Q": 25, "D": 10, "N": 5, "P": 1}


def make_change2(n):
    r = {}
    for x, y in BASE.items():
        if n >= y:
            r[x], n = divmod(n, y)
    return r
