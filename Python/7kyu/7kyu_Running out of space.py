from itertools import accumulate


def spacey(array):
    result, arr = '', []
    for item in array:
        result += item
        arr.append(result)
    return arr


def spacey2(a):
    return list(accumulate(a))
