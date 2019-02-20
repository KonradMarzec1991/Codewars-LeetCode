def first_non_repeating_letter(string):
    
    if not isinstance(string, str):
        return ""

    if len(string) == 1:
        return string

    for letter in string:
        if_duplicate = string.lower().count(letter.lower())

        if if_duplicate == 1:
            return letter
            break

    return ""