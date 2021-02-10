def generateName():
    from random import sample
    from string import ascii_letters
    size = 6
    name = ''.join(sample(ascii_letters, size))
    if not photoManager.nameExists(name):
        return name