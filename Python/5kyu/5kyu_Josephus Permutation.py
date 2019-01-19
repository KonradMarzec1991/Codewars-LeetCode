def josephus(items,k):
    num = -1
    my_list = []

    while len(items) > 0:
        num = (num + k) % len(items)
        my_list.append(items[num])
        items.pop(num)
        num -= 1

    return my_list


print(josephus([1, 2, 3, 4, 5, 6, 7], 3))