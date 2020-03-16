def solution(s):
    temp, j = [], 0
    for i, v in enumerate(s):
        if s[i].isupper():
            temp.append(s[j:i])
            j = i
    temp.append(s[j:])
    return ' '.join(temp)


# Great CW solution
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
