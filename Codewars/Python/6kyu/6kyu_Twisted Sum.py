def compute_sum(n):
    if n < 10:
        return int(n*(n+1)/2)
    s = 45
    while n > 9:
        x = sum(map(int, str(n)))
        s += x
        n -= 1
    return s
