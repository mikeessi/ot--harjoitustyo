from deck import Deck
from load_image import load_image


class Drawpile:
    
    def __init__(self,display,deck):
        self.coords = (400,200)
        self.display = display
        self.deck = deck
        self.cardback = load_image("back_1.png")
        self.empty_deck = load_image("empty_1.png")
        self.pile_rect = self.cardback.get_rect(x = self.coords[0], y = self.coords[1])
    
    def update(self):
        if len(self.deck.cards) == 0:
            self.display.blit(self.empty_deck, self.coords)
        else:
            self.display.blit(self.cardback, self.coords)