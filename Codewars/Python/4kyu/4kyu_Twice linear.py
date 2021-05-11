def dbl_linear(n):
    arr = [1]
    x0, y0 = 0, 0
    for i in range(n):
        x, y = 2*arr[x0] + 1, 3*arr[y0] + 1
        arr.append(min(x, y))
        if min(x, y) == x:
            x0 += 1
        if min(x, y) == y:
            y0 += 1
    return arr[n]
