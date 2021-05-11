def solution(array_a, array_b):
    return sum([abs(k-l)**2 for k, l in zip(array_a, array_b)])/len(array_a)
