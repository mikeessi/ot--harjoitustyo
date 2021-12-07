import pygame
from pygame.constants import K_ESCAPE, K_F2, MOUSEBUTTONDOWN, KEYDOWN
from deck.draggedcard import DraggedCard
from deck.endpile import Endpile
from deck.drawpile import Drawpile
from deck.deck import Deck
from deck.discardpile import DiscardPile
from deck.tableau import Tableau

class GameLoop:

    def __init__(self,clock,event_queue,display,renderer,hitboxes):

        self.clock = clock
        self.event_queue = event_queue
        self.display = display
        self.renderer = renderer
        self.hb = hitboxes

        self.deck = Deck()
        self.discardpile = DiscardPile(self.deck)
        self.drawpile = Drawpile(self.deck)

        self.renderer_list = [self.drawpile,self.discardpile]

        self.endpile_list = []
        for suit in range(4):
            endpile = Endpile(suit,self.deck)
            self.renderer_list.append(endpile)
            self.endpile_list.append(endpile)

        self.tableau_list = []

        for tabl_id in range(7):
            tableau = Tableau(tabl_id)
            self.tableau_list.append(tableau)

        self.currently_dragging = False
        self.dragged_card = None
        self.no_hits = True


    def start(self):

        self.deck.shuffle_deck()
        self.setup_game()

        while True:
            if self.handle_events() is False:
                break
            self.renderer.render(self.display,self.renderer_list,self.tableau_list,
            self.dragged_card)


        self.clock.tick(60)

    def handle_events(self):
        for event in self.event_queue.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.no_hits = False
                pile, index, rank = self.hb.check_rects(mouse_pos)
                if pile == "drawpile":
                    self.handle_drawpile()
                if pile == "discardpile":
                    self.handle_discardpile()
                if pile == "endpile":
                    self.handle_endpiles(index)
                if pile == "tableau":
                    self.handle_tableaus(index, rank)
                if pile is None:
                    self.no_hits = True
                    self.handle_no_hits()

            if event.type == KEYDOWN:
                if event.key == K_F2:
                    self.restart()
                    return False
                if event.key == K_ESCAPE:
                    return False

            if event.type == pygame.QUIT:
                return False

    def cancel_drag(self, destination, success):
        if success is False:
            self.dragged_card.cancel_drag()
        else:
            for card in self.dragged_card.cards:
                destination.append(card)
        self.dragged_card = None
        self.currently_dragging = False

    def handle_endpiles(self, endpile_index):
        self.no_hits = False
        if self.currently_dragging is False:
            card = self.endpile_list[endpile_index].dragged_card()
            if card:
                self.currently_dragging = True
                self.dragged_card = DraggedCard(self.endpile_list[endpile_index].pile,[card])
        elif self.currently_dragging is True:
            if self.endpile_list[endpile_index].check_move(self.dragged_card) is True:
                self.cancel_drag(self.endpile_list[endpile_index].pile, True)

    def handle_drawpile(self):
        if self.currently_dragging is True:
            pass
        else:
            self.deck.draw_card()

    def handle_discardpile(self):
        if self.currently_dragging is False:
            card = self.discardpile.dragged_card()
            if card:
                self.currently_dragging = True
                self.dragged_card = DraggedCard(self.deck.discard, [card])
        elif self.currently_dragging is True:
            self.cancel_drag(None, False)

    def handle_tableaus(self, tableau_index, tableau_rank):
        if self.currently_dragging is False:
            cards = self.tableau_list[tableau_index].dragged_cards(tableau_rank)
            if cards:
                self.currently_dragging = True
                self.dragged_card = DraggedCard(self.tableau_list[tableau_index].cards, cards)
        elif self.currently_dragging is True:
            if self.tableau_list[tableau_index].check_move(self.dragged_card) is True:
                self.cancel_drag(self.tableau_list[tableau_index].cards, True)

    def handle_no_hits(self):
        if self.currently_dragging is True:
            if self.no_hits is True:
                self.cancel_drag(None, False)

    def setup_game(self):
        for i in range(1,8):
            for rank in range(i):
                card = self.deck.cards.pop(-1)
                card.face_down = True
                self.tableau_list[i-1].cards.append(card)
        for tabl in self.tableau_list:
            tabl.cards[-1].face_down = False

    def restart(self):
        self.deck = Deck()
        self.discardpile = DiscardPile(self.deck)
        self.drawpile = Drawpile(self.deck)

        self.renderer_list = [self.drawpile,self.discardpile]

        self.endpile_list = []
        for suit in range(4):
            endpile = Endpile(suit,self.deck)
            self.renderer_list.append(endpile)
            self.endpile_list.append(endpile)

        self.tableau_list = []

        for tabl_id in range(7):
            tableau = Tableau(tabl_id)
            self.tableau_list.append(tableau)

        self.start()
