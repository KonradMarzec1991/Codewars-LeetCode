import string


def is_pangram(s):
    d = dict.fromkeys(string.ascii_lowercase, 0)
    s_with_strings_only = [x.lower() for x in s if isinstance(x, str)]

    for x in s_with_strings_only:
        if x in d:
            d[x] += 1

    return False if any(value == 0 for value in d.values()) else True
