def atomic_number(electrons):
    arr, i = [], 1
    p = lambda n: 2 * n ** 2
    while electrons > 0:
        num = p(i)
        if electrons > num:
            arr.append(num)
        else:
            arr.append(electrons)
            break
        electrons -= num
        i += 1
    return arr


