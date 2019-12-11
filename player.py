'''
Module for player
'''
class Player():
    '''
    Player interface.

    Bank is how much money the player has remaining
    '''

    def __init__(self, bank):
        self.bank = bank

    def modify_bank(self, amount):
        '''
        Modifies the player's bank by the amount. Positive for gain, negative for loss
        '''
        text = ''
        self.bank += amount
        if (amount > 0):
            text = f'You gained ${amount}.'
        elif (amount < 0):
            text = f'You lost ${-amount}.'

        print(f'{text} Current bank: ${self.bank}')