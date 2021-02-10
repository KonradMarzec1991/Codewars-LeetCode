def solution(n):
    import math
    if not isinstance(n, int) and not isinstance(n, float):
        return "Not a number!!!"

    if n - math.floor(n) >= 0.75:
        return math.ceil(n)
    elif 0.75 > n - math.floor(n) >= 0.25:
        return math.floor(n) + 0.5
    elif n - math.floor(n) < 0.25:
        return math.floor(n)