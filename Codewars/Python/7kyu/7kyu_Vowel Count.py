import re


def getCount(inputStr):
    return len(re.findall('a|e|u|i|o', inputStr))




print(getCount("aa3tfweg"))