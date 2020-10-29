table = [['']]


def gen_balanced(n):
    if n < len(table):
        return table[n]

    result = []
    for i in range(n):
        for x in gen_balanced(i):
            for y in gen_balanced(n - i - 1):
                result.append('(' + x + ')' + y)

    table.append(result)
    return table[n]
