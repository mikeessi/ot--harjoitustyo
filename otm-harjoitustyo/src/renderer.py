import pygame
from load_image import load_image

class Renderer:

    def __init__(self, positions, images):

        self.images = images

        self.positions = positions

    def render(self, display, others_list, tableau_list):
        display.fill((0,130,25))
        for tableau in tableau_list:
            self.render_tableau(display, tableau)
        for object in others_list:
            self.render_help(display, object)
        pygame.display.flip()


    def render_help(self, display, object):
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

    def render_tableau(self, display, tableau):
        tab = f"tableau_{tableau.id}"
        pos_base = self.positions[tab]
        if len(tableau.cards) == 0:
            card_img = load_image(self.images[tab])
            display.blit(card_img, pos_base)
        else:
            pos_adjust = 0
            for card in tableau.cards:
                card_img = load_image(str(card))
                pos = (pos_base[0],pos_base[1]+pos_adjust)
                display.blit(card_img, pos)
                pos_adjust += 20

                
        
        
