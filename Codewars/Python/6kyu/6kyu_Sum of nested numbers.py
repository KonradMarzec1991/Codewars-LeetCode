def sum_nested_numbers(arr, depth=1):
    result = 0
    for item in arr:
        if isinstance(item, int):
            result += item ** depth
        else:
            result += sum_nested_numbers(item, depth + 1)
    return result
