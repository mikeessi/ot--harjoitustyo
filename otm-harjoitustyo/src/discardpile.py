from deck import Deck
from card import Card
from load_image import load_image

class DiscardPile:

    def __init__(self, display, deck):
        self.display = display
        self.deck = deck
        self.coords = (900, 20)
        self.empty_pile = load_image("empty_2.png")
        self.pile_rect = self.empty_pile.get_rect(x=self.coords[0],y=self.coords[1])
        self.drag = False

    def dragged_card(self):
        if len(self.deck.discard) == 0:
            return None
        else:
            card = self.deck.discard.pop(-1)
            return card
    
    def update(self):
        if len(self.deck.discard) == 0:
            self.display.blit(self.empty_pile, self.coords)
        else:
            card = self.deck.discard[-1]
            card_image = load_image(str(card))
            self.display.blit(card_image, self.coords)