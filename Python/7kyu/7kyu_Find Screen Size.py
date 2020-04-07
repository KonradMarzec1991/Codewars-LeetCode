def find_screen_height(width, ratio):
    import functools
    return f'{width}x{int(width * functools.reduce(lambda x, y: y/x, map(int, ratio.split(":"))))}'