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
