def choose_best_sum(t, k, ls):
    from itertools import combinations
    if k > len(ls) or sum(sorted(ls)[:k]) > t:
        return None
    maks = 0
    for comb in combinations(ls, r=k):
        s = sum(comb)
        if t >= s > maks:
            maks = s
        if maks == t:
            break
    return maks

