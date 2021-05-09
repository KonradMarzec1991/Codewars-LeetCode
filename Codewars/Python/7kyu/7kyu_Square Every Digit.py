def square_digits(num):
    s = ""
    lista = [int(d) for d in str(num)]
    for element in lista:
        s += str(element ** 2)
    return int(s)
