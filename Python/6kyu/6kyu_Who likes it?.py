def likes(names):

    if len(names) is None or len(names) == 0:
        return "no one likes this"

    if len(names) == 1:
        return '%s likes this' % names[0]

    if len(names) == 2:
        return '%s and %s like this' % (names[0], names[1])

    if len(names) == 3:
        return '%s, %s and %s like this' % (names[0], names[1], names[2])

    if len(names) > 3:
        return '%s, %s and %s others like this' % (names[0], names[1], str(len(names) - 2))
