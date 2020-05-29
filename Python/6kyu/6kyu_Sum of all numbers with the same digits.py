def sum_arrangements(num):
    from math import factorial
    digits = len(str(num))
    mult, base = factorial(digits-1), int('1'*digits)
    return sum(map(int, str(num))) * base * mult