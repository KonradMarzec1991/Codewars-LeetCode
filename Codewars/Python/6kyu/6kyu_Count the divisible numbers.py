def divisible_count(x,y,k):
    if x % k == 0:
        return y//k - x//k + 1
    return y//k - x//k