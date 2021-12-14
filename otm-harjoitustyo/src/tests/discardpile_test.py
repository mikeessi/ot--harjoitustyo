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

    def test_update_correct_value_when_empty(self):
        value = self.discardpile.update()
        self.assertEqual(value, (None, "discard"))

    def test_update_correct_value_when_nonempty(self):
        self.deck.draw_card()
        card, s = self.discardpile.update()
        self.assertEqual((str(card), s), ("3_12.png", "discard"))
