from functools import wraps


class InvalidArgument(Exception):
    pass


def validate_args(*types_):

    def decorator(fn):
        @wraps(fn)
        def inner(*args):
            if not all(isinstance(item, types_) for item in args):
                raise InvalidArgument
            return fn(*args)
        return inner
    return decorator
