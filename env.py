from collections import namedtuple


class SpiderEnv:
    '''
    init Reward = 500
    remove column = 100
    move card = -1
    Max Reward = 1254
    min move = 46
    '''
    def __init__(self):
        self.Card = namedtuple('Card', ['value','suit'])
        self.suits = ['hearts','diamonds','spades','clubs']
        self.cards = [self.Card(value, suit) for value in range(1,14) for suit in self.suits]



env = Spade()
print(env.cards[0])
print(len(env.cards))