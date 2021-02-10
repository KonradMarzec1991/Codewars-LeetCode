def dashatize(num):
    import re
    if num is None:
        return 'None'
    num = abs(num)
    if num < 100:
        return str(num)
    num = str(num)
    s = ''
    for i in range(len(num)):
        val = int(num[i])
        if val % 2 == 0:
            s += num[i]
        else:
            s += '-' + num[i] + '-'
    return re.sub(r'\-\-', '-', s.strip('-'))



print(dashatize(274), "2-7-4", "Should return 2-7-4")
print(dashatize(5311), "5-3-1-1", "Should return 5-3-1-1")
print(dashatize(86320), "86-3-20", "Should return 86-3-20")
print(dashatize(974302), "9-7-4-3-02", "Should return 9-7-4-3-02")
print(dashatize(None), "None", "Should return None")
print(dashatize(0), "0", "Should return 0")
print(dashatize(-1), "1", "Should return 1")
print(dashatize(-28369), "28-3-6-9", "Should return 28-3-6-9")