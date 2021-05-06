def jumbled_string(s, n):
    cache = [s]
    while True:
        s = s[::2] + s[1::2]
        if cache[0] == s:
            break
        cache.append(s)
    return cache[n % len(cache)]
