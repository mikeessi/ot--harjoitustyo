import unittest
from deck.discardpile import DiscardPile
from deck.deck import Deck
from deck.card import Card

class TestDiscardPile(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.discardpile = DiscardPile(self.deck)

    def test_dragged_card_empty_pile(self):
        card = self.discardpile.dragged_card()
        self.assertEqual(card, None)

    def test_dragged_card_nonempty_pile(self):
        self.deck.draw_card()
        card = self.discardpile.dragged_card()
        self.assertEqual(str(card), "3_12.png")
