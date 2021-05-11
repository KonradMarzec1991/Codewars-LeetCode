def convertFracts(lst):
    denominator = 1
    for item in lst:
        denominator *= item[1]
    print(denominator)
