def min_sum(arr):
    arr.sort()
    return sum([arr[num]*arr[-1-num] for num in range(len(arr)//2)])
