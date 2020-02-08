def bouncingBall(h, bounce, window):
    import math
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    else:
        return math.floor(math.log10(window/h)/math.log10(bounce)) * 2 + 1