from itertools import groupby
MAPPING = {'0': '00', '1': '0'}


def send(s):
    binary = ''.join(format(ord(x), 'b') for x in s)
    binary = '0' * (7 - len(binary)) + binary
    arr = []
    for key, group in groupby(binary):
        group2 = len(list(group))
        arr.append(MAPPING[key])
        arr.append(group2 * '0')
    return ' '.join(arr)


def receive(s):
    return

