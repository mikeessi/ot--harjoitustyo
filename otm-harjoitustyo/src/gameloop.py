import pygame
from pygame.constants import MOUSEBUTTONDOWN
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
        self.renderer_list = [self.drawpile,self.discardpile]

    def start(self):
        self.deck.shuffle_deck()

        while True:
            if self.handle_events() == False:
                break
            self.renderer.render(self.renderer_list)

        current_time = self.clock.get_ticks()


        self.clock.tick(60)

    def handle_events(self):
        for event in self.event_queue.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.drawpile.pile_rect.collidepoint(mouse_pos):
                    self.deck.draw_card()
            if event.type == pygame.QUIT:
                return False
            