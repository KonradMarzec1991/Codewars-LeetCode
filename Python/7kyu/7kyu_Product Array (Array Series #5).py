def product_array(numbers):
    from functools import reduce
    return [reduce(lambda a, b: a*b, numbers)/x for x in numbers]