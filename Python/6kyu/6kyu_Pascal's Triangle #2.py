def pascal(p):
    output, start = [[1]], [1]
    for i in range(p-1):
        temp = [1]
        for j in range(len(start) - 1):
            temp.append(start[j] + start[j+1])
        temp.append(1)
        start = temp
        output.append(temp)
    return output
