def combine(*args):
    from itertools import zip_longest
    arr = []
    for val in zip_longest(*args):
        for k in val:
            if k is not None:
                arr.append(k)
    return arr


# Great solution from CW
def combine(*args):
    from itertools import chain, zip_longest
    return filter(lambda x: x is not None,
                  chain.from_iterable(zip_longest(*args)))
