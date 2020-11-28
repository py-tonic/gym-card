from collections import namedtuple

'''
num of cards 13x8 = 104
columns = 10
get cards = 5xcolumns = 50
init cards = 54
random drow 'n' rows
simultaneously move if num is continuous
Draw one card in n columns
Erase when Ace to King is completed
'''

class SpiderEnv:
    '''
    init Reward = 500
    remove column = 100
    move card = -1
    Max Reward = 1254
    min move = 46
    '''
    def __init__(self, mode='easy'):
        if mode is 'easy':
            self.cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']*8
            self.move = 0
        '''
        self.Card = namedtuple('Card', ['value','suit'])
        self.suits = ['hearts','diamonds','spades','clubs']
        self.cards = [self.Card(value, suit) for value in range(1,14) for suit in self.suits]
        '''


env = SpiderEnv()
print(env.cards)