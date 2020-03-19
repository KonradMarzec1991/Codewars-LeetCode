def longest_palindrome(s):
    s_alpha = ''.join(e for e in s.lower() if e.isalnum())
    d, even, odds = {}, [], []
    for ch in s_alpha:
        d[ch] = d.get(ch, 0) + 1
    for k, v in d.items():
        if d[k] % 2 == 0:
            even.append(d[k])
        else:
            odds.append(d[k]-1)
    return sum(even) + (sum(odds) + 1 if odds else 0)