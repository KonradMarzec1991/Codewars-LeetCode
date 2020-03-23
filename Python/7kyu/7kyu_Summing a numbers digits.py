def sum_digits(number):
    return sum(list(map(int, str(abs(number)))))