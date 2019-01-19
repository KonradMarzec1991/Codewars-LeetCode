import numbers

def faulty_odometer(n):
    pass



num = 2003
BASE = '012356789'

for i, n in enumerate(str(num)[::-1]):
    print(i, n)
    print(BASE.index(n) * len(BASE) ** i)