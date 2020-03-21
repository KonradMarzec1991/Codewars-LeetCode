def find_pattern(sequence):
    temp = []
    if len(sequence) == 2:
        return [sequence[1] - sequence[0]]
    for i, v in enumerate(sequence[1:]):
        temp.append(sequence[i+1] - sequence[i])
    for i in range(1, len(temp)+1):
        loc = temp[:i]
        for j in range(1, len(temp)+1):
            if loc * j == temp:
                return loc
