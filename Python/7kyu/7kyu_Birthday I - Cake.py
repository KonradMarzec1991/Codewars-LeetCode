def cake(candles, debris):

    if not isinstance(candles, int):
        return 'Candles should be int!'

    if not isinstance(debris, str):
        return 'Debris must be a string!'

    value = 0

    for i, x in enumerate(debris):
        if i % 2 != 0:
            value += ord(x) - 97
        else:
            value += ord(x)

    if value > 0.7 * candles and candles:
        return "Fire!"
    else:
        return 'That was close!'
