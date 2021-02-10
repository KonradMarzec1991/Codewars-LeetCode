def expanded_form(num):
    if num <= 0:
        return None

    i = len(str(num)) - 1
    string_value = ""
    num_array = [int(d) for d in str(num)]
    for x in num_array:
        if x != 0:
            string_value += str(x * (10 ** i)) + " + "
        i -= 1
    return string_value[:len(string_value) - 3]