from collections import defaultdict


def cakes(recipe, available):
    av = defaultdict(lambda: 0, available)
    times = 0

    while True:
        for k, v in recipe.items():
            av[k] = av[k] - recipe[k]
            if av[k] < 0:
                return times
        times += 1


# Amazing solution from CodeWars
def cakes_alternative(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)
