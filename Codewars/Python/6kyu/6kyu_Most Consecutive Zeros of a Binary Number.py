def max_consec_zeros(n):
    my_nums = {
        0: 'Zero', 1: 'One',
        2: 'Two', 3: 'Three',
        4: 'Four', 5: 'Five',
        6: 'Six', 7: 'Seven',
        8: 'Eight', 9: 'Nine',
        10: 'Ten', 11: 'Eleven',
        12: 'Twelve', 13: 'Thirteen'
    }
    n = bin(int(n))[2:]
    t_maximum, maximum = 0, 0
    for ch in n:
        if ch == '0':
            t_maximum += 1
        if ch == '1':
            t_maximum = 0
        if t_maximum > maximum:
            maximum = t_maximum
    return my_nums[maximum]