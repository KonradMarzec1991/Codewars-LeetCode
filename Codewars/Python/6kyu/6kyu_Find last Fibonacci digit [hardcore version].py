def generator(num):
    arr = []
    k, l = 1, 1
    for i in range(num):
        arr.append(int(str(k)[-1]))
        k, l = l, k + l
    return arr


def find_patter():
    # returns 60
    arr = generator(1000)
    i = 2
    while True:
        a = arr[:i]
        b = arr[i:i+len(a)]
        if a == b:
            return i
        i += 1


def last_fib_digit(n):
    arr = generator(60)
    return arr[n % 60 - 1]