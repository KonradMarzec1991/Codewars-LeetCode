def freq_seq(s, sep):
    return sep.join([str(s.count(ch)) for ch in s])
