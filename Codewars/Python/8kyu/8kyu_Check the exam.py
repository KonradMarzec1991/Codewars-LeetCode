def check_exam(arr1, arr2):
    s = 0
    for x, y in zip(arr1, arr2):
        if y != '':
            if x == y:
                s += 4
            else:
                s -= 1
    return max(s, 0)


# nice answer from CW
def check_exam_1(arr1, arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))
