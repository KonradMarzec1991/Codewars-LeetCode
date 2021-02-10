def next_higher(value):
    bin_val = bin(value)[2:].count('1')
    while True:
        value += 1
        if bin(value)[2:].count('1') == bin_val:
            return value
