def is_letter(s):
    import re
    return bool(re.fullmatch(r'^[a-zA-Z]$', s))
