def find_outlier(integers):
    is_even, is_odd = [], []
    for i in integers[:3]:
        if i % 2 == 0:
            is_even.append(i)
        else:
            is_odd.append(i)

    i = 0
    if len(is_even) > len(is_odd):
        while i < len(integers):
            if integers[i] % 2 == 1:
                return integers[i]
            i += 1
    else:
        while i < len(integers):
            if integers[i] % 2 == 0:
                return integers[i]
            i += 1
