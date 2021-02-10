def path_finder(maze):
    maze = [list(row) for row in maze.split('\n')]
    goal = len(maze)
    not_visited = [(0, 0)]

    while not_visited:
        x, y = not_visited.pop(0)

        if 0 <= x < goal and 0 <= y < goal:
            if x == goal-1 and y == goal-1:
                return True
            if maze[x][y] == '.':
                maze[x][y] = 'W'
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    not_visited.append((x + dx, y + dy))
    return False
