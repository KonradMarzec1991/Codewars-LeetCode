def solve(arr):
    from collections import Counter
    counter = Counter(arr)
    print(counter)
    return sorted(arr, key=lambda s: (-counter[s], s))
