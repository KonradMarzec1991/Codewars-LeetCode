def path_finder(maze):
    maze = [list(row) for row in maze.split('\n')]
    goal = len(maze)
    not_visited = [(0, 0, 0)]

    while not_visited:
        x, y, counter = not_visited.pop(0)
        if 0 <= x < goal and 0 <= y < goal:
            if maze[x][y] == '.':
                maze[x][y] = counter
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    not_visited.append((x + dx, y + dy, counter + 1))
            if x == goal-1 and y == goal-1:
                return maze[x][y]
    return False