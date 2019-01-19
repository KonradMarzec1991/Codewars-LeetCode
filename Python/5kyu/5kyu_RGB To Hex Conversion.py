def rgb(r, g, b):

    list_rgb = [dec_to_hex(r), dec_to_hex(g), dec_to_hex(b)]

    return "".join(list_rgb)


def dec_to_hex(num):

    if not (isinstance(num, int) and num > 0):
        return "00"

    if num < 0:
        return "00"

    if num < 10:
        return "0" + str(num)

    if num > 255:
        return "FF"

    hex_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    hex_array = []

    while num > 0:
        hex_value = hex_list[num % 16]
        hex_array.append(hex_value)
        num /= 16
        num = int(num)

    hex_array.reverse()

    return "".join(str(d) for d in hex_array)


print(rgb(-20,275,125))
