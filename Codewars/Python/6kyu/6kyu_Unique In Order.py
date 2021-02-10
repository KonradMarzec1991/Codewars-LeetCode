def unique_in_order(iterable):
    if iterable is None or len(iterable) == 0:
        return []
    my_list = []
    x = 0

    while x < len(iterable) - 1:
        if iterable[x] != iterable[x+1]:
            my_list.append(iterable[x])
        x += 1

    my_list.append(iterable[len(iterable) - 1])
    return my_list



