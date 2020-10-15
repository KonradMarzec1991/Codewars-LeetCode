def distribute_evenly(lst):
    org, dup = [], []
    for item in lst:
        if item in org:
            dup.append(item)
        else:
            org.append(item)
    while len(dup) > 0:
        for item in org:
            if item in dup:
                org.append(item)
                dup.remove(item)
    return org