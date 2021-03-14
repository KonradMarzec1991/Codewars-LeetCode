def overload(*types):

    def decorator(func):
        print(func.__qualname__)

        def wrapper(*args, **kwargs):
            print(*args, **kwargs)
        return wrapper
    return decorator


@overload(int)
def analyse(x):
    print('X is an int!')


@overload(list)
def analyse(x):
    print('X is a list!')


print(analyse(2))
print(analyse([]))