def is_palindrome(num):
    return str(num) == str(num)[::-1]


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def find_primes(num):
    from math import sqrt
    divs = set()
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            while num % i == 0 and is_prime(i):
                num = num // i
            divs.add(i)
        i += 1
    if is_prime(num):
        divs.add(num)
    return divs


def same_factRev(nMax):
    result = [1089]
    if nMax < 1089:
        return []
    for i in range(1090, nMax + 1):
        if i % 3 == 0 and not is_palindrome(i) and not i % 10 == 0:
            rev = int(str(i)[::-1])
            if set(find_primes(i)) == set(find_primes(rev)):
                result.append(i)
    return result
