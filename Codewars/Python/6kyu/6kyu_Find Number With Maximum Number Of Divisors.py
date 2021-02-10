def find_divs(num):
    if num == 1:
        return 1
    arr = [1, num]
    for i in range(2, int(num ** .5 + 1)):
        if num % i == 0:
            if num/i == i:
                arr.append(i)
            else:
                arr.append(i)
                arr.append(num/i)
    return len(arr)


def div_num(a, b):
    if a > b:
        return 'Error'
    max_num = 0, 0
    for i in range(a, b+1):
        if find_divs(i) > max_num[1]:
            max_num = i, find_divs(i)
    return max_num[0]
