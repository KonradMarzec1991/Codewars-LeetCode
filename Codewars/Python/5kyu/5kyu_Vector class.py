def check_length(func):
    def inner(self, other):
        if len(self) != len(other):
            raise TypeError
        return func(self, other)
    return inner


class Vector:
    def __init__(self, arr):
        self._arr = arr

    def equals(self, other):
        if isinstance(other, self.__class__) and len(self) == len(other):
            return all(a == b for a, b in zip(self._arr, other._arr))
        return False

    @check_length
    def add(self, other):
        return Vector([a + b for a, b in zip(self._arr, other._arr)])

    @check_length
    def subtract(self, other):
        return Vector([a - b for a, b in zip(self._arr, other._arr)])

    @check_length
    def dot(self, other):
        return sum([a * b for a, b in zip(self._arr, other._arr)])

    def norm(self):
        return sum((x ** 2 for x in self._arr)) ** .5

    def __str__(self):
        return f'({",".join(map(str, self._arr))})'

    def __len__(self):
        return len(self._arr)
