def largest_sum(arr):
    if not arr or max(arr) < 0:
        return 0
    if min(arr) > 0:
        return sum(arr)
    max_result = float('-inf')
    temp = 0

    for i in range(len(arr)):
        temp += arr[i]
        if temp > max_result:
            max_result = temp
        if temp < 0:
            temp = 0
    return max_result
