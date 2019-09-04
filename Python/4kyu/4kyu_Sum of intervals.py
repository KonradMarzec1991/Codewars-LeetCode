def sum_of_intervals(intervals):
    numbers_in = []
    for interval in intervals:
        for i in range(interval[0], interval[1]):
            numbers_in.append(i)
    return len(set(numbers_in))