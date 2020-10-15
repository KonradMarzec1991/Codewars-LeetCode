def even_chars(st):
    if len(st) < 2 or len(st) > 100:
        return "invalid string"
    else:
        return [v for i, v in enumerate(st, 1) if i % 2 == 0]
