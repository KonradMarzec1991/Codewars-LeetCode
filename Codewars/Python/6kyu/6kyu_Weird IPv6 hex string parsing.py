def parse_IPv6(iPv6):
    separator = iPv6[4]
    str_result = ''
    list_of_hexs = iPv6.split(separator)
    value = 0
    for item in list_of_hexs:
        for ch in item:
            value += int(ch, 16)
        str_result += str(value)
        value = 0
    return str_result
