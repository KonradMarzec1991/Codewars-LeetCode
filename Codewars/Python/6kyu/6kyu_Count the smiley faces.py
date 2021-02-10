def count_smileys(arr):
    import re
    counter = 0
    for smile in arr:
        if bool(re.match(r'^(:|;)(-|~)?(\)|D)$', smile)):
            counter += 1
    return counter