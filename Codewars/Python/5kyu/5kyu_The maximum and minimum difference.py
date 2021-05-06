# solution for CW
from math import inf


def max_and_min(seq1, seq2):
    seq1.sort()
    seq2.sort()
    maximum = max(seq1[-1] - seq2[0], seq2[-1] - seq1[0])
    minimum = inf
    index_1 = index_2 = 0
    while index_1 < len(seq1) and index_2 < len(seq2):
        minimum = min(minimum, abs(seq1[index_1] - seq2[index_2]))
        if seq1[index_1] < seq2[index_2]:
            index_1 += 1
        else:
            index_2 += 1
    return maximum, minimum
