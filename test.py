import unittest
from deck import Deck

class Test(unittest.TestCase):

    def test_deck_create(self):
        deck = Deck()
        count = len(deck.cards)
        self.assertEquals(count, 52)

if __name__ == "__main__":
    unittest.main()