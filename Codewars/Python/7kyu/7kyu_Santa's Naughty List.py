def find_children(santas_list, children):
    return sorted(list(set(santas_list) & set(children)))
