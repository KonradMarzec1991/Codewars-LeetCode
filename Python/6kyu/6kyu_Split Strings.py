from textwrap import wrap


def solution(s):

    if s is None or len(s) == 0 or type(s) is not str:
        return []

    if len(s) % 2 == 0:
        return wrap(s, 2)
    else:
        arr = wrap(s, 2)
        arr[len(arr) - 1] = arr[len(arr) - 1] + "_"
        return arr