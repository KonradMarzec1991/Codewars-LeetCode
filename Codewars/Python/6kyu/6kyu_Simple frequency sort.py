def solve(arr):
    from collections import Counter
    counter = Counter(arr)
    return sorted(arr, key=lambda s: (-counter[s], s))
