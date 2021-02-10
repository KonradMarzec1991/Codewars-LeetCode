class Primes:
    arr = []

    @classmethod
    def first(cls, rng):
        if rng <= len(cls.arr):
            return cls.arr[:rng]
        else:
            if cls.arr:
                starting_point = cls.arr[-1]
            else:
                starting_point = 0
            while len(cls.arr) < rng:
                starting_point += 1
                if cls.is_prime(starting_point):
                    cls.arr.append(starting_point)
            return cls.arr

    @staticmethod
    def is_prime(num):
        if num < 2:
            return False
        if num == 2 or num == 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
