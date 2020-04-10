def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return "Not valid"
    if num < 10:
        return 0
    counter = 0
    s = str(num)
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i: j + 1] == s[i: j + 1][::-1]:
                counter += 1
    return counter