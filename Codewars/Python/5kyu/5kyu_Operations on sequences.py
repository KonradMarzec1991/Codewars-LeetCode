# that not working
def solve_brute(arr):
    import functools
    import operator
    import math

    result = functools.reduce(
        operator.mul,
        [x*x + y*y for x, y in zip(arr[::2], arr[1::2])]
    )
    for i in range(int(math.sqrt(result))+1):
        val = i ** 2
        val2 = result - val
        if math.sqrt(val2) == int(math.sqrt(val2)):
            return [int(val**.5), int(val2**.5)]
    return []


def solve(arr):
    a, b, c, d = arr[0:4]
    first = abs(a*c-b*d)
    second = a*d + b*c
    result = [first, second]
    if len(arr) == 4:
        return result
    return solve(result + arr[4:])
