def stringy(size):
    i, arr, s = 0, ['1', '0'], ''
    while i < size:
        s += arr[0]
        arr.append(arr.pop(0))
        i += 1
    return s
