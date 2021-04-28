def even_binary(n):
    n = n.split(' ')
    m = map(int, n)
    temp = []
    for i, v in enumerate(m):
        if v % 2 == 0:
            temp.append(v)
    temp.sort(reverse=True)
    for i, v in enumerate(n):
        if int(v) % 2 == 0:
            n[i] = str(temp.pop()).zfill(3)
    return ' '.join(n)
