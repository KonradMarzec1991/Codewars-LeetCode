def min_value(digits):
    return int(''.join(map(str, sorted(set(digits)))))


print(min_value([4, 8, 1, 4]))