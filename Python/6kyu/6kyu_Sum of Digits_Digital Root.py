def digital_root(n):
    if len(str(n)) < 2:
        return n
    else:
        s = sum(list(map(int, str(n))))
        return digital_root(s)