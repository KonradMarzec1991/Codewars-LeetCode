from itertools import groupby


def most_money(students):
    if len(students) == 1:
        return students[0].name
    d_money = {}
    for s in students:
        d_money[s.name] = s.fives * 5 + s.tens * 10 + s.twenties * 20
    groups = groupby(d_money.values())
    next(groups, None)
    if next(groups, None) is None:
        return 'all'
    return max(d_money.keys(), key=lambda k: d_money[k])


class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)
