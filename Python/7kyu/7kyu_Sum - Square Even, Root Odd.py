def sum_square_even_root_odd(nums):
    output = 0
    for item in nums:
        if item % 2 == 0:
            output += item ** 2
        else:
            output += item ** .5
    return round(output, 2)
