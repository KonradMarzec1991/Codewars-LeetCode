def count_inversions(array):
    if array == sorted(array) or len(array) == 0:
        return 0
    else:
        inversions = 0
        for i in range(len(array)):
            for j in range(i, len(array)):
                if array[i] > array[j]:
                    inversions += 1
    return inversions
