def josephus_survivor(n,k):

    num = 0
    for x in range(1, n + 1):
        num = (num + k) % x

    return num + 1
