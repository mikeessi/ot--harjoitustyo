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

    def test_handle_endpiles_no_hits_toggle(self):
        self.gl.handle_endpiles(1)
        self.assertEqual(self.gl.no_hits, False)

    def test_handle_endpiles_not_dragging_toggle_dragging(self):
        self.gl.endpile_list[1].pile.append(Card(1,3))
        self.gl.handle_endpiles(1)
        self.assertEqual(self.gl.currently_dragging, True)

    def test_handle_endpiles_while_dragging_fail(self):
        self.gl.dragged_card = DraggedCard(self.gl.deck.discard, [Card(1,3)])
        self.gl.currently_dragging = True
        self.gl.handle_endpiles(1)
        self.assertEqual(len(self.gl.endpile_list[1].pile), 0)

    def test_handle_endpiles_while_dragging_success(self):
        self.gl.dragged_card = DraggedCard(self.gl.deck.discard, [Card(0,1)])
        self.gl.currently_dragging = True
        self.gl.handle_endpiles(1)
        self.assertEqual(len(self.gl.endpile_list[1].pile), 1)

    def test_handle_no_hits_both_true(self):
        self.gl.currently_dragging = True
        self.gl.no_hits = True
        self.gl.handle_no_hits()
        self.assertEqual(self.gl.currently_dragging, False)

    def test_handle_no_hits_both_false(self):
        self.gl.currently_dragging = False
        self.gl.no_hits = False
        self.gl.handle_no_hits()
        self.assertEqual(self.gl.currently_dragging, False)

    def test_handle_no_hits_false(self):
        self.gl.currently_dragging = True
        self.gl.no_hits = False
        self.gl.handle_no_hits()
        self.assertEqual(self.gl.currently_dragging, True)

    def test_handle_tableaus_add_card_success(self):
        self.gl.tableau_list[0].cards = []
        self.gl.currently_dragging = True
        self.gl.dragged_card = DraggedCard(self.gl.deck.discard, [Card(12,3)])
        self.gl.handle_tableaus(0,0)
        self.assertEqual(len(self.gl.tableau_list[0].cards),1)

    def test_handle_tableaus_drag_card_success(self):
        self.gl.tableau_list[0].cards.append(Card(1,3))
        self.gl.currently_dragging = False
        self.gl.handle_tableaus(0,0)
        self.assertIsNotNone(self.gl.dragged_card)
    
    def test_handle_tableaus_drag_card_miss(self):
        self.gl.dragged_card = None
        self.gl.currently_dragging = False
        self.gl.handle_tableaus(0,15)
        self.assertIsNone(self.gl.dragged_card)

    def test_handle_tableaus_dragged_card_check_fail(self):
        self.gl.currently_dragging = True
        self.gl.dragged_card = DraggedCard(self.gl.deck.discard, [Card(12,3)])
        self.gl.handle_tableaus(0,0)
        self.assertEqual(len(self.gl.tableau_list[0].cards),1)

    def test_calculate_points_from_deck_to_tabl(self):
        card = self.gl.deck.cards.pop()
        self.gl.tableau_list[1].cards.append(card)
        self.gl.calculate_points()
        self.assertEqual(self.gl.points, 5)

    def test_calculate_points_from_tabl_to_endpile(self):
        card = self.gl.tableau_list[1].cards.pop()
        self.gl.endpile_list[1].pile.append(card)
        self.gl.calculate_points()
        self.assertEqual(self.gl.points, 10)

    def test_calculate_points_from_deck_to_endpile(self):
        card = self.gl.deck.cards.pop()
        self.gl.endpile_list[1].pile.append(card)
        self.gl.calculate_points()
        self.assertEqual(self.gl.points, 10)

    def test_calculate_points_from_endpile_to_tabl_negative(self):
        card = self.gl.deck.cards.pop()
        self.gl.endpile_list[1].pile.append(card)
        self.gl.calculate_points()
        card = self.gl.endpile_list[1].pile.pop()
        self.gl.tableau_list[1].cards.append(card)
        self.gl.calculate_points()
        self.assertEqual(self.gl.points, 0)

    def test_calculate_points_turn_face_down_card(self):
        self.gl.tableau_list[1].cards.pop()
        self.gl.tableau_list[1].cards[-1].face_down = False
        self.gl.calculate_points()
        self.assertEqual(self.gl.points, 5)

    def test_check_game_finish_true(self):
        for endpile in self.gl.endpile_list:
            for i in range(13):
                endpile.pile.append(Card(1,3))
        val = self.gl.check_game_finish()
        self.assertEqual(val, True)
    
    def test_check_game_finish_false(self):
        self.gl.endpile_list[1].pile.append(Card(1,3))
        val = self.gl.check_game_finish()
        self.assertEqual(val, False)

    def test_add_bonus_points_full(self):
        for i in range(10):
            self.gl.deck.draw_card()
        self.gl.add_bonus_points()
        self.assertEqual(self.gl.points, 100)

    def test_add_bonus_points_partial(self):
        for i in range(50):
            self.gl.deck.draw_card()
        self.gl.add_bonus_points()
        self.assertEqual(self.gl.points, 30)
    
    def test_add_bonus_points_nothing(self):
        for i in range(100):
            self.gl.deck.draw_card()
        self.gl.add_bonus_points()
        self.assertEqual(self.gl.points, 0)