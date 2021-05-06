import numpy as np


def solve_eq(eq):
    arr = []
    for i, x in enumerate(eq):
        for j, y in enumerate(x):
            if j == len(x) - 1:
                arr.append(y)
                del x[-1]

    a = np.array(eq)
    b = np.array(arr)
    return [round(i) for i in np.linalg.solve(a, b)]
