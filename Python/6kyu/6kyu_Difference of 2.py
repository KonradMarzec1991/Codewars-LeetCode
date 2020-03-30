def twos_difference(lst):
    arr, length = [], len(lst)
    for i in range(length):
        for j in range(i+1, length):
            if abs(lst[i] - lst[j]) == 2:
                if lst[j] > lst[i]:
                    arr.append((lst[i], lst[j]))
                else:
                    arr.append((lst[j], lst[i]))
    return sorted(arr)


# Amazing CW solution!
def twos_difference1(a):
    s = set(a)
    return sorted((x, x + 2) for x in a if x + 2 in s)