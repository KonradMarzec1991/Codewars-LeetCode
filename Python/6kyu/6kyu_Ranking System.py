def rankings(arr):
    return [sorted(arr, reverse=True).index(n) + 1 for n in arr]

