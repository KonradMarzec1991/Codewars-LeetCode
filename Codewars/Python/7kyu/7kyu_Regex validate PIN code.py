import re


def validate_pin(pin):
    if not pin.isdigit():
        return False
    return True if re.match(r'^\d{4}(\d{2})?$', pin) else False
