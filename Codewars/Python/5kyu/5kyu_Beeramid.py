def beeramid(bonus, price):
    if bonus < 0:
        return 0
    beers = bonus//price
    qs = lambda n: n*(n+1)*(2*n+1)/6
    i = 1
    while beers >= qs(i):
        i += 1
    return i - 1


