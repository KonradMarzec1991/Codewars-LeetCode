def min_path(grid, x, y):
    for i in range(1, x+1):
        grid[0][i] = grid[0][i-1] + grid[0][i]

    for j in range(1, y+1):
        grid[j][0] = grid[j-1][0] + grid[j][0]

    for i in range(1, x+1):
        for j in range(1, y+1):
            grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
    return grid[y][x]
