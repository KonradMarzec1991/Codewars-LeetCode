# CodeWars String -> N iterations -> String
def jumbled_string(s, n):
    checker = [s]
    while n:
        n -= 1
        s = s[0::2] + s[1::2]
        if s == checker[0]:
            return checker[n % len(checker)]
        else:
            checker.append(s)
    return s