from collections import namedtuple
import random 
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
            self.order = ['K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2, 'A']
            self.cards = self.order*8
            random.shuffle(self.cards)
            self.move = 0
            self.hide_board = []
            self.view_board = []
            for _ in range(44):
                self.hide_board.append(self.cards.pop())
            for _ in range(10):
                self.view_board.append(self.cards.pop())
        '''
        self.Card = namedtuple('Card', ['value','suit'])
        self.suits = ['hearts','diamonds','spades','clubs']
        self.cards = [self.Card(value, suit) for value in range(1,14) for suit in self.suits]
        '''

    def draw(self):



env = SpiderEnv()
print(env.hide_board)
print(env.view_board)