def elevator_distance(array):
    return sum([abs(array[i] - array[i + 1]) for i in range(len(array) - 1)])


print(elevator_distance([5,2,8]), 9)
print(elevator_distance([1,2,3]), 2)
print(elevator_distance([7,1,7,1]), 18)