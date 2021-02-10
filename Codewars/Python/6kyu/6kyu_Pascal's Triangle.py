def pascals_triangle(n):
    output, start = [1], [1]
    for i in range(n-1):
        temp = [1]
        for j in range(len(start) - 1):
            temp.append(start[j] + start[j+1])
        temp.append(1)
        start = temp
        output.extend(temp)
    return output
