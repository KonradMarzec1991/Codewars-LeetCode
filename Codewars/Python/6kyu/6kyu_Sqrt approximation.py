def sqrt_approximation(number):
    k = eval('number*' + '*.5')
    return int(k) if k.is_integer() else [int(k), int(k) + 1]
