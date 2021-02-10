from collections import defaultdict
from functools import wraps


class FuncAdd:
    values = defaultdict(list)

    def __init__(self, fn):
        wraps(fn)(self)
        self.name = fn.__name__
        FuncAdd.values[self.name].append(fn)

    def __call__(self, *args, **kwargs):
        results = []
        funcs = FuncAdd.values.get(self.name, None)
        if funcs is not None:
            for f in funcs:
                results.append(f(*args, **kwargs))
            return tuple(results)
        else:
            raise NameError

    @classmethod
    def delete(cls, fn):
        del cls.values[fn.__wrapped__.__name__]

    @classmethod
    def clear(cls):
        cls.values.clear()
