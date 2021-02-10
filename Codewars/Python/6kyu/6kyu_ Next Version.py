def next_version(version):
    version_no_dots = version.replace('.', '')
    dots = len(version) - len(version_no_dots)
    increment = str(int(version_no_dots) + 1)
    zeros = len(version_no_dots) - len(increment)
    if not dots:
        return increment
    n_ver = increment[::-1] + '0' * zeros if zeros > 0 else increment[::-1]
    result, i = '', 0
    while dots:
        result += n_ver[i] + '.'
        i += 1
        dots -= 1
    return n_ver[i:][::-1] + result[::-1]