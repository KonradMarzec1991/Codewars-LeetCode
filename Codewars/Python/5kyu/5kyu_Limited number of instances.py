def limiter(limit, unique, lookup):
    uniq = {}
    global_lookup = 0

    if lookup == 'LAST':
        global_lookup = -1
    else:
        global_lookup = -2

    def wrapper(cls):
        def inner(*args, **kwargs):
            obj = cls(*args, **kwargs)
            attr = getattr(obj, unique)
            if attr in uniq:
                return uniq[list(uniq.keys())[global_lookup]]
            if len(uniq) == limit:
                return uniq[list(uniq.keys())[global_lookup]]
            uniq[attr] = obj
            return obj
        return inner
    return wrapper


@limiter(2, "ID", "FIRST")
class ExampleClass:
    def __init__(self, ID, value): self.ID, self.value = ID, value

    def __str__(self):
        return f'{self.__class__.__name__}({self.ID},{self.value})'


a = ExampleClass(1, 5)  # unique ID=1
b = ExampleClass(2, 8)  # unique ID=2

print(ExampleClass(1, 20).value)
print(ExampleClass(3, 0).value)
