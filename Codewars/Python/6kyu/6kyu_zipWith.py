def zip_with(fn, a1, a2):
    return [fn(*i) for i in zip(a1, a2)]
