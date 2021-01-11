def longest_slide_down(pyramid):
    last = pyramid.pop()
    while pyramid:
        after = pyramid.pop()
        last = [max(last[i], last[i+1]) + v for i, v in enumerate(after)]
    return last[0]
