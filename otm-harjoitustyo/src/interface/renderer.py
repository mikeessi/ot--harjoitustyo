import pygame
from load_image import load_image

class Renderer:
    """Luokka, joka hoitaa pelimaton ja sen objektien piirtämisen.

    Attributes:
        font: Fontti, jota piirretyissä teksteissä käytetään.
        images: Dict, jossa tieto korttien kuvien tiedostonimistä.
        positions: Dict, jossa tieto korttipinojen sijainnista matolla.
    """

    def __init__(self, positions, images):

        self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self.images = images

        self.positions = positions

    def render(self, display, others_list, tableau_list, dragged_cards, points):
        """Piirtää pelimaton ja organisoi muiden objektien siihen piirtämisen.

        Args:
            display: Peliruutu.
            others_list: Lista objekteista, jotka piirretään poislukien
                         pelipinot ja raahatut kortit.
            tableau_list: Lista piirrettävistä pelipinoista.
            dragged_cards: Tällä hetkellä raahatut kortit.
            points: Tähän mennessä kerätyt pisteet.
        """
        display.fill((0,130,25))
        for tableau in tableau_list:
            self.render_tableau(display, tableau)
        for sprite in others_list:
            self.render_help(display, sprite)
        if dragged_cards:
            self.render_dragged(display, dragged_cards)
        self.render_points(display, points)
        pygame.display.flip()


    def render_help(self, display, sprite):
        """Hoitaa kaiken muun piirtämisen, paitsi pelipinot ja raahatut kortit.

        Args:
            display: Peliruutu.
            sprite: Objekti-mitä piirretään.
        """
        if sprite:
            card, origin = sprite.update()
            if card is not None:
                card_img = load_image(str(card))
            if card is None:
                card_img = load_image(self.images[origin])
            pos = self.positions[origin]

        display.blit(card_img, pos)

    def render_tableau(self, display, tableau):
        """Hoitaa pelipinojen piirtämisen.

        Args:
            display: Peliruutu.
            tableau: Piirrettävä pelipino.
        """
        tab = f"tableau_{tableau.tab_id}"
        pos_base = self.positions[tab]
        if len(tableau.cards) == 0:
            card_img = load_image(self.images[tab])
            display.blit(card_img, pos_base)
        else:
            pos_adjust = 0
            for card in tableau.cards:
                if card.face_down is True:
                    card_img = load_image(self.images["draw"])
                else:
                    card_img = load_image(str(card))
                pos = (pos_base[0],pos_base[1]+pos_adjust)
                display.blit(card_img, pos)
                pos_adjust += 20

    def render_dragged(self, display, dragged_cards):
        """Hoitaa raahatun kortin piirtämisen.

        Args:
            display: Peliruutu.
            dragged_cards: Tällä hetkellä raahatut kortit.
        """
        pos_adjust = 0
        pos_base = pygame.mouse.get_pos()
        for card in dragged_cards.cards:
            card_img = load_image(str(card))
            pos = (pos_base[0],pos_base[1]+pos_adjust)
            pos_adjust +=20
            display.blit(card_img, pos)

    def render_points(self, display, points):
        """Piirtää tekstin, jossa lukee tämänhetkinen pistetilanne.

        Args:
            display: Peliruutu.
            points: Tämänhetkiset pisteet."""
        text_surface = pygame.font.Font.render(self.font, f"Score: {points}", True, (0,0,0))
        display.blit(text_surface, (800,600))

    def render_end_screen(self, display, points):
        """Piirtää pelin loppuruudun ja sen viestit.

        Args:
            display: Peliruutu.
            points: Pisteet pelin lopussa.
        """
        display.fill((50,50,50))
        score_display = pygame.font.Font.render(self.font, f"Game won! Score: {points}",
                                                 True, (255,255,255))
        quit_message = pygame.font.Font.render(self.font, "Press Esc to go back to menu.",
                                                 True, (255,255,255))
        display.blit(score_display, (400,300))
        display.blit(quit_message, (50,700))
        pygame.display.flip()
