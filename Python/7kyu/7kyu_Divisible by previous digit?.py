def divisible_by_last(n):
    n = list(map(int, str(n)))
    output = []
    for i in range(len(n)-1, 0, -1):
        if n[i-1] == 0 or n[i] % n[i-1] != 0:
            output.append(False)
        else:
            output.append(True)
    return [False] + output[::-1]
