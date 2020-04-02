def index_equals_value(arr):
    first, last = 0, len(arr)
    while first < last:
        mid = (first + last)//2
        if arr[mid] >= mid:
            last = mid
        else:
            first = mid + 1
    if first < len(arr) and arr[first] == first:
        return first
    else:
        return -1