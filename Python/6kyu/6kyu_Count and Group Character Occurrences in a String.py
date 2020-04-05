def get_char_count(s):
    from collections import defaultdict
    s, d, default = s.lower(), dict(), defaultdict(list)
    for v in s:
        if v.isalnum():
            d[v] = d.get(v, 0) + 1
    for k, v in sorted(d.items(), key=lambda x: -x[1]):
        default[v].append(k)
        default[v].sort()
    return default
