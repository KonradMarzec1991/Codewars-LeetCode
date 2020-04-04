def longest_palindrome(s):
    if s == s[::-1] or len(s) <= 1:
        return s
    longest = ''
    i, j = 0, 1
    while i < len(s):
        if len(s[i:]) <= len(longest):
            return longest
        while j <= len(s):
            result = s[i:j]
            if len(result) > len(longest) and result == result[::-1]:
                longest = result
            j += 1
        i += 1
        j = i + 1
    return longest


p = [[1, 2, 3],
     [8, 9, 4],
     [7, 6, 5]]


def spiral(array):
    arr = []
    while array:
        arr.extend(array.pop(0))
        array = list(zip(*array))
        array.reverse()
    return arr


