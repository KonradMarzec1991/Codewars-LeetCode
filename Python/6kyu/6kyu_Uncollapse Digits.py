def uncollapse(digits):
    import re
    return ' '.join(re.findall(r'one|two|three|four|five|six|seven|eight|nine|zero', digits))