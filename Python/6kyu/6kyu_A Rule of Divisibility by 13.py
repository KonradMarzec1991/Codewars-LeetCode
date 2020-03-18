def thirt(n):
    arr = [1, 10, 9, 12, 3, 4]
    while True:
        n2 = list(map(int, [x for x in str(n)[::-1]]))
        if len(n2) > len(arr):
            new_arr = arr * (len(n2) // len(arr)) + arr[:len(n2) % len(arr)]
            val2 = sum(x*y for x, y in zip(n2, new_arr))
        else:
            val2 = sum(x*y for x, y in zip(n2, arr))
        if n == val2:
            return n
        n = val2