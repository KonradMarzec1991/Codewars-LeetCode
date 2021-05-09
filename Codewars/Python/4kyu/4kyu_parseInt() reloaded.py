nums = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90,
}


def parse_int(string):
    values = string.split(" ")
    temp = 0
    temp_2 = 0
    for value in values:
        if value in nums:
            temp += nums[value]
            continue
        if value == 'hundred':
            temp *= 100
            continue
        if value == 'thousand':
            temp *= 1000
            temp_2, temp = temp, 0
            continue
        if value == "million":
            temp *= 1000000
            continue
        if '-' in value:
            twenties, ones = value.split('-')
            temp += nums[twenties] + nums[ones]
    return temp_2 + temp
