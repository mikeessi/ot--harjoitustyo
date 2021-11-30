import unittest
from deck.deck import Deck

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_correct_first_card(self):
        card = self.deck.cards[0]
        self.assertEqual(str(card), "0_0.png")

    def test_draw_card_nonempty_deck(self):
        card = self.deck.draw_card()
        self.assertEqual(str(card), "3_12.png")

    def test_draw_card_empty_deck(self):
        for i in range(52):
            self.deck.draw_card()
        card = self.deck.draw_card()
        self.assertEqual(card, None)