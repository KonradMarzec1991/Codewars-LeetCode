def is_valid_IP(strng):
    import re
    return bool(re.search(
        r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])\.){3}'
        r'((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9]))$',
        strng
    ))