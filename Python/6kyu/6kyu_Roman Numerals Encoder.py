roman_letters = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
roman_values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
romans = dict(zip(roman_values, roman_letters))


def solution(n):

    if not isinstance(n, int):
        raise TypeError("Must be an integer!!!")

    if n > 4000 or n < 1:
        raise ValueError("Must be between 1 and 3999")

    if n in romans.keys():
        return romans[n]

    result = ""

    for x in sorted(romans, reverse=True):
        times = int(n/x)
        result += times * romans[x]
        n -= times * x

    return result


print(solution(1666))
