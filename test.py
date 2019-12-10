import unittest
from deck import Deck
from player import Player
from hand import Hand
from card import Card
import game

class Test(unittest.TestCase):

    def test_deck_create(self):
        deck = Deck()
        count = len(deck.cards)
        self.assertEqual(count, 52)

    def test_card_print(self):
        deck = Deck()
        text = str(deck.cards[0])
        self.assertEqual(text, '1 of Hearts')

    def test_modify_player_bank(self):
        player = Player(100)
        player.modify_bank(50)
        self.assertEqual(player.bank, 150)

    def test_add_card(self):
        hand = Hand()
        card = Card(1, 'Hearts')

        hand.add_card(card)

        self.assertEqual(len(hand.cards), 1)

    def test_deal(self):
        hand = Hand()
        deck = Deck()

        game.deal_cards(deck, hand, 5)

        self.assertEqual(len(hand.cards), 5)
    
    #def test_ask_bet(self):
    #    player = Player(1000)
    #    amount = game.ask_bet(player)
    #    self.assertGreater(amount, 0)

if __name__ == "__main__":
    unittest.main()