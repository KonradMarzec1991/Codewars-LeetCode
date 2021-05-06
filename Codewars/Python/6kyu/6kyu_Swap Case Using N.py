def swap(s, n):
    b, new_s, i = bin(n)[2:], '', 0
    for ch in s:
        if ch.isalpha():
            if b[i] == '1':
                new_s += ch.swapcase()
            else:
                new_s += ch
            if i < len(b) - 1:
                i += 1
            else:
                i = 0
        else:
            new_s += ch
    return new_s
