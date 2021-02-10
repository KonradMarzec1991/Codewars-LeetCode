def send(s):
    from itertools import groupby
    MAPPING = {'0': '00', '1': '0'}
    binary = ''.join(format(ord(x), '07b') for x in s)
    arr = []
    for key, group in groupby(binary):
        group2 = len(list(group))
        arr.append(MAPPING[key])
        arr.append(group2 * '0')
    return ' '.join(arr)


def receive(s):
    MAPPING_REV = {'00': '0', '0': '1'}
    arr, s = s.split(' '), ''
    for i in range(0, len(arr) - 1, 2):
        s += MAPPING_REV[arr[i]] * len(arr[i+1])
    return ''.join([chr(int(s[i:i+7], 2)) for i in range(0, len(s), 7)])
