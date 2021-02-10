class Person:

    def __init__(self, name):
        self.name = name

    def greet(self, sb_name):
        return f'Hello {sb_name}, my name is {self.name}'
