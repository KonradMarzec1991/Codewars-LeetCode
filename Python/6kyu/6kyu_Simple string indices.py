def solve(st, idx):
    if st[idx] != '(':
        return -1
    left = []
    left_appeared = False
    for i in range(idx, len(st)):
        if st[i] == '(':
            left.append(st[i])
            left_appeared = True
        if st[i] == ')':
            if not left:
                break
            left.pop()
        if not left and left_appeared:
            return i
    return -1
