def remove_parentheses(s):
    counter = 0
    new_string = ''
    for ch in s:
        if ch == '(':
            counter += 1
        if ch == ')':
            counter -= 1
            continue

        if not counter:
            new_string += ch
    return new_string
