def duplicate_sandwich(arr):
    found_duplicate, output = False, []
    for i in arr:
        if arr.count(i) > 1:
            found_duplicate = not found_duplicate
            continue
        if found_duplicate:
            output.append(i)
    return output
