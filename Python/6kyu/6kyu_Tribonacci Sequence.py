def tribonacci(signature, n):

    if n == 0:
        return []

    if n <= 3:
        return signature[:n]

    a = signature[0]
    b = signature[1]
    c = signature[2]

    n_array = []

    n_array.append(a)
    n_array.append(b)
    n_array.append(c)

    i = 3
    while i < n:

        val = sum(n_array[-3:])
        n_array.append(val)
        i += 1

    return n_array