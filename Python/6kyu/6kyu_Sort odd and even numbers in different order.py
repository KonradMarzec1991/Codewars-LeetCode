def sort_array(a):
    even = sorted([x for x in a if x % 2 == 0])
    odds = sorted([x for x in a if x % 2 == 1], reverse=True)
    for i, v in enumerate(a):
        if a[i] % 2 == 0:
            a[i] = even.pop()
        else:
            a[i] = odds.pop()
    return a