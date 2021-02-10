def nb_year(p0, percent, aug, p):
    percent = percent/100
    counter = 0
    while p > p0:
        p0 = p0*(1 + percent) + aug
        counter += 1
    return counter
