def longest(s):
    lgst, local = '', ''
    for ch in s:
        if local + ch == ''.join(sorted(local + ch)):
            local += ch
            continue
        else:
            if len(local) > len(lgst):
                lgst = local
            local = ch
    if len(local) > len(lgst):
        lgst = local
    return lgst