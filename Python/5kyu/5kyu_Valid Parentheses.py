import re


def valid_parentheses(string):

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