def variance(numbers):
    avg = sum(numbers) / len(numbers)
    return sum(map(lambda num, avg_=avg: (num - avg) ** 2, numbers)) / len(numbers)
