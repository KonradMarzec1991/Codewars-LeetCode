def num_primorial(n):
    import math

    def check_if_prime(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    counter, index, mult = 2, 0, 1
    while index != n:
        if check_if_prime(counter):
            index += 1
            mult *= counter
        counter += 1
    return mult

