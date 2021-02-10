def kPermutationsOfN(indices, m):
    import itertools
    if m > len(indices) or m == 0:
        return [[]]
    return [list(indice) for indice in itertools.permutations(indices, m)]