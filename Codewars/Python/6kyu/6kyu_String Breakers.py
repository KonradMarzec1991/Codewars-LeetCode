def string_breakers(n, st):
    s = ''.join(st.split(' '))
    return '\n'.join([s[i:i+n] for i in range(0, len(s), n)])
