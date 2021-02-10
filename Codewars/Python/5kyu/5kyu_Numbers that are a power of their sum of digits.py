def power_sumDigTerm(n):
    def sum_digits(num):
        return sum(map(int, str(num)))
    arr = []
    for num in range(2, 400):
        for p in range(2, 50):
            comp = num ** p
            if sum_digits(comp) == num:
                arr.append(comp)
    arr.sort()
    return arr[n-1]