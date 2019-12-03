# Progressive Spiral Number Position
def layers(n):
    val = 1
    counter = 1
    iteration = 1
    while val < n:
        counter += 2
        iteration += 1
        val = counter * counter
    return iteration