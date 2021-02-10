def more_zeros(s):
    s = dict.fromkeys(s)
    arr, final = [bin(ord(ch))[2:] for ch in s], []
    for num in arr:
        if num.count('0') > num.count('1'):
            final.append(chr(int(num, 2)))
    return final