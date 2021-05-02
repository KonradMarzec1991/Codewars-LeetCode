from math import factorial as fact


def get_coefficient(n, k, a, c):
    return (a ** (n - k)) * fact(n) // fact(k) // fact(n - k) * (c ** k)


def expand(expr):
    base, pow = tuple(expr.split('^'))
    pow, base = int(pow), base[1:-1]
    if pow in (0, 1):
        return ('1', base)[pow]
    i = 0
    while not base[i].isalpha():
        i += 1
    name = base[i]
    val, const = tuple(base.split(name))
    if val in ('', '-'):
        val = ('1', '-1')[('', '-').index(val)]
    val, const, m = int(val), int(const), int(val) ** pow
    if const == 0:
        return f'{m if val else ""}{name}^{pow}'
    t = [f'{m if m not in (1, -1) else "-" if m < 1 else ""}{name}^{pow}']
    k = 1
    while k <= pow - 1:
        co = get_coefficient(pow, k, val, const)
        t.append(f'{co}{name}{"^" + str(pow - k) if pow - k > 1 else ""}')
        k += 1
    t.append(f'{const ** pow}')
    s = ['+' + t[i] if not t[i][0] == '-' else t[i] for i in range(1, len(t))]
    return t[0] + ''.join(s)
