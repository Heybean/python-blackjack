'''
Main game script
'''
from player import Player
from hand import Hand
from deck import Deck
import math

def ask_bet(player):
    '''
    Ask player to enter a bet and returns the betting amount
    '''
    while True:
        try:
            print('\nCurrent bank: $', player.bank)
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

def deal_cards(deck, hand, n = 1):
    '''
    Deals a number of cards to a hand.
    INPUT
        deck = cards to draw from
        hand = hand to deal to
        n = number of cards to deal from the deck. Default of 1 if no value given
    '''

    for _ in range(0, n):
        hand.add_card(deck.deal())

def displayStatus(dealerHand, playerHand, bet, hideOne):
    '''
    Displays hand status from both hands to console
    dealerHand = dealer's hand
    playerHand = player's hand
    bet = current bet value
    hideOne = If True, will hide one of the dealer's cards
    '''
    print('-'*15)
    print("Dealer's hand:")
    dealerHand.display(hideOne)
    if not hideOne:
        print(f'Hand value: {dealerHand.value()}')
    print("\nPlayer's hand:")
    playerHand.display()
    print(f'Hand value: {playerHand.value()}')
    print(f'\nCurrent bet: ${bet}')

def dealing(deck, dealerHand, playerHand, bet):
    '''
    Handles player hit or stand.
    Returns -1 if player has busted. Returns 0 if player chose to stand
    '''
    while True:
        displayStatus(dealerHand, playerHand, bet, True)

        inp = input('Do you wish to HIT or STAND? ').lower()
        if (inp == 'hit'):
            playerHand.add_card(deck.deal())

            # BUST or Auto STAND
            value = playerHand.value()
            if (value > 21):
                return -1
            elif (value == 21):
                return 0

            continue
        elif (inp == 'stand'):
            return 0

def play_dealer_hand(deck, dealerHand, playerHand):
    '''
    Play the dealer's hand until at least 17 or BUST.
    Returns Values:
    2 = player won (2 card blackjack)
    1 = player won
    0 = tie
    -1 = dealer won
    '''
    value = dealerHand.value()
    playerValue = playerHand.value()
    # Special cases
    if (playerValue == 21):
        if (value == 21) and (len(playerHand.cards) == 2):
            # Both have natural blackjacks, tie
            return 0
        elif (value == 21) and (len(playerHand.cards) > 2):
            # Dealer has natural blackjack
            return -1
        else:
            # Player has natural blackjack
            return 2

    # Auto play dealer hand until >= 17
    while (value <= 17):
        dealerHand.add_card(deck.deal())
        value = dealerHand.value()

    if (value > 21) or (playerValue > value):
        return 1

    if (value > playerValue):
        return -1

    return 0

def ask_play_again(player):
    '''
    Ask if player wants to play another hand.
    player = the player object
    Returns 1 if play another hand, 0 if quit
    '''
    while True:
        result = input('Do you wish to play another hand? Yes or No. ').lower()
        if (result == 'yes'):
            return 1
        elif (result == 'no'):
            return 0
        else:
            print('Invalid input! Please enter Yes or No.')


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

        deal_cards(deck, dealerHand, 2)
        deal_cards(deck, playerHand, 2)

        result = dealing(deck, dealerHand, playerHand, bet)

        if (result == 0):
            finalGameResult = play_dealer_hand(deck, dealerHand, playerHand)

            displayStatus(dealerHand, playerHand, bet, False)
            if (finalGameResult == 0):
                print('PUSH! Game ended in tie, wager returned.')
            elif (finalGameResult == -1):
                print('Dealer wins.')
                player.modify_bank(-bet)
            elif (finalGameResult == 1):
                print('You win!')
                player.modify_bank(bet)
            elif (finalGameResult == 2):
                print('Natural Blackjack! You win!')
                player.modify_bank(math.floor(bet * 0.5))
        else:
            # BUST
            displayStatus(dealerHand, playerHand, bet, False)
            print('BUST! You lost!')
            player.modify_bank(bet * -1)

        # No more money
        if (player.bank <= 0):
            print('Game Over! You lost all your money!')
            break
        elif (ask_play_again(player) == 0):
            break

    print(f'Final winnings: ${player.bank}')