import pygame
from load_image import load_image

class Renderer:

    def __init__(self, positions, images):

        self.images = images

        self.positions = positions

    def render(self, display, list):
        display.fill((0,130,25))
        for object in list:
            if object:
                card, origin = object.update()
                if card != None:
                    card_img = load_image(str(card))
                if card == None:
                    card_img = load_image(self.images[origin])
                pos = self.positions[origin]
                if origin == "drag":
                    pos = pygame.mouse.get_pos()
                
            display.blit(card_img, pos)
        pygame.display.flip()