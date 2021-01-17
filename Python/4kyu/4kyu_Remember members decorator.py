class RememberMeta(type):
    def __new__(mcs, name, bases, cls_dict):
        return super().__new__(mcs, name, bases, cls_dict)

    def __call__(cls, *args):
        print(*args)


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
