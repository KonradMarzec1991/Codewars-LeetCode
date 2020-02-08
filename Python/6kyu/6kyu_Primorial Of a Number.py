def num_primorial(n):
    import math

    def check_if_prime(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    counter = 2
    index = 0
    mult = 1

    while index != n:
        if check_if_prime(counter):
            index += 1
            mult *= counter
        counter += 1

    return mult


print(num_primorial(3))
print(num_primorial(5))
print(num_primorial(6))

