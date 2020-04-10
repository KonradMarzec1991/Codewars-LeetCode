def palindrome(n, s):
    if not (isinstance(n, int) and isinstance(s, int)) or n < 0 or s < 0:
        return "Not valid"
    result = []
    if n < 11:
        n = 11
    while s:
        st = str(n)
        if st == st[::-1]:
            result.append(n)
            s -= 1
        n += 1
    return result
