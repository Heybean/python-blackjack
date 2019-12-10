'''
Module for deck of cards
'''
import random
from card import Card

class Deck():
    '''
    Holds a deck of standard 52 poker cards
    '''
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Spades', 'Clubs']:
            for x in range(1, 14):
                self.cards.append(Card(x, suit))
    def shuffle(self):
        '''
        Shuffles the deck of cards
        '''
        random.shuffle(self.cards)
    def deal(self):
        '''
        Deals the top card and removes it from the deck
        '''
        return self.cards.pop()
