def deep_count(a):
    counter = 0
    for item in a:
        if type(item) == list:
            counter += deep_count(item)
        counter += 1
    return counter