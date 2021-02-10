def triangle_type(a, b, c):
    if not (a + b > c and b + c > a and a + c > b):
        return 0
    sides = sorted([a, b, c])
    if sides[2] ** 2 == sides[1] ** 2 + sides[0] ** 2:
        return 2
    elif sides[2] ** 2 > sides[1] ** 2 + sides[0] ** 2:
        return 1
    else:
        return 3
