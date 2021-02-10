def first_n_smallest(arr, n):
    from heapq import nsmallest
    from collections import Counter
    counter = Counter(nsmallest(n, arr))
    output = []
    for item in arr:
        if counter.get(item, 0):
            output.append(item)
            counter[item] -= 1
    return output