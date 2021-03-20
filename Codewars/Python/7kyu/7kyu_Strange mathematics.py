def strange_math(n, k):
    return sorted(list(map(str, range(1, n+1)))).index(str(k)) + 1


# Great CW solution
def strange_math_v1(n, k):
    return sorted(range(n+1), key=str).index(k)
