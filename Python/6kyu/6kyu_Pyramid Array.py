def pyramid(n):
    arr = []
    for i in range(n):
        arr.append([1 for i in range(i+1)])
    return arr