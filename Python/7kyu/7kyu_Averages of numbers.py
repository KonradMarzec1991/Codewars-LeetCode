def averages(arr):
    return [sum(arr[i:i+2])/2 for i in range(len(arr)-1)] if arr and len(arr) > 1 else []