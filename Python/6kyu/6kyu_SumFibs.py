def sum_fibs(n):
    total = 0
    k, l = 0, 1

    while n > 0:
        k, l = l, k + l
        if k % 2 == 0:
            total += k
        n -= 1
    return total


print(sum_fibs(5))
print(sum_fibs(9))
