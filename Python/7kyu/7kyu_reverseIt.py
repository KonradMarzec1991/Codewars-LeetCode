def reverse_it(data):
    type_ = type(data)
    return type_(str(data)[::-1]) if type_ in (str, int, float) else data
