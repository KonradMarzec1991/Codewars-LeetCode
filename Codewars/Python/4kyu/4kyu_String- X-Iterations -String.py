def string_func(s, x):
    arr, s = [s], list(s)
    while True:
        s[::2], s[1::2] = s[:len(s)//2-1:-1], s[:len(s)//2]
        arr.append(''.join(s))
        if arr[-1] == arr[0]:
            break
    return arr[x % (len(arr)-1)]
