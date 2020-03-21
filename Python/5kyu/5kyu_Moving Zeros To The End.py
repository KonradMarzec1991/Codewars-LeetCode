# Not the best solution for sure, but it's working
def move_zeros(array):
    arr = []
    for val in array:
        if isinstance(val, type(None)) or isinstance(val, bool):
            arr.append(val)
            continue
        if isinstance(val, float) and int(val) == val:
            continue
        if not isinstance(val, int):
            arr.append(val)
            continue
        if isinstance(val, int) and val != 0:
            arr.append(val)
    return arr + (len(array) - len(arr))*[0]


# Great one
def move_zeros2(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))