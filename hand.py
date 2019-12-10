'''
Module for managing cards in hand
'''

from card import Card

class Hand():
    '''
    Starts with an empty hand of cards.
    '''
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if (type(card) != Card):
            raise Exception('Invalid type. Must be of type Card')
        
        self.cards.append(card)

