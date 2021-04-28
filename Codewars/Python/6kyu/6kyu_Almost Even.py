def split_integer(num, parts):
    how_much, rest = num//parts, num % parts
    return [how_much] * (parts - rest) + [how_much+1] * rest
