def circularly_sorted(arr):
    if arr == sorted(arr):
        return True
    cut = 0
    for val in range(len(arr) - 1):
        if arr[val + 1] >= arr[val]:
            continue
        else:
            cut = val
            break
    new_arr = arr[cut+1:] + arr[:cut+1]
    return all(i <= j for i, j in zip(new_arr, new_arr[1:]))


# Top solution from Codewars
def circularly_sorted2(arr):
    m = arr.index(min(arr))
    return sorted(arr) == (arr[m:]+arr[:m])