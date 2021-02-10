def same_col_seq(val, k, col):
    from math import sqrt
    if col == 'yellow':
        return []
    output = []
    start_point = int((sqrt(1+8*val)-1)/2) + 1
    for i in range(val+1, 2*k*val):
        value = start_point*(start_point + 1)/2
        start_point += 1
        if define_colour(value) == col:
            output.append(int(value))
            if len(output) == k:
                break
    return output


def define_colour(n):
    if n % 3 == 0:
        return 'blue'
    return 'red'
