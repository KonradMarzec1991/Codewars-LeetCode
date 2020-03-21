def decomp(n):
    import math
    if not isinstance(n, int) or n <= 0:
        return ''
    d = {}
    for x in range(2, n + 1):
        while x % 2 == 0:
            if 2 in d:
                d[2] += 1
            else:
                d[2] = 1
            x = x / 2

        for i in range(3, int(math.sqrt(x)) + 1, 2):
            while x % i == 0:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
                x = x / i

        if x > 2:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

    s = ''
    for k, v in d.items():
        if v == 1:
            s += str(k) + " * "
        else:
            s += str(k) + '^' + str(v) + " * "
    return s[:-3]
