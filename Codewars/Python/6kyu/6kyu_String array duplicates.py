def dup(arry):
    result = []
    s = ''
    from itertools import groupby
    for item in arry:
        for ch, _ in groupby(item):
            s += ch
        result.append(s)
        s = ''
    return result
