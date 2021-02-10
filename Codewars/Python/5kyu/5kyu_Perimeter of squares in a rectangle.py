def perimeter(n):
    if n < 2:
        return 4 * n
    i, j, counter, s = 1, 1, 1, 8
    while counter < n:
        i, j = j, i + j
        s += 4*j
        counter += 1
    return s
