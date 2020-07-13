def nb_dig(n, d):
    return sum(str(num * num).count(str(d)) for num in range(n+1))
