def count_change(money, coins):
    combinations = [0]*(money+1)
    combinations[0] = 1

    for coin in coins:
        for i in range(len(combinations)):
            if i >= coin:
                combinations[i] += combinations[i-coin]
    return combinations[money]
