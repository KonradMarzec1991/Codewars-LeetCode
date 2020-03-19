def numericals(s):
    string, dct = '', {}
    for ch in s:
        if ch not in dct.keys():
            dct[ch] = 1
        else:
            dct[ch] += 1
        string += str(dct.get(ch))
    return string