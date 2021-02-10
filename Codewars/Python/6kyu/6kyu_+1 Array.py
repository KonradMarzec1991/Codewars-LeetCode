def up_array(arr):
    if not isinstance(arr, list):
        return None
    if len(arr) == 0:
        return None
    if not all(isinstance(x, int) and 10 > x >= 0 for x in arr):
        return None
    num = int("".join(str(x) for x in arr))
    num += 1
    return list(map(int, list(str(num))))