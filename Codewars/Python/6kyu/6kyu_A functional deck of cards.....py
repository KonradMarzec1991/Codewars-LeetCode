deck_of_cards = lambda: [f'{x} of {y}' for x in 'ace two three four five six seven eight nine ten jack queen king'.split(' ') for y in 'hearts spades diamonds clubs'.split(' ')]
