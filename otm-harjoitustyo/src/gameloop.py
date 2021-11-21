import pygame
from pygame.constants import MOUSEBUTTONDOWN
from draggedcard import DraggedCard
from drawpile import Drawpile
from deck import Deck
from discardpile import DiscardPile


class GameLoop:

    def __init__(self, clock, event_queue, display,renderer):
        self.clock = clock
        self.event_queue = event_queue
        self.display = display
        self.renderer = renderer
        self.deck = Deck()
        self.drawpile = Drawpile(self.display, self.deck)
        self.discardpile = DiscardPile(self.display, self.deck)
        self.currently_dragging = False
        self.dragged_card = None
        self.renderer_list = [self.drawpile,self.discardpile]

    def start(self):
        self.deck.shuffle_deck()

        while True:
            if self.handle_events() == False:
                break
            self.display.fill((0,130,25))
            self.renderer.render(self.renderer_list)

        current_time = self.clock.get_ticks()


        self.clock.tick(60)

    def handle_events(self):
        for event in self.event_queue.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.drawpile.pile_rect.collidepoint(mouse_pos):
                    self.deck.draw_card()
                if self.discardpile.pile_rect.collidepoint(mouse_pos):                    
                    if self.currently_dragging == False:
                        card = self.discardpile.dragged_card()
                        if card:
                            self.currently_dragging = True
                            self.dragged_card = DraggedCard(self.display,self.deck.discard,card)
                            self.renderer_list.append(self.dragged_card)
                    elif self.currently_dragging == True:
                        self.cancel_drag()

                elif self.currently_dragging == True:
                    self.cancel_drag()


            if event.type == pygame.QUIT:
                return False

    def cancel_drag(self):
        self.renderer_list.pop(-1)
        self.dragged_card.cancel_drag()
        self.dragged_card = None
        self.currently_dragging = False
            