def snail(snail_map):
    rows = len(snail_map)
    cols = len(snail_map[0])
    r, c = 0, 0
    arr = []

    while r < rows and c < cols:
        for i in range(c, cols):
            arr.append(snail_map[r][i])
        r += 1
        for i in range(r, rows):
            arr.append(snail_map[i][cols - 1])
        cols -= 1
        if r < rows:
            for i in range(cols - 1, c - 1, -1):
                arr.append(snail_map[rows - 1][i])
            rows -= 1
        if c < cols:
            for i in range(rows - 1, r - 1, -1):
                arr.append(snail_map[i][c])
            c += 1
    return arr


# Amazing solution from CW
def snail_v2(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = list(zip(*array))
        array.reverse()
    return a
