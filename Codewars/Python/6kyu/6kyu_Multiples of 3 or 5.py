def solution(number):
    i, count = 2, 0
    while i < number:
        if i % 3 == 0 or (i % 5 == 0 and i % 3 != 0):
            count += i
        i += 1
    return count
