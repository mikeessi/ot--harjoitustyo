import unittest
from deck.card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        pass

    def test_correct_color_black(self):
        card = Card(1,3)
        self.assertEqual(card.color, "Black")

    def test_correct_color_red(self):
        card = Card(1,2)
        self.assertEqual(card.color, "Red")

    def test_correct_repr(self):
        card = Card(1,2)
        self.assertEqual(str(card), "2_1.png")