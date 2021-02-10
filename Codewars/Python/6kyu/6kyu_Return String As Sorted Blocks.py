def blocks(s):
    import string
    modified = string.ascii_letters + '0123456789'
    sorter = lambda arr: sorted(arr, key=modified.index)
    result, duplicates, s = '', [], sorter(list(s))
    for sign in s:
        if sign not in result:
            result += sign
        else:
            duplicates.append(sign)
    duplicates = ''.join(duplicates)
    if duplicates:
        return result + '-' + blocks(duplicates)
    return result