def prefill(n, v=None):
    try:
        n = int(n)

        if v is None:
            return None

        if n == 0:
            return []

        return n * [v]
    except (ValueError, TypeError):
        raise TypeError(f'{n} is invalid')
