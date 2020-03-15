def alternateCase(s):
    s2 = ''
    for ch in s:
        if ch.isupper():
            s2 += ch.lower()
        else:
            s2 += ch.upper()
    return s2