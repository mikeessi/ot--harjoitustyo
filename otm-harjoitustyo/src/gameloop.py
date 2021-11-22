import pygame
from pygame.constants import MOUSEBUTTONDOWN
from draggedcard import DraggedCard
from endpile import Endpile
from drawpile import Drawpile
from deck import Deck
from discardpile import DiscardPile


class GameLoop:

    def __init__(self, clock, event_queue, display,renderer, positions, card_size):

        self.discardpile_rect = pygame.Rect(positions["discard"], card_size)
        self.drawpile_rect = pygame.Rect(positions["draw"], card_size)
        self.endpile_rects = []
        self.endpile_list = []
        self.clock = clock
        self.event_queue = event_queue
        self.display = display
        self.renderer = renderer
        self.deck = Deck()
        self.drawpile = Drawpile(self.deck)
        self.discardpile = DiscardPile(self.deck)
        self.currently_dragging = False
        self.dragged_card = None
        self.renderer_list = [self.drawpile,self.discardpile]
        for suit in range(4):
            endpile = Endpile(suit,self.deck)
            self.renderer_list.append(endpile)
            self.endpile_list.append(endpile)
            self.endpile_rects.append(pygame.Rect(positions[f"empty_{suit}"], card_size))
        

    def start(self):
        self.deck.shuffle_deck()

        while True:
            if self.handle_events() == False:
                break
            self.renderer.render(self.display, self.renderer_list)

        current_time = self.clock.get_ticks()


        self.clock.tick(60)

    def handle_events(self):
        for event in self.event_queue.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                endpile = self.check_endpile_rects(mouse_pos)
                if endpile != None:
                    if self.currently_dragging == True:
                        if self.endpile_list[endpile].check_move(self.dragged_card.card) == True:
                            self.cancel_drag(True)
                        else:
                            continue
                if self.drawpile_rect.collidepoint(mouse_pos):
                    self.deck.draw_card()
                if self.discardpile_rect.collidepoint(mouse_pos):                    
                    if self.currently_dragging == False:
                        card = self.discardpile.dragged_card()
                        if card:
                            self.currently_dragging = True
                            self.dragged_card = DraggedCard(self.deck.discard,card)
                            self.renderer_list.append(self.dragged_card)
                    elif self.currently_dragging == True:
                        self.cancel_drag(False)
                
                
                 
                elif self.currently_dragging == True:
                    self.cancel_drag(False)


            if event.type == pygame.QUIT:
                return False

    def cancel_drag(self, bool):
        self.renderer_list.pop(-1)
        if bool == False:
            self.dragged_card.cancel_drag()
        self.dragged_card = None
        self.currently_dragging = False


    def check_endpile_rects(self, mouse_pos):
        for i, suit_rect in enumerate(self.endpile_rects):
            if suit_rect.collidepoint(mouse_pos):
                return i
                
            