import math


class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __add__(self, other):
        if isinstance(other, self.__class__):
            bottom = self.bottom * other.bottom
            top = self.top * other.bottom + self.bottom * other.top
            gcd = math.gcd(top, bottom)
            if gcd > 1:
                top = top // gcd
                bottom = bottom // gcd
            return Fraction(top, bottom)
        else:
            raise TypeError('Other is not a Fraction type!')

    def __repr__(self):
        return f'{self.top}/{self.bottom}'
