def string_task(s):
    import re
    s = re.sub(r'[eyuioaEYUIOA]', '', s).lower()
    return '.' + '.'.join(list(s)) if s else ''
