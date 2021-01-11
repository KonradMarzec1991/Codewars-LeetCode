def generate_pairs(n):
    return list([i, j] for i in range(n+1) for j in range(i, n+1))
