import re


def kebabize(string):

    mystring = ""

    for x in string:
        if x == x.lower() and x.isalpha():
            mystring += x
        elif x == x.upper() and x.isalpha():
            mystring += '-' + x

    return mystring.strip('-').lower()


print(kebabize('myCamelCased33String'))
print(kebabize('SOS'))
print(kebabize('42'))
print(kebabize('Codewars'))
