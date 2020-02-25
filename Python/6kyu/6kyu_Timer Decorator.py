def timer(seconds):
    import time

    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            finish = time.time()
            return finish - start < seconds
        return wrapper
    return decorator