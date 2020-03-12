def lowest_product(input):
    from functools import reduce
    if len(input) < 4:
        return 'Number is too small'
    minimum = 9 ** 4
    for i in range(len(input) - 3):
        s = input[i:i+4]
        mult = reduce(lambda x, y: x * y, [int(ch) for ch in s])
        if mult < minimum:
            minimum = mult
    return minimum