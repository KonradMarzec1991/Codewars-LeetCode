import string


def find_missing_letter(chars):

    alphabet = string.ascii_letters
    start_point = alphabet.index(chars[0])

    find_letter = ""
    i = 0

    while start_point < start_point + len(chars):
        if chars[i] == alphabet[start_point]:
            start_point += 1
            i += 1
            continue
        else:
            find_letter = alphabet[start_point]
            break

    return find_letter
