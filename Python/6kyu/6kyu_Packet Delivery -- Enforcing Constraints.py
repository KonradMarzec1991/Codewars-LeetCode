import abc


class AutoStorage:
    def __init__(self, min_value, max_value):
        self._min = min_value
        self._max = max_value

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
        instance.__dict__[self.property_name] = value

    @abc.abstractmethod
    def validate(self, value):
        """Implement this method for descriptor"""
        return NotImplemented


class Package:
    length =
    width =
    height =
    weight =


    def __init__(self, length, width, height, weight):
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight

    def volume(self):
        return self.length * self.width * self.height

