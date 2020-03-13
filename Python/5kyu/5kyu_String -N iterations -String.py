def jumbled_string(s, n):
    cache = [s]
    while True:
        s = s[::2] + s[1::2]
        if cache[0] == s:
            break
        cache.append(s)
    return cache[n % len(cache)]


print(jumbled_string('abcde', 10))
print(jumbled_string("Such Wow!", 1))