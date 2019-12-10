'''
Module for standard poker card
'''

class Card():
    '''
    Holds info for a single poker card.
    Face is an integer from 1-14. 11-13 are JQK, and 14 is A
    Suit is Hearts, Diamonds, Spades, or Clubs
    '''

    faces = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
    values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)    # Values apply to Blackjack

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
    def __str__(self):
        return f'{Card.faces[self.face-1]} of {self.suit}'
    def value(self):
        '''
        Returns the numerical value of the card
        '''
        return Card.values[self.face-1]
