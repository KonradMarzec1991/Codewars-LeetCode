def is_int_array(arr):
    if not isinstance(arr, list):
        return False
    if len(arr) == 0:
        return True
    for item in arr:
        if isinstance(item, (int, float)) and item%1 == 0:
            continue
        else:
            return False
    return True