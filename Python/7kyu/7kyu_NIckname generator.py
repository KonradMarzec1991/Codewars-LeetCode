def nickname_generator(name):
    import re
    if len(name) < 4:
        return "Error: Name too short"
    return name[:3] if re.match(r'^\w{2}[^aeiou]{1}', name) else name[:4]