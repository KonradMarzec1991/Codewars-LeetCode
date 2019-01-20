def nb_year(p0, percent, aug, p):

    percent = percent/100
    counter = 0

    while p > p0:
        p0 = p0*(1 + percent) + aug
        counter += 1

    return counter


print(nb_year(1500, 5, 100, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))
print(nb_year(1500000, 0.25, 1000, 2000000))