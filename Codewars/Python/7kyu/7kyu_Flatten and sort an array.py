# Flatten and sort an array
def flatten_and_sort(array):
    def flatten(array, ignore_items=(str, bytes)):
        from collections import Iterable
        for x in array:
            if isinstance(x, Iterable) and not isinstance(x, ignore_items):
                yield from flatten(x)
            else:
                yield x
    arr = []
    for x in flatten(array):
        arr.append(x)
    return sorted(arr)