def binary_array_to_number(arr):

    if len(arr) == 0:
        return None
    else:
        joined_values = "".join(str(x) for x in arr)
        return int(joined_values, 2)