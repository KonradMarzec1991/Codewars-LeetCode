class RememberMeta(type):
    instances = {}

    def __call__(cls, *args):
        existing_instance = RememberMeta.instances.get(tuple(args), None)
        print(existing_instance)
        if existing_instance is None:
            RememberMeta.instances[tuple(args)] = super().__call__(*args)
        return RememberMeta.instances[tuple(args)]


def remember(cls):
    return RememberMeta(
        cls.__name__,
        cls.__bases__,
        dict(cls.__dict__)
    )


@remember
class A:
   def __init__(self, x, y=0, z=0):
     pass


a = A(1)
b = A(2, 3)
c = A(4, 5, 6)
d = A(1)
