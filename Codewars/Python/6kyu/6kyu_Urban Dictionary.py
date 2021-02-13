import re


class WordDictionary:
    def __init__(self):
        self.stocks = set()

    def add_word(self, word):
        self.stocks.add(word)

    def search(self, word):
        for stock in self.stocks:
            if re.search(f'^{word}$', stock):
                return True
        return False
