def is_onion_array(a):
    length = len(a)//2
    for i in range(length):
        if a[i] + a[len(a) -i - 1] > 10:
            return False
    return True
