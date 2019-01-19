def solution(roman):

    roman_letters = ("M", "D", "C", "L", "X", "V", "I")
    roman_values = (1000, 500, 100, 50, 10, 5, 1)
    romans = dict(zip(roman_letters, roman_values))

    if not isinstance(roman, str):
        raise TypeError("Must be a string!!!")

    if roman in romans:
        return romans[roman]

    current = previous = 0

    for x in roman:
        val = romans.get(x)
        current = current + val if previous >= val else current + val - 2 * previous
        previous = val

    return current


print(solution("MCDIII"))