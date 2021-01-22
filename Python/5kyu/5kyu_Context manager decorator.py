class Manager:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def contextmanager(f):
    def wrapper(*args, **kwargs):
        return Manager(f(*args, **kwargs))
    return wrapper
