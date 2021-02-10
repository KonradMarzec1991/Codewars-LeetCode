def get_bingo_card():
    from random import sample
    down, up, result = 1, 16, []
    for item in zip('BINGO', [5, 5, 4, 5, 5]):
        some = sample(range(down, up), item[1])
        for s in some:
            result.append(item[0] + str(s))
        down = up
        up += 15
    return result