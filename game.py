'''
Main game script
'''
from player import Player

def ask_bet(player):
    while True:
        try:
            amount = int(input('How much do you wish to bet? '))
            if (amount <= 0):
                print('You must enter a value greater than 0.\n')
            elif (amount > player.bank):
                print('You do not have enough money!\n')
            else:
                return amount
        except:
            print('Please enter a valid whole number.\n')
            continue


if __name__ == "__main__":
    print('Welcome to Blackjack!')
    player = Player(1000)
    print(f'Your starting bank funds: ${player.bank}')
    while True:
        break