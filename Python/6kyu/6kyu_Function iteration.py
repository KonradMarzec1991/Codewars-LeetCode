def create_iterator(func, n):
    def wrapper(result):
        for _ in range(n):
            result = func(result)
        return result
    return wrapper