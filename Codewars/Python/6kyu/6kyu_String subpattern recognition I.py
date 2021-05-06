def has_subpattern(string):
    import re
    return bool(re.search(r'(.*)\1+', string))
