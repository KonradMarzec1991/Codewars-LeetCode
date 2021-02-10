def count_adjacent_pairs(st):
    from itertools import groupby
    return len([key for key, group in groupby(st.lower().split(' ')) if len(list(group)) >= 2])
