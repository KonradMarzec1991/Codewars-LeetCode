def sqInRect(lng, wdth):
    if lng == wdth:
        return None

    result = []
    while lng != wdth:
        if lng > wdth:
            lng -= wdth
            result.append(wdth)
        else:
            wdth -= lng
            result.append(lng)
    result.append(wdth)
    return result
