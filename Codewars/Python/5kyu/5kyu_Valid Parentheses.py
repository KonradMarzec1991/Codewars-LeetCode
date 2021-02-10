def valid_parentheses(string):
    import re
    LPAREN = r'(?P<LPAREN>\()'
    RPAREN = r'(?P<RPAREN>\))'
    WS = r'(?P<WS>\s+)'
    LETTERS = r'(?P<LETTERS>\w+)'

    paren_count = 0
    master_pat = re.compile('|'.join([LPAREN, RPAREN, WS, LETTERS]))
    scanner = master_pat.scanner(string)

    for m in iter(scanner.match, None):
        if m.lastgroup == 'LPAREN':
            paren_count += 1
        elif m.lastgroup == 'RPAREN':
            paren_count -= 1
        if paren_count < 0:
            return False
    if paren_count != 0:
        return False
    return True


# Another solution
def parentheses_checker(mystr):

    class Stack:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return self.items == []

        def size(self):
            return len(self.items)

        def push(self, item):
            self.items.append(item)

        def pop(self):
            if self.is_empty():
                raise Empty('This is empty')
            return self.items.pop()

        def top(self):
            if self.is_empty():
                raise Empty('This is empty')
            return self.items[-1]

    class Empty(Exception):
        pass

    s = Stack()
    lefty = '([{'
    righty = '}])'

    for ch in mystr:
        if ch in lefty:
            s.push(ch)
        else:
            if s.is_empty():
                return False
            if righty.index(ch) != lefty.index(s.pop()):
                return False
    return s.is_empty()