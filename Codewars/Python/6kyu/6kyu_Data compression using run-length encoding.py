def encode(string):
    from itertools import groupby
    result = ''
    for key, group in groupby(string):
        num = str(len(list(group)))
        result += num
        result += key
    return result


def decode(string):
    import re
    result = ''
    string = re.split('(\d+)', string)
    for i in range(1, len(string) - 1, 2):
        result += int(string[i])*string[i+1]
    return result
