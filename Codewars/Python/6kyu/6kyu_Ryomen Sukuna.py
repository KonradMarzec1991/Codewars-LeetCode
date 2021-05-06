def sukuna(n):
    l = []
    for i in range(2, int(n ** .5) + 1):
        p = i
        while p <= n:
            p *= i
            if p <= n:
                l.append(p)
    return n - len(set(l))
