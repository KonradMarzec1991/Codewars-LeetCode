def hex_string_to_RGB(hex_string):
    return {
        'r': int(hex_string[1:3], base=16),
        'g': int(hex_string[3:5], base=16),
        'b': int(hex_string[5:7], base=16),
    }