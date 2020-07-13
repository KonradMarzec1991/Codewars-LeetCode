def solve(st):
    import string
    return ''.join(sorted(st)) in string.ascii_lowercase
