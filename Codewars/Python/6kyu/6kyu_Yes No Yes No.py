def yes_no(arr):
    if len(arr) < 3:
        return arr
    new_arr = []
    while arr:
        new_arr.append(arr.pop(0))
        if arr:
            arr.append(arr.pop(0))
    return new_arr
