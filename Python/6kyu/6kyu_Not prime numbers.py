def is_prime(n):
    for i in range(2, int(n ** .5 + 1)):
        if n % i == 0:
            return False
    return True


def has_primes(n):
    if set('2357') >= set(str(n)):
        return True
    return False


def not_primes(a, b):
    a = 22 if a < 22 else a
    b = 7778 if b > 7777 else b
    return [i for i in range(a, b) if has_primes(i) and not is_prime(i)]