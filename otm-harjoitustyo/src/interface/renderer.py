import pygame
from load_image import load_image

class Renderer:

    def __init__(self, positions, images):

        self.images = images

        self.positions = positions

    def render(self, display, others_list, tableau_list, dragged_cards):
        display.fill((0,130,25))
        for tableau in tableau_list:
            self.render_tableau(display, tableau)
        for sprite in others_list:
            self.render_help(display, sprite)
        if dragged_cards:
            self.render_dragged(display, dragged_cards)
        pygame.display.flip()


    def render_help(self, display, sprite):
        if sprite:
            card, origin = sprite.update()
            if card is not None:
                card_img = load_image(str(card))
            if card is None:
                card_img = load_image(self.images[origin])
            pos = self.positions[origin]

        display.blit(card_img, pos)

    def render_tableau(self, display, tableau):
        tab = f"tableau_{tableau.tab_id}"
        pos_base = self.positions[tab]
        if len(tableau.cards) == 0:
            card_img = load_image(self.images[tab])
            display.blit(card_img, pos_base)
        else:
            pos_adjust = 0
            for card in tableau.cards:
                if card.face_down is True:
                    card_img = load_image("back_1.png")
                else:
                    card_img = load_image(str(card))
                pos = (pos_base[0],pos_base[1]+pos_adjust)
                display.blit(card_img, pos)
                pos_adjust += 20

    def render_dragged(self, display, dragged_cards):
        pos_adjust = 0
        pos_base = pygame.mouse.get_pos()
        for card in dragged_cards.cards:
            card_img = load_image(str(card))
            pos = (pos_base[0],pos_base[1]+pos_adjust)
            pos_adjust +=20
            display.blit(card_img, pos)
