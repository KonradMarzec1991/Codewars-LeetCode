def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[len(arr) - 1]
    else:
        return arr[0]
