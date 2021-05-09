def number(lines):
    import itertools
    if len(lines) == 0:
        return []
    output = []
    counter = itertools.count()
    next(counter)
    for line in lines:
        output.append(f'{next(counter)}: {line}')
    return output
