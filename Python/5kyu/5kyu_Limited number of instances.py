from collections import defaultdict


def limiter(limit, unique, lookup):
    print(limit, unique, lookup)
    instances = defaultdict(list)
    global_lookup = 0

    if lookup == 'LAST':
        global_lookup = -1
    if lookup == 'RECENT':
        global_lookup = -2

    def wrapper(cls):
        name = cls.__name__
        original__new__ = cls.__new__

        def other__new__(cls, *args, **kwargs):
            instance = original__new__(cls)
            instance.__init__(*args, **kwargs)

            for obj in instances[name]:
                if obj.__dict__[unique] == instance.__dict__[unique]:
                    return instances[name][global_lookup]

            if len(instances[name]) == limit:
                return instances[name][global_lookup]

            instances[name].append(instance)
            return instance

        cls.__new__ = other__new__
        return cls
    return wrapper


@limiter(2, "ID", "FIRST")
class ExampleClass:
    def __init__(self, ID, value):
        self.ID, self.value = ID, value
        print(self)


a = ExampleClass(1, 5)  # unique ID=1
b = ExampleClass(2, 8)  # unique ID=2

print(ExampleClass(1, 20).value)
print(ExampleClass(3, 0).value)
