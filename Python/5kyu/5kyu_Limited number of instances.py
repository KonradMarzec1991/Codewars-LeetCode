from collections import defaultdict


class Meta(type):
    def __call__(cls, *args, **kwargs):
        obj = super().__call__(*args, **kwargs)
        print(*args, **kwargs)
        print(type(obj))
        return obj


def limiter(limit, unique, lookup):
    print(limit, unique, lookup)
    instances = defaultdict(list)

    def wrapper(cls):
        print(cls.__name__)

        return Meta(
            cls.__name__,
            cls.__bases__,
            dict(cls.__dict__)
        )
    return wrapper


@limiter(2, "ID", "FIRST")
class ExampleClass:
    def __init__(self, ID, value): self.ID, self.value = ID, value


a = ExampleClass(1, 5)  # unique ID=1
b = ExampleClass(2, 8)  # unique ID=2

# ExampleClass(1, 20).value == 5
# ExampleClass(3, 0).value  == 5
