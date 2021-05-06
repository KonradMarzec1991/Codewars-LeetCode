def solve(st):
    st = st[::-1]
    final = ''
    for ch in st:
        if ch.isdigit():
            final *= int(ch)
        elif ch.isalpha():
            final += ch
    return final[::-1]
