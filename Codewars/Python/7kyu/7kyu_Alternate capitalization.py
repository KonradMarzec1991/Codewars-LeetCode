def capitalize(s):
    arr = ''.join([v if i % 2 else v.upper() for i, v in enumerate(s)])
    return [arr, arr.swapcase()]