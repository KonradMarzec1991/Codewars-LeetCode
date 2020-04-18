def split_and_add(numbers, n):
    from itertools import zip_longest
    while n > 0:
        if len(numbers) == 1:
            return numbers
        x, y = numbers[:len(numbers)//2], numbers[len(numbers)//2:]
        nums = [i+j for i, j in zip_longest(x[::-1], y[::-1], fillvalue=0)]
        numbers = nums[::-1]
        n -= 1
    return numbers
