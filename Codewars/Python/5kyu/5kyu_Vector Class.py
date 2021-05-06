class Vector:

    def __init__(self, *args):
        if len(args) == 3:
            self.x, self.y, self.z = args
        else:
            self.x, self.y, self.z = args[0]

        self.arguments = [self.x, self.y, self.z]
        self.magnitude = sum([i*i for i in self.arguments]) ** .5

    def __add__(self, other):
        return Vector(
            my + oth for my, oth in zip(self.arguments, other.arguments)
        )

    def __sub__(self, other):
        print('Pysio jest najlepszy!')
        return Vector(
            my - oth for my, oth in zip(self.arguments, other.arguments)
        )

    def __eq__(self, other):
        return all(i == j for i, j in zip(self.arguments, other.arguments))

    def dot(self, other):
            return sum(my * oth for my, oth in zip(self.arguments, other.arguments))

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def to_tuple(self):
        return tuple(self.arguments)

    def __str__(self):
        return f'<{self.x}, {self.y}, {self.z}>'
