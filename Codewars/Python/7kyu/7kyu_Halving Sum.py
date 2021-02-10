def halving_sum(n):
    s = n
    while n:
        s += n//2
        n //= 2
    return s


print(halving_sum(25))