def max_and_min(arr1, arr2):
    min_val = float('inf')
    max_val = float('-inf')

    for i in arr1:
        for j in arr2:
            diff = abs(i - j)
            if diff > max_val:
                max_val = diff
            if diff < min_val:
                min_val = diff
    return [max_val, min_val]
