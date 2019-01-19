def find_uniq(arr):

    arr.sort()
    if arr[0] == arr[1]:
        return arr[len(arr) - 1]
    else:
        return arr[0]


print(find_uniq([3, 10, 3, 3, 3]))
