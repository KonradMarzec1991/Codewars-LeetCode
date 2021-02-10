def parts_sums(ls):
    arr, temp = [], 0
    ls = ls[::-1]
    for num in ls:
        temp += num
        arr.append(temp)
    arr.reverse()
    arr.append(0)
    return arr