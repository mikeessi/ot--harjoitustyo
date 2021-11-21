import pygame
from load_image import load_image


class DraggedCard:

    def __init__(self, display, origin, card):
        self.display = display
        self.origin = origin
        self.card = card
        self.card_img = load_image(str(card))
        self.coords = pygame.mouse.get_pos()

    def cancel_drag(self):
        self.origin.append(self.card)

    def update(self):
        self.coords = pygame.mouse.get_pos()
        self.display.blit(self.card_img, self.coords)