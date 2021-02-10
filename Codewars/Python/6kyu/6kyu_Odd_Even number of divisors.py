def oddity(n):
    import math
    divisors = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if n/i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n/i)
        i += 1
    return 'odd' if len(divisors) % 2 == 1 else 'even'