def remove_url_anchor(url):

    valid_url = ''
    for char in url:
        if not char == '#':
            valid_url += char
        else:
            break
    return valid_url
