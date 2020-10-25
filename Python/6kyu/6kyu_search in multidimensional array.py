def locate(seq, value):
    maintaining = [seq]
    while maintaining:
        lst = maintaining.pop()
        for i in lst:
            if isinstance(i, str):
                if i == value:
                    return True
            else:
                maintaining.append(i)
    return False
