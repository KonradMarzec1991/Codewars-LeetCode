def solution(string, markers):
    rows = string.split('\n')
    for marker in markers:
        for v in range(len(rows)):
            if marker in rows[v]:
                rows[v] = rows[v][:rows[v].index(marker)].rstrip()
            else:
                continue
    return '\n'.join(rows)
