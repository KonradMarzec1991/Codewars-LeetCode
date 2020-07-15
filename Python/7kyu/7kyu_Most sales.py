def top3(products, amounts, prices):
    return [
        t[0] for t in sorted(list(zip(
        products,
        [t[0] * t[1] for t in zip(amounts, prices)])),
        key=lambda x: -x[1])
    ][:3]
