def sum_arrays(array1, array2):
    if not array1 and not array2:
        return []

    def join_to_str(arr):
        if not arr:
            return 0
        return int(''.join(map(str, arr)))
    num = str(join_to_str(array1) + join_to_str(array2))
    if num.startswith('-'):
        num_list = [(num[:2])] + list(num[2:])
    else:
        num_list = list(num)
    return list(map(int, num_list))
