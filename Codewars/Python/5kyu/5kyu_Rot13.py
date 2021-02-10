def rot13(message):
    from string import ascii_lowercase, ascii_uppercase
    letters = [ascii_uppercase * 2, ascii_lowercase * 2]
    which = lambda x: letters[0] if x.isupper() else letters[1]

    result = ''
    for item in message:
        if item.isalpha():
            item_index = which(item).index(item)
            result += which(item)[item_index + 13]
        else:
            result += item
    return result