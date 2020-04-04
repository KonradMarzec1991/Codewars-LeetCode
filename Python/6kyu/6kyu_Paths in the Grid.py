def number_of_routes(m, n):
    from math import factorial
    return factorial(m+n)//(factorial(m)*factorial(n))