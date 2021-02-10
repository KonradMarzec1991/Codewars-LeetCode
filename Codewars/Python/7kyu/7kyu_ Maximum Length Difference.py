def mxdiflg(a1, a2):
    if a1 and a2:
        a1_sorted = sorted(a1, key=len)
        a2_sorted = sorted(a2, key=len)
        a1_a2_diff = abs(len(a1_sorted[-1]) - len(a2_sorted[0]))
        a2_a1_diff = abs(len(a2_sorted[-1]) - len(a1_sorted[0]))
        return max(a1_a2_diff, a2_a1_diff)
    return -1
