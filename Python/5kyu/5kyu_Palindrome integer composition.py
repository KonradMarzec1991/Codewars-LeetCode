def values(n):
    pal, i = set(), 1
    while i * i <= n:
        j = i + 1
        squares = i * i + j * j
        while squares <= n:
            if str(squares) == str(squares)[::-1]:
                pal.add(squares)
            j += 1
            squares += j * j
        i += 1
    return len(pal)
