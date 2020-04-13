def find(seq):
    from heapq import nsmallest
    min_seq, max_seq = min(seq), max(seq)
    second_min_seq = nsmallest(2, seq)[-1]
    d = second_min_seq - min_seq
    n = (max_seq - min_seq)/d + 1
    return int(n*(min_seq + max_seq)/2 - sum(seq))
