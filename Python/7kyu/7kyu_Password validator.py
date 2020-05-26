def password(string):
    import re
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$', string))
