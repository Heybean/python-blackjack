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
        '''
        Adds the card to the hand
        '''
        if (type(card) != Card):
            raise Exception('Invalid type. Must be of type Card')
        
        self.cards.append(card)

    def value(self):
        '''
        Calculates the total value of the hand for blackjack
        '''
        total = 0
        numOfAces = 0

        for card in self.cards:
            total += card.value()
            if (card.face == 14):
                numOfAces += 1

        # Determine if Aces is 11 or 1
        while (numOfAces > 0) and (total > 21):
            total -= 10
            numOfAces -= 1

        return total

    def display(self, hideOne = False):
        '''
        Prints the cards in hand.
        hideOne = Default is False. If set to True, one of the cards is displayed as 'hidden' (used for dealer)
        '''

        text = []
        for card in self.cards:
            text.append(str(card))

        if hideOne:
            text[0] = '?? Hidden ??'

        print('     ' + ', '.join(text))

