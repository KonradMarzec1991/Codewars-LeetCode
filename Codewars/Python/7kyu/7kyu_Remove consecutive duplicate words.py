def remove_consecutive_duplicates(s):
    import re
    return re.sub(r'\b(\w+)( \1\b)+', r'\1', s)
