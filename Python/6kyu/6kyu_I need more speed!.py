def reverse(seq):
    point = len(seq)
    if point % 2 == 0:
        middle = point//2 - 1
    else:
        middle = point//2
    for i in range(middle+1):
        seq[i], seq[point-i-1] = seq[point-i-1], seq[i]
