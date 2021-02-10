def get_total_primes(a, b):
    import math
    import itertools

    def check_if_prime(num):
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                return False
        return True

    arr, result = [], []
    start, end = len(str(a)), len(str(b))
    for i in range(start, end + 1):
        for n in map(''.join, itertools.product('2357', repeat=i)):
            arr.append(int(n))
    for d in arr:
        if a <= d < b and check_if_prime(d):
            result.append(d)
    return len(result)
