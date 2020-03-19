def wave(string):
    arr = []
    string = string.lower()
    for i, v in enumerate(string):
        if v == ' ':
            continue
        s = list(string)
        s[i] = s[i].upper()
        arr.append(''.join(s))
    return arr