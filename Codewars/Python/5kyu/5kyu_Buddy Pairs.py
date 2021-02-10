def buddy(start, limit):
    import math

    def sum_divisors(n):
        arr = [1]
        for i in range(2, int(math.sqrt(n)+1)):
            if n % i == 0:
                arr.append(i)
                if i * i != n:
                    arr.append(n/i)
        return int(sum(arr))

    for i in range(start, limit + 1):
        val = sum_divisors(i) - 1
        if sum_divisors(val) - 1 == i and val > i:
            return [i, val]
    return 'Nothing'
