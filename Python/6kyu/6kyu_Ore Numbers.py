def is_ore(n):
    temp = 0.0

    divs = find_divisors(n)
    count = len(divs)

    for i in divs:
        temp += 1.0 / i
    return (count / temp) - int(count / temp) < 1e-5


def find_divisors(n):
    from math import sqrt
    arr = [1]
    for x in range(2, int(sqrt(n)) + 1):
        if n % x == 0:
            arr.append(x)
            arr.append(n / x)

    arr.append(n)
    arr = [int(i) for i in arr]
    return sorted(set(arr))
