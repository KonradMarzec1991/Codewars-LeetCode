def convertFracts(lst):
    denominator = 1
    for item in lst:
        denominator *= item[1]
    print(denominator)


print(convertFracts([[2, 7], [1, 3], [1, 12]]))