def solve(arr):
    arr = arr[::-1]
    result = []
    for item in arr:
        if item not in result:
            result.append(item)
    return result[::-1]
