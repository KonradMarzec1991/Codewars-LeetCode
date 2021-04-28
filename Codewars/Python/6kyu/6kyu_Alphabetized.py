def alphabetized(s):
    s = list("".join(x for x in s if x.isalpha()))
    s.sort(key=lambda x: x.lower())
    s = "".join(s)
    return s
