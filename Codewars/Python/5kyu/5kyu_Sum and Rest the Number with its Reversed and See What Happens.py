def sum_dif_rev(n):
    start_list = [45, 54, 495, 594]
    temp = []
    if n < 5:
        return start_list[n-1]
    i = 4356
    while len(start_list) < n:
        if i % 10 != 0 and not str(i) == str(i)[::-1]:
            if i in temp and i not in start_list:
                start_list.append(i)
            else:
                rev = int(str(i)[::-1])
                if (i + rev) % abs(i - rev) == 0:
                    start_list.append(i)
                    temp.append(rev)
        i += 9
    return start_list[n-1]
