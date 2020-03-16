def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    longest, j = '', 0
    for _ in strarr:
        connected = ''.join(strarr[j:j+k])
        if len(connected) > len(longest):
            longest = connected
        j += 1
    return longest