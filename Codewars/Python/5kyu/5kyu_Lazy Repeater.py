def make_looper(string):
    index = 0

    def f():
        nonlocal index
        if index >= len(string):
            index = 0
        out = string[index]
        index += 1
        return out
    return f


def make_looper(s):
    from itertools import cycle

    class C:
        def __init__(self, s):
            self.s = cycle(s)

        def __call__(self):
            return next(self.s)
    return C(s)


def make_looper(s):
    from itertools import cycle
    g = cycle(s)
    return lambda: next(g)


from itertools import cycle


class make_looper(cycle):
    def __call__(self):
        return self.__next__()


def make_looper(string):
    def looper():
        while True:
            for c in string:
                yield c

    loop = looper()

    return lambda: next(loop)
