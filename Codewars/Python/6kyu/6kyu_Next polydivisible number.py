def next_num(n):
    if n == 0:
        return 1
    if n < 10:
        return n
    result = ''
    str_n = str(n)
    for i in range(len(str_n)):
        current = int(result + str_n[i])
        j = i + 1
        while current % j != 0:
            current += 1
        result += str(current)[-1]
    return int(result)
