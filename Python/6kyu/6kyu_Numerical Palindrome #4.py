def palindrome(num):
    if type(num) != int or num < 0:
        return 'Not valid'
    if num <= 11:
        return 11
    def revs(num):
        return int(str(num)[::-1])
    rev = revs(num)
    if num == rev:
        return num

    inc = num
    dec = num
    while True:
        inc += 1
        if inc == revs(inc):
            return inc
        dec -= 1
        if dec == revs(dec):
            return dec