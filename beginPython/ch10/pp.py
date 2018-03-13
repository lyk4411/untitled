from pip._vendor.distlib.compat import raw_input

values = list(range(1,11)) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v,s) for v in values for s in suits]
print(values)
print(suits)
print(deck)

from pprint import pprint
pprint(deck[:12])

from random import shuffle
shuffle(deck)
# pprint(deck[:12])

while deck:
    raw_input(deck.pop())