def uglify_word(s):
    flag = True
    output = ''
    for ch in s:
        if ch.isalpha():
            if flag:
                output += ch.upper()
            else:
                output += ch.lower()
            flag = not flag
        else:
            output += ch
            flag = True
    return output
