def recycle(a):
    paper = []
    glass = []
    organic = []
    plastic = []

    for item in a:
        name = item['type']
        locals().get(item['material']).append(name)
        if 'secondMaterial' in item:
            locals().get(item['secondMaterial']).append(name)
    return paper, glass, organic, plastic


a = [
    {"type": "rotten apples", "material": "organic"},
    {"type": "out of date yogurt", "material": "organic", "secondMaterial": "plastic"},
    {"type": "wine bottle", "material": "glass", "secondMaterial": "paper"},
    {"type": "amazon box", "material": "paper"},
    {"type": "beer bottle", "material": "glass", "secondMaterial": "paper"}
]

print(recycle(a))