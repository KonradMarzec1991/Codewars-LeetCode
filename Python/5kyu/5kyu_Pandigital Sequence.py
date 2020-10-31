def get_sequence(offset, size):
    from itertools import count
    thres = 1023456789
    if offset < thres:
        offset = thres
    res = []
    if offset >= 9999999999:
        return res
    for i in count(start=offset):
        if set(str(i)) == set('1234567890'):
            res.append(i)
            if len(res) == size:
                return res
