shorter_reverse_longer = lambda a, b: a + b[::-1] + a if len(b) > len(a) else b + a[::-1] + b
