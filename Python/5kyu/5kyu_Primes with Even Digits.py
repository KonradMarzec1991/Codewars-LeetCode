from math import sqrt


def f(n):
    top_prime, max_counter = 0, 0

    for i in range(n-1, 0, -1):

        if len(str(i)) <= max_counter + 1:
            break

        if is_prime(i):
            counter = sum(d in '02468' for d in str(i))
            if counter > max_counter:
                top_prime = i
                max_counter = counter
    return top_prime


def is_prime(n):
    if n % 2 == 0:
        return False
    for x in range(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True
