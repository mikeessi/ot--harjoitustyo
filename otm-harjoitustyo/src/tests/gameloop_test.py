import unittest
from deck.gameloop import GameLoop
from deck.draggedcard import DraggedCard
from deck.card import Card

class TestGameloop(unittest.TestCase):
    def setUp(self):
        self.gl = GameLoop(None,None,None,None,None)
        self.gl.setup_game()
        self.gl.dragged_card = DraggedCard(self.gl.deck.discard, [Card(1,3)])
        

    def test_setting_up_game_cards_on_table(self):
        lengths = []
        for tab in self.gl.tableau_list:
            lengths.append(len(tab.cards))

        self.assertEqual(lengths, [1,2,3,4,5,6,7])

    def test_handle_drawpile_draw_card_success(self):
        self.gl.currently_dragging = False
        self.gl.handle_drawpile()
        drawpile_len = len(self.gl.deck.discard)
        self.assertEqual(drawpile_len, 1)

    def test_handle_drawpile_draw_card_fail(self):
        self.gl.currently_dragging = True
        self.gl.handle_drawpile()
        drawpile_len = len(self.gl.deck.discard)
        self.assertEqual(drawpile_len, 0)
    
    def test_handle_discardpile_empty_pile_drag(self):
        self.gl.currently_dragging = False
        self.gl.handle_discardpile()
        self.assertEqual(self.gl.currently_dragging, False)

    def test_handle_discardpile_nonempty_pile_drag(self):
        self.gl.currently_dragging = False
        self.gl.deck.draw_card()
        self.gl.handle_discardpile()
        self.assertEqual(self.gl.currently_dragging, True)

    def test_handle_discardpile_while_dragging(self):
        self.gl.currently_dragging = True
        self.gl.handle_discardpile()
        self.assertEqual(self.gl.currently_dragging, False)

    def test_cancel_drag_succesful_move_dragged_cards_removed(self):
        self.gl.currently_dragging = True
        self.gl.cancel_drag(self.gl.endpile_list[0].pile, True)
        dragged_card = self.gl.dragged_card
        self.assertEqual(dragged_card, None)