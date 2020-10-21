def find_num(n):
    visited = [0]
    while len(visited) <= n:
        counter = 0
        while True:
            if counter not in visited:
                if not set(str(counter)).intersection(str(visited[-1])):
                    visited.append(counter)
                    break
                else:
                    counter += 1
            else:
                counter += 1
    return visited[-1]
