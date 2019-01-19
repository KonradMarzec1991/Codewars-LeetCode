def filter_list(l):

    if not isinstance(l, list):
        return []

    return [x for x in l if isinstance(x, int)]
