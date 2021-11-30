import pygame
from pygame.constants import MOUSEBUTTONDOWN
from deck.draggedcard import DraggedCard
from deck.endpile import Endpile
from deck.drawpile import Drawpile
from deck.deck import Deck
from deck.discardpile import DiscardPile
from deck.tableau import Tableau

class GameLoop:

    def __init__(self, clock, event_queue, display,renderer, positions, card_size):

        self.clock = clock
        self.event_queue = event_queue
        self.display = display
        self.renderer = renderer
        self.deck = Deck()

        self.discardpile_rect = pygame.Rect(positions["discard"], card_size)
        self.discardpile = DiscardPile(self.deck)

        self.drawpile_rect = pygame.Rect(positions["draw"], card_size)
        self.drawpile = Drawpile(self.deck)

        self.renderer_list = [self.drawpile,self.discardpile]

        self.endpile_rects = []
        self.endpile_list = []
        for suit in range(4):
            endpile = Endpile(suit,self.deck)
            self.renderer_list.append(endpile)
            self.endpile_list.append(endpile)
            self.endpile_rects.append(pygame.Rect(positions[f"empty_{suit}"], card_size))
       
        self.tableau_list = []
        self.tableau_rects = []
        self.tableau_union_rects = []

        for id in range(7):
            pos_base = positions[f"tableau_{id}"]
            tableau = Tableau(id)
            single_pile_rects = []
            pos_adjust = 0
            for rect in range(20):
                pos = (pos_base[0],pos_base[1]+pos_adjust)
                single_pile_rects.append(pygame.Rect(pos,card_size))
                pos_adjust += 20
            self.tableau_rects.append(single_pile_rects)
            self.tableau_list.append(tableau)
        
        for sequence in self.tableau_rects:
            first_rect = sequence[0]
            union_rect = first_rect.unionall(sequence[1:])
            self.tableau_union_rects.append(union_rect)

       
        self.currently_dragging = False
        self.dragged_card = None
        self.no_hits = True

        
        

    def start(self):
        self.deck.shuffle_deck()

        while True:
            if self.handle_events() == False:
                break
            self.renderer.render(self.display, self.renderer_list, self.tableau_list, self.dragged_card)

        current_time = self.clock.get_ticks()

        self.clock.tick(60)

    def handle_events(self):
        for event in self.event_queue.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.no_hits = True
                self.handle_endpiles(mouse_pos)
                self.handle_drawpile(mouse_pos)
                self.handle_discardpile(mouse_pos)
                self.handle_tableaus(mouse_pos)
                self.handle_no_hits()

            if event.type == pygame.QUIT:
                return False

    def cancel_drag(self, destination, success):
        if success == False:
            self.dragged_card.cancel_drag()
        else:
            for card in self.dragged_card.cards:
                destination.append(card)
        self.dragged_card = None
        self.currently_dragging = False

    def handle_endpiles(self, mouse_pos):
        endpile = self.check_rects(mouse_pos, self.endpile_rects, False)
        if endpile != None:
            self.no_hits = False
            if self.currently_dragging == True:
                if self.endpile_list[endpile].check_move(self.dragged_card.card) == True:
                    self.cancel_drag(self.endpile_list[endpile].pile, True)
    
    def handle_drawpile(self, mouse_pos):
        if self.drawpile_rect.collidepoint(mouse_pos):
            self.no_hits = False
            if self.currently_dragging == True:
                self.cancel_drag(None, False)           
            else:
                self.deck.draw_card()
            

    def handle_discardpile(self, mouse_pos):
        if self.discardpile_rect.collidepoint(mouse_pos):
            self.no_hits = False                    
            if self.currently_dragging == False:
                card = self.discardpile.dragged_card()
                if card:
                    self.currently_dragging = True
                    self.dragged_card = DraggedCard(self.deck.discard,[card])
            elif self.currently_dragging == True:
                self.cancel_drag(None, False)

    def handle_tableaus(self, mouse_pos):
        tableau_num = self.check_rects(mouse_pos, self.tableau_union_rects, False)
        if tableau_num != None:
            tableau_ranks = self.tableau_rects[tableau_num]
            tableau_rank = self.check_rects(mouse_pos, tableau_ranks, True)
            self.no_hits = False
            if self.currently_dragging == False:
                cards = self.tableau_list[tableau_num].dragged_cards(tableau_rank)
                if cards:
                    self.currently_dragging = True
                    self.dragged_card = DraggedCard(self.tableau_list[tableau_num].cards, cards)
            elif self.currently_dragging == True:
                if self.tableau_list[tableau_num].check_move(self.dragged_card) == True:
                    self.cancel_drag(self.tableau_list[tableau_num].cards, True)
            
    
    def handle_no_hits(self):
        if self.currently_dragging == True:
            if self.no_hits == True:
                self.cancel_drag(None, False)

    def check_rects(self, mouse_pos, rect_list, reverse):
        if reverse:
            rects = reversed(list(enumerate(rect_list)))
        else:
            rects = enumerate(rect_list)

        for rect_index, rect in rects:
            if rect.collidepoint(mouse_pos):
                return rect_index
                
            