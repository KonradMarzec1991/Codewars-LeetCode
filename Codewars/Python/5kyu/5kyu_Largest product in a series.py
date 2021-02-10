def greatest_product(n):
    from functools import reduce
    maximum, temp = 0, 0
    for i, v in enumerate(n[:-4]):
        piece = n[i:i+5]
        if '0' in piece:
            continue
        elif '99999' in piece:
            return 59049
        temp = reduce(lambda x, y: x*y, map(int, piece))
        if temp > maximum:
            maximum = temp
    return maximum
