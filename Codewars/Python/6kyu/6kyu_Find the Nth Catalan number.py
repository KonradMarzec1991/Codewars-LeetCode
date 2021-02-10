def nth_catalan_number(n):
    from math import factorial
    return int(factorial(2*n)//(factorial(n+1)*factorial(n))) if n > 0 else 1