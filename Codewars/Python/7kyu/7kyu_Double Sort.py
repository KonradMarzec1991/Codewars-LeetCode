# def db_sort(arr):
#     return sorted([num for num in arr if isinstance(num, int)]) + \
#     sorted([num for num in arr if isinstance(num, str)]





arr = ['Banana', "Orange", "Apple", "Mango", 0, 2, 2]
print(sorted([num for num in arr if isinstance(num, int)]) + sorted([num for num in arr if isinstance(num, str)]))