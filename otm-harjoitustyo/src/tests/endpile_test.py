import unittest
from deck.endpile import Endpile
from deck.card import Card
from deck.deck import Deck
from deck.draggedcard import DraggedCard

class TestEndpile(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.endpile = Endpile(1, self.deck)

    def test_endpile_update_empty_pile(self):
        val1, val2 = self.endpile.update()
        self.assertEqual(val1, None)

    def test_endpile_update_nonempty_pile(self):
        self.endpile.pile.append(Card(1,3))
        val1, val2 = self.endpile.update()
        self.assertEqual(str(val1), "3_1.png")
    
    def test_check_move_too_many_cards(self):
        dragged_card = DraggedCard(None,[Card(1,3),Card(2,3)])
        val = self.endpile.check_move(dragged_card)
        self.assertEqual(val, False)

    def test_check_move_empty_pile_success(self):
        dragged_card = DraggedCard(None, [Card(0,1)])
        val = self.endpile.check_move(dragged_card)
        self.assertEqual(val, True)

    def test_check_move_nonempty_pile_success(self):
        dragged_card = DraggedCard(None, [Card(1,1)])
        self.endpile.pile.append(Card(0,1))
        val = self.endpile.check_move(dragged_card)
        self.assertEqual(val, True)
    
    def test_check_move_empty_pile_fail(self):
        dragged_card = DraggedCard(None, [Card(5,1)])
        val = self.endpile.check_move(dragged_card)
        self.assertEqual(val, False)

    def test_check_move_nonempty_pile_fail(self):
        dragged_card = DraggedCard(None, [Card(5,1)])
        self.endpile.pile.append(Card(0,1))
        val = self.endpile.check_move(dragged_card)
        self.assertEqual(val, False)
