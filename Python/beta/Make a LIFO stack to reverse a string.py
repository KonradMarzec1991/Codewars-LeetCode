# This one does not pass all tests from reason I do not know


class CWStack(object):

    def __init__(self):
        self.items = []

    @property
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items.pop()
        return item

    def top(self):
        if self.isEmpty():
            return None
        return self.items[len(self.items) - 1]

    def __str__(self):
        return 'Stack of size: {}'.format(self.size)


def reverse_str(s, stack):
    for letter in s:
        stack.append(letter)
        
    rString = ''

    while not s.isEmtpy():
        rString += stack.pop()
    return rString


