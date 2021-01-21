import abc


class DimensionsOutOfBoundError(Exception):
    pass


class AutoStorage:

    def __set_name__(self, owner, name):
        self.property_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)

    def __set__(self, instance, value):
        instance.__dict__[self.property_name] = value


class Validated(abc.ABC, AutoStorage):

    def __set__(self, instance, value):
        value = self.validate(value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, value):
        """Implement this method for descriptor"""
        return NotImplemented


class Quantity(Validated):
    def __init__(self, min_value, max_value):
        self._min = min_value
        self._max = max_value

    def validate(self, value):
        if value < self._min or value > self._max:
            raise DimensionsOutOfBoundError(
                f"Package {self.property_name}=={value} out of bounds, should be: {self._min} < {self.property_name} <= {self._max}")
        else:
            return value


class Package:
    length = Quantity(0, 350)
    width = Quantity(0, 300)
    height = Quantity(0, 150)
    weight = Quantity(0, 40)

    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    @property
    def volume(self):
        return self.length * self.width * self.height


p = Package(10, 12, 13, 20)
print(p.volume())