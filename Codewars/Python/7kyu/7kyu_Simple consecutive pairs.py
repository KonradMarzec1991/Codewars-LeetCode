def pairs(ar):
    return sum([
        1 if len(ar[i:i+2]) == 2 and abs(ar[i+1] - ar[i]) == 1 else 0
        for i in range(0, len(ar), 2)
    ])
