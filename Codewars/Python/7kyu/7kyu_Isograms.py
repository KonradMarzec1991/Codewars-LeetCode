def is_isogram(string):
    s_len = len(string.lower())
    s1_len = len(set(string.lower()))
    return s_len == s1_len