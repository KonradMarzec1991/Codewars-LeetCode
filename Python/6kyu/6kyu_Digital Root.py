def digital_root(n):

    array = []

    while n >= 1:
        root = int(n) % 10
        array.append(root)
        n /= 10

    value = sum(array)

    if value < 10:
        return value
    else:
        return digital_root(value)
