def delete_nth(order, max_e):
    arr = []
    for val in order:
        if arr.count(val) >= max_e:
            continue
        else:
            arr.append(val)
    return arr


print(delete_nth([20,37,20,21], 1))
print(delete_nth([1,1,3,3,7,2,2,2,2], 3))
print(delete_nth([1, 2, 3, 1, 1, 2, 1, 2, 3, 3,  2, 4, 5, 3, 1], 3))