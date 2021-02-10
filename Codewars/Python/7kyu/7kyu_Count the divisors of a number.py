def divisors(n):
    return len(set([x for x in range(2, int(n**.5)+1) if n % x == 0] + [n/x for x in range(2, int(n**.5)+1) if n % x == 0]))+2 if n > 1 else 1