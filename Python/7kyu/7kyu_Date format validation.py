def date_checker(date):
    import re
    return bool(re.match(r'^\d{2}-\d{2}-\d{4}\s\d{2}:\d{2}$', date))