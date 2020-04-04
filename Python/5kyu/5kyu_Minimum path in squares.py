def min_path(grid, x, y):
    for i in range(1, x+1):
        grid[0][i] = grid[0][i-1] + grid[0][i]

    for j in range(1, y+1):
        grid[j][0] = grid[j-1][0] + grid[j][0]

    for i in range(1, x+1):
        for j in range(1, y+1):
            grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
    return grid[y][x]


square = [
    [1, 2, 3, 6, 2, 8, 1],
    [4, 8, 2, 4, 3, 1, 9],
    [1, 5, 3, 7, 9, 3, 1],
    [4, 9, 2, 1, 6, 9, 5],
    [7, 6, 8, 4, 7, 2, 6],
    [2, 1, 6, 2, 4, 8, 7],
    [8, 4, 3, 9, 2, 5, 8]]


print(min_path(square, 6, 6))
print(min_path(square, 4, 2))