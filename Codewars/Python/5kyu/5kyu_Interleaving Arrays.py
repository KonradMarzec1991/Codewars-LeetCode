def interleave(*args):
    from itertools import zip_longest
    result = []
    for item in zip_longest(*args):
        for t_item in item:
            result.append(t_item)
    return result
