def add(n):
    def wrapper(m):
        return m + n
    return wrapper


# other solution
def add2(n):
    return lambda x: x + n
