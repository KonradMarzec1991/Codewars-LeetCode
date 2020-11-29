def solve(arr):
    from itertools import zip_longest, chain
    arr = sorted(arr, reverse=True)
    return [
        num for num in chain.from_iterable(
            zip_longest(
                arr[:len(arr)//2],
                arr[len(arr)//2:][::-1],
                fillvalue='xxx'
            )
        ) if num != 'xxx'
    ]
