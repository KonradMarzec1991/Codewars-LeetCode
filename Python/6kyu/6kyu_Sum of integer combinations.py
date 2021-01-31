import itertools


def find(arr, n):
    counter = 0
    start = 1
    while start <= len(arr):
        for comb in itertools.combinations_with_replacement(arr, start):
            if sum(comb) == n:
                counter += 1
        start += 1
    return counter
