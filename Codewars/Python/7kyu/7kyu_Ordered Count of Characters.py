def ordered_count(input):
    d = dict()
    for letter in input:
        if not letter in d:
            d[letter] = 1
        else:
            d[letter] += 1
    return sorted(list(d.items()), key=lambda x: input.index(x[0]))