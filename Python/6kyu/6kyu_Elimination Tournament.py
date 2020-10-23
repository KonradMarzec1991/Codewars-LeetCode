def tourney(inp):
    result = [inp.copy()]
    length = len(inp)
    while length > 1:
        temp = []
        if length % 2:
            arr = [0, inp[-1]] + inp[:-1]
        else:
            arr = inp.copy()
        for i in range(0, len(arr) - 1, 2):
            temp.append(max(arr[i], arr[i + 1]))
        result.append(temp)
        inp = temp.copy()
        length = len(inp)
    return result
