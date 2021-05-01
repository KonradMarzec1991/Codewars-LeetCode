import numbers


def sumDigits(number):
    if not isinstance(number, numbers.Number):
        return "Not a number!!!"
    sum_of = 0
    number = str(abs(number))
    for digit in number:
        sum_of += int(digit)
    return sum_of
