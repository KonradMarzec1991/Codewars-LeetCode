def switcher(arr):
    s = 'zyxwvutsrqponmlkjihgfedcba!? '
    return ''.join([s[int(ch)-1] for ch in arr])
