def validate_time(time):
    import re
    return bool(re.match(r'^[01]?[0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]$', time))
