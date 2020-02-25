class UnexpectedTypeException(Exception):
    pass


def expected_type(type_arr):
    def decorator(func):
        def wrapper(*args, **kwargs):
            val = func(*args, **kwargs)
            if not isinstance(val, type_arr):
                raise UnexpectedTypeException
            return val

        return wrapper

    return decorator