'''
Main game script
'''
from player import Player
from hand import Hand
from deck import Deck

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
        bet = ask_bet(player)

        deck = Deck()
        deck.shuffle()

        dealerHand = Hand()
        playerHand = Hand()

        # No more money
        if (player.bank <= 0):
            break
        break
    else:
        print(f'Game is over. Final amount: ${player.bank}')