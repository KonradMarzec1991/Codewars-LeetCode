def mergeArrays(arr1, arr2):
    i, j, z = 0, 0, []
    while i < arr1.__len__() or j < arr2.__len__():
        if j == arr2.__len__() or i < arr1.__len__() and arr1[i] <= arr2[j]:
            z += [arr1[i]]
            i += 1
        else:
            z += [arr2[j]]
            j += 1
    return z
