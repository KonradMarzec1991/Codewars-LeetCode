def sequence_classifier(arr):
    if len(set(arr)) == 1:
        return 5
    if len(set(arr)) == len(arr) and arr == sorted(arr):
        return 1
    if len(set(arr)) < len(arr) and arr == sorted(arr):
        return 2
    if len(set(arr)) == len(arr) and arr == sorted(arr, reverse=True):
        return 3
    if len(set(arr)) < len(arr) and arr == sorted(arr, reverse=True):
        return 4
    return 0
