def sum_consecutives(s):
    temp, final = [], []
    s = s + [None]
    for index, value in enumerate(s[:-1]):
        if s[index] == s[index+1]:
            temp.append(s[index])
        else:
            if len(temp) != 0:
                temp.append(s[index])
                final.append(sum(temp))
                temp = []
            else:
                final.append(s[index])
    return final


# Great solution from CW
def sum_consecutives(s):
    from itertools import groupby
    return [sum(group) for c, group in groupby(s)]


