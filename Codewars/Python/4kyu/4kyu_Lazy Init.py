import inspect


class LazyInit(type):
    def __call__(cls, *args, **kwargs):
        cls = super().__call__(*args, **kwargs)
        for n, v in zip(inspect.getfullargspec(cls.__init__).args[1:], args):
            cls.__setattr__(n, v)
        return cls
