from collections import defaultdict


class FuncAdd:
    values = defaultdict(list)

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        result = self.fn(*args, **kwargs)
        key = self.fn.__name__
        self.values[key].append(result)
        print(self.values)

    def delete(self, fn_name):
        self.values.pop(fn_name)

    def clear(self):
        self.values.clear()


@FuncAdd
def foo():
    return 'Hello'


@FuncAdd
def foo():
    return 'World'


print(foo())