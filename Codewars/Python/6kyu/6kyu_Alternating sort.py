def alternate_sort(l):
    return sorted(l, key=abs)


print(alternate_sort([5, -42, 2, -3, -4, 8, -9,]))