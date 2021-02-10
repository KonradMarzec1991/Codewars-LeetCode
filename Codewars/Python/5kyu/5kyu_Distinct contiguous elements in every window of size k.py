from collections import defaultdict


def count_contiguous_distinct(k, x):
    temp = defaultdict(lambda: 0)
    dist, z = 0, []

    for i in range(k):
        if temp[x[i]] == 0:
            dist += 1
        temp[x[i]] += 1
    z.append(dist)

    for j in range(k, len(x)):
        if temp[x[j - k]] == 1:
            dist -= 1
        temp[x[j - k]] -= 1

        if temp[x[j]] == 0:
            dist += 1
        temp[x[j]] += 1

        z.append(dist)
    return z
