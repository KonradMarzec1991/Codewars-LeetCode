def mul(m1, m2):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += m1[i][k] * m2[k][j]
    return res


def pow_fib_matrix(m):
    top_left = m[0][0] ** 2 + m[0][1] * m[1][0]
    bottom_right = m[1][0] * m[0][1] + m[1][1] ** 2
    co = top_left - bottom_right
    return [[top_left, co], [co, bottom_right]]


def fib(n):
    t = [[1, 1], [1, 0]]
    i = 2
    while n >= i:
        t = pow_fib_matrix(t)
        i *= 2
    print(t)
    s = i//2
    while n > s + 1:
        t = mul(t, [[1, 1], [1, 0]])
        s += 1
    print(t)
    print(i)
    return t[0][0]


print(fib(1000000))