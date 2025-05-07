import random, itertools

deck = list(itertools.product(range(1, 14), ['Hearts', 'Diamonds', 'Clubs', 'Spades']))
# deck = [str(i[0]) + " of " + i[1] for i in deck]
# deck = random.sample(deck, len(deck))
random.shuffle(deck)
for i in range(5):
    print(deck[i][0], "of", deck[i][1])