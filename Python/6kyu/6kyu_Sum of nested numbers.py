def sum_nested_numbers(arr):
    depth, final = 1, 0
    for val in arr:
        if isinstance(val, int):
            final += val ** depth
        else:
            depth += 1
            sum_nested_numbers(val)
    return


print(sum_nested_numbers([6, [5], [[4]], [[[3]]], [[[[2]]]], [[[[[1]]]]]]))