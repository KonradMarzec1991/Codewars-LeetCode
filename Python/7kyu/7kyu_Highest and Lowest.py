def high_and_low(numbers):

    arr = [int(x) for x in numbers.split(" ")]
    return f'{max(arr)} {min(arr)}'


print(high_and_low('1554 2760 1822 712 2338 1241 638 461 1674 2321 -311 660 2105 330 1762 1131 115 2651 792 2563 1891 1681'))