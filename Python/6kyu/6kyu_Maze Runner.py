def maze_runner(maze, directions):
    start = 2
    start_point = (None, None)
    for index, row in enumerate(maze):
        if start in row:
            start_point = index, row.index(start)
            break

    moves = {
        'W': (0, -1),
        'E': (0, 1),
        'N': (-1, 0),
        'S': (1, 0),
    }

    sh, sv = start_point
    for direction in directions:
        h, v = moves[direction]
        sh, sv = sh + h, sv + v

        if sh < 0 or sh > len(maze) - 1:
            return 'Dead'
        if sv < 0 or sv > len(maze) - 1:
            return 'Dead'
        if maze[sh][sv] == 1:
            return 'Dead'
        if maze[sh][sv] == 3:
            return 'Finish'
        if maze[sh][sv] == 0:
            continue
    return 'Lost'