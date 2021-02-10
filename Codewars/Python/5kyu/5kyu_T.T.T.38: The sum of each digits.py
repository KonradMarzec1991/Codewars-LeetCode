def sum_digits_with_arr(n):
    digits_num = len(str(n))
    arr = [0] * (digits_num + 1)
    arr[0] = 0
    arr[1] = 9 * 10 // 2
    for val in range(2, digits_num):
        arr[val] = arr[val - 1] * 10 + 45 * 10 ** (val - 1)
    return sum_digits(n, arr)


def sum_digits(n, arr):
    if n <= 9:
        return n * (n + 1) // 2
    digits_num = len(str(n)) - 1
    max_div = 10 ** digits_num
    mult = n // max_div
    return mult * arr[digits_num] + (mult * (mult-1) // 2) * max_div + mult * (1 + n % max_div) + sum_digits(n % max_div, arr)


def sum_of_digits(a, b):
    return sum_digits_with_arr(b) - sum_digits_with_arr(a-1)