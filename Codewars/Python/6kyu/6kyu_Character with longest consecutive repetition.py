def longest_repetition(chars):
    import itertools
    if len(chars) == 0:
        return '', 0
    return max(
        [(ch, len(list(group))) for ch, group in itertools.groupby(chars)],
        key=lambda x: x[1]
    )