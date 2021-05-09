def exp_sum(n):
    if n <= 3:
        return n
    matrix = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        matrix[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                val_up = matrix[i-1][j]
                val_combination = matrix[i][j-i]
                matrix[i][j] = val_up + val_combination
    return matrix[n][n]
