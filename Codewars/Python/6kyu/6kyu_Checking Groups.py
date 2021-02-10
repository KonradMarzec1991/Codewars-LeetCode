def group_check(s):
    lefty, righty, temp = '([{', ')]}', []
    for group in s:
        if group in lefty:
            temp.append(group)
        else:
            if len(temp) == 0:
                return False
            if righty.index(group) != lefty.index(temp.pop()):
                return False
    return len(temp) == 0
