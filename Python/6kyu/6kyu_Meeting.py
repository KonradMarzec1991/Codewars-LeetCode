def meeting(strg):
    import operator
    fl_names = strg.upper().split(';')
    my_list = list()
    for name in fl_names:
        f, l = name.split(':')
        my_list.append((l, f))
    my_list.sort(key=operator.itemgetter(0, 1))
    return ''.join([f'({n[0]}, {n[1]})' for n in my_list])