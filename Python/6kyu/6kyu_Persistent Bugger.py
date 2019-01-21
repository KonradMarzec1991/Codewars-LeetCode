import numpy as np


def persistence(n):

    if not isinstance(n, int):
        return 'Not a number!'

    if len(str(n)) == 1:
        return 0

    counter = 0

    while len(str(n)) > 1:
        x = [int(i) for i in str(n)]
        n = np.product(x)
        counter += 1

    return counter