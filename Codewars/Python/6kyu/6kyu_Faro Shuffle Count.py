def faro_cycles(deck_size):

    class Faro:
        def __init__(self, deck):
            self.deck = self.initialize_deck(deck)
            self.new_deck = [None] * len(self.deck)
            self.counter = 0

        @staticmethod
        def initialize_deck(nums):
            return [num for num in range(1, nums+1)]

        def shuffle(self):
            p1 = self.deck[:len(self.deck)//2]
            p2 = self.deck[len(self.deck)//2:]
            self.new_deck[::2] = p1
            self.new_deck[1::2] = p2

            self.deck = self.new_deck
            self.counter += 1

        def is_equal(self, deck_size):
            return self.deck == deck_size

    faro = Faro(deck_size)
    faro.shuffle()
    deck_equal = faro.initialize_deck(deck_size)

    while not faro.is_equal(deck_equal):
        faro.shuffle()
    return faro.counter
