def pos_average(s):
    arr = s.split(', ')
    counter, counter_2= 0, 0
    for i in zip(*arr):
        j = 0
        while j < len(i):
            current, *rest = i[j:]
            if rest:
                for k in rest:
                    counter_2 += 1
                    if k == current:
                        counter += 1
            j += 1
    return round(counter / counter_2 * 100, 10)
