import inspect


class LazyInit(type):
    def __new__(mcs, mcs_name, mcs_bases, mcs_dict):
        cls = super().__new__(mcs, mcs_name, mcs_bases, mcs_dict)
        print(inspect.getfullargspec(cls.__init__).args)
        return cls


class Person(metaclass=LazyInit):
    def __init__(self, name='abc', age=123):
        pass


p = Person()
