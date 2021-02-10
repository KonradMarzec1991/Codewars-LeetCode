from functools import wraps


class InvalidArgument(Exception):
    pass


# function decorator
def validate_args(*types_):

    def decorator(fn):
        @wraps(fn)
        def inner(*args):
            if not all(isinstance(item, types_) for item in args):
                raise InvalidArgument
            return fn(*args)
        return inner
    return decorator


# class decorator
class validate_args_cls:
    def __init__(self, *types_):
        self.types_ = types_

    def __call__(self, fn):
        def inner(*args):
            if not all(isinstance(item, self.types_) for item in args):
                raise InvalidArgument
            return fn(*args)
        return inner
