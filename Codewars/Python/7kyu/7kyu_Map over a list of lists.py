def grid_map(inp, op):
    output = []
    for arr in inp:
        temp = []
        for ele in arr:
            temp.append(op(ele))
        output.append(temp)
    return output


# Great solution from CW
def grid_map_v2(lst, op):
    return [[*map(op, x)] for x in lst]
