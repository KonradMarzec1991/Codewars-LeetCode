def namelist(names):
    if len(names) == 0:
        return ""
    if len(names) == 1:
        return names[0]['name']
    if len(names) == 2:
        return names[0]['name'] + " & " + names[1]['name']

    names = [d['name'] for d in names]
    output = ""
    for name in names:
        if names.index(name) == 0:
            output += name
        elif names.index(name) == len(names) - 1:
            output += " & " + name
        else:
            output += ", " + name
    return output

