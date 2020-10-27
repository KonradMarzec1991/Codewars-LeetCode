def productFib(prod):
    k, l = 0, 1
    while True:
        fib = k * l
        if fib == prod:
            return [k, l, True]
        if fib > prod:
            return [k, l, False]
        k, l = l, k + l
