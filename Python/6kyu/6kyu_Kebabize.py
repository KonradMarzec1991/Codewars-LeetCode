import re


def kebabize(string):

    string = re.sub('[0-9]', '', string)
    string = string[:1].lower() + string[1:]

    for x in string:
        if x.isupper():
            s = "-" + x.lower()
            string = string.replace(x, s)

    return string


print(kebabize('myCamelCased33String'))
print(kebabize('SOS'))
print(kebabize('42'))
print(kebabize('Codewars'))
