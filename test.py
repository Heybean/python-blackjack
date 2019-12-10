import unittest
from deck import Deck
from player import Player

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

if __name__ == "__main__":
    unittest.main()