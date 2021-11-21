import pygame
from load_image import load_image

class Renderer:

    def __init__(self, coordinates):

        self.images = {"discard": "empty_2.png",
                       "empty_draw": "empty_1.png",
                       "draw": "back_1.png"}
        self.coordinates = coordinates

    def render(self, display, list):
        display.fill((0,130,25))
        for object in list:
            if object:
                card, origin = object.update()
                if card != None:
                    card_img = load_image(str(card))
                if card == None:
                    card_img = load_image(self.images[origin])
                coords = self.coordinates[origin]
                if origin == "drag":
                    coords = pygame.mouse.get_pos()
                
            display.blit(card_img, coords)
        pygame.display.flip()