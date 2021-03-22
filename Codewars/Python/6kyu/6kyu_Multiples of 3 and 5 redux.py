def arithmetic(n, d):
    n = (n - 1) // d
    return n * (n + 1) * d // 2


def solution(number):
    return arithmetic(number, 3) + arithmetic(number, 5) - arithmetic(number, 15)
