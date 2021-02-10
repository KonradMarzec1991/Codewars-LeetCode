def reverse_factorial(num):

    if not isinstance(num, int):
        return 'Should be int!'

    if num < 0:
        return 'Negative value!'

    if num == 0 or num == 1:
        return '1!'

    counter = 1
    factorial = 1

    while num > factorial:
        counter += 1
        factorial *= counter

        if num == factorial:
            return f'{counter}!'

    return 'None'