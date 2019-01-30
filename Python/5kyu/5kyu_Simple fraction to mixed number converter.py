from fractions import Fraction
from math import floor


def mixed_fraction(s):

    arr = s.split("/")
    threshold = 10 ** 7

    if len(arr) == 1:
        return str(arr[0])

    if arr[1] == 0:
        raise ZeroDivisionError('Divide by 0!')

    if threshold < int(arr[0]) < -threshold or threshold < int(arr[1]) < -threshold:
        return 'Wrong input'

    is_ngtv = False

    if (int(arr[0]) < 0 and int(arr[1]) > 0) or (int(arr[0]) > 0 and int(arr[1]) < 0):
        is_ngtv = True

    arr[0] = abs(int(arr[0]))
    arr[1] = abs(int(arr[1]))

    if arr[0] % arr[1] == 0:
        if is_ngtv:
            return str(-int(arr[0]/arr[1]))
        else:
            return str(int(arr[0] / arr[1]))

    full = floor(arr[0]/arr[1])
    if full < 1:
        if is_ngtv:
            return f'-{str(Fraction(arr[0], arr[1]))}'
        else:
            return f'{str(Fraction(arr[0], arr[1]))}'

    arr[0] = arr[0] - full * arr[1]

    if is_ngtv:
        return f'-{str(full)} {str(Fraction(arr[0], arr[1]))}'
    else:
        return f'{str(full)} {str(Fraction(arr[0], arr[1]))}'


print(mixed_fraction('-6/3'))