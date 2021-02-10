def sort_array(source_array):
    sorted_odds = sorted([d for d in source_array if d % 2 == 1])
    startpoint = 0

    for d in range(len(source_array)):
        if source_array[d] % 2 == 1:
            source_array[d] = sorted_odds[startpoint]
            startpoint += 1
    return source_array
