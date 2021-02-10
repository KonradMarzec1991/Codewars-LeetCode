# backwardsPrime is renamed backwards_prime
def backwards_prime(start, stop):
    def check_if_prime(num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False

        i = 5
        while i*i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    arr = []
    if start < 13:
        start = 13
    for i in range(start, stop + 1):
        rev = int(str(i)[::-1])
        if rev != i and check_if_prime(i) and check_if_prime(rev):
            arr.append(i)
    return arr
