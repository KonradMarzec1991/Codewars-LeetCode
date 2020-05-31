def encode(st):
    return ''.join([
        char if char not in 'aeiou' else
        str('aeiou'.index(char)+1) for char in st
    ])


def decode(st):
    return ''.join([
        char if char not in '12345' else 'aeiou'[int(char)-1] for char in st
    ])
