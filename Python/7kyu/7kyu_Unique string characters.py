def solve(a, b):
    return ''.join([ch for ch in a if ch not in b] + [ch for ch in b if ch not in a])