import unittest
from deck.drawpile import Drawpile
from deck.deck import Deck

class TestDrawpile(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.drawpile = Drawpile(self.deck)

    def test_update_empty_drawpile(self):
        for i in range(52):
            self.deck.draw_card()
        
        s, word = self.drawpile.update()
        self.assertEqual(word, "empty_draw")

    def test_update_nonempty_pile(self):
        s, word = self.drawpile.update()
        self.assertEqual(word, "draw")