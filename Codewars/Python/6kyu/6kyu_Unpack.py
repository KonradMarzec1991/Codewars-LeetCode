def unpack(l):
    output = []
    for item in l:
        if isinstance(item, (list, set, tuple)):
            output += unpack(item)
        elif isinstance(item, dict):
            output += unpack(item.keys())
            output += unpack(item.values())
        else:
            output += [item]
    return output
