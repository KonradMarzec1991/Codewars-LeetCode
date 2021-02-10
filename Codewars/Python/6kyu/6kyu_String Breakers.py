def string_breakers(n, st):
    s = ''.join(st.split(' '))
    return '\n'.join([s[i:i+n] for i in range(0, len(s), n)])


st = "This is an example string";
n = 5

print(string_breakers(n, st))