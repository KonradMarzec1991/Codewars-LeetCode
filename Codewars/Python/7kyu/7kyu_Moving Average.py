def moving_average(values, n):
    if n == 0 or n > len(values):
        return None
    res = []
    for i in range(0, len(values) - n+1):
        res.append(sum(values[i:i+n])/n)
    return res
