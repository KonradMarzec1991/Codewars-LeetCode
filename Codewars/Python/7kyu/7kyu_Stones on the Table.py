def solution(stones):
    from itertools import groupby
    duplicates = 0
    for _, group in groupby(stones):
        added = len(list(group)) - 1
        duplicates += added
    return duplicates