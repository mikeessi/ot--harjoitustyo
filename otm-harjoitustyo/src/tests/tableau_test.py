import unittest
from deck.tableau import Tableau
from deck.deck import Deck
from deck.card import Card
from deck.draggedcard import DraggedCard

class TestTableau(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.tableau = Tableau(1)

    def test_check_move_fail_wrong_color(self):
        self.tableau.cards.append(Card(1,3))
        dragged_card = DraggedCard(None, [Card(2,3)])
        val = self.tableau.check_move(dragged_card)
        self.assertEqual(val, False)

    def test_check_move_success_nonempty_pile(self):
        self.tableau.cards.append(Card(3,3))
        dragged_card = DraggedCard(None, [Card(2,2)])
        val = self.tableau.check_move(dragged_card)
        self.assertEqual(val, True)

    def test_check_move_fail_wrong_value_card(self):
        self.tableau.cards.append(Card(3,3))
        dragged_card = DraggedCard(None, [Card(1,2)])
        val = self.tableau.check_move(dragged_card)
        self.assertEqual(val, False)

    def test_check_move_fail_wrong_value_empty_pile(self):
        dragged_card = DraggedCard(None, [Card(1,3)])
        val = self.tableau.check_move(dragged_card)
        self.assertEqual(val, False)

    def test_dragged_cards_top_card_is_face_down(self):
        self.tableau.cards.append(Card(1,3))
        self.tableau.cards[-1].face_down = True
        val = self.tableau.dragged_cards(0)
        self.assertEqual(val, None)
    
    def test_dragged_cards_card_rank_too_low(self):
        for i in range(6):
            self.tableau.cards.append(Card(1,3))
        
        for card in self.tableau.cards:
            card.face_down = True
        
        self.tableau.cards[-1].face_down = False

        val = self.tableau.dragged_cards(0)
        self.assertEqual(val, None)