def max_sequence(arr):
    max_local, max_global = 0, 0
    for a in arr:
        max_local += a
        if max_local < 0:
            max_local = 0
        if max_local > max_global:
            max_global = max_local
    return max_global
