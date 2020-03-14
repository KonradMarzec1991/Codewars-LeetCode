def jsonattr(filepath):
    import json
    with open(filepath, 'r') as f:
        j_data = json.load(f)

    def wrapper(cls):
        for key, value in j_data.items():
            setattr(cls, key, value)
        return cls
    return wrapper
