def solve(s):
    r = list(s[::-1].replace(' ', ''))
    s1 = ''
    for i, v in enumerate(s):
        if v == ' ':
            s1 += ' '
        else:
            s1 += r.pop(0)
    return s1
