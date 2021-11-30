from deck.card import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []
        self.discard = []
        for i in range(4):
            for j in range(13):
                self.cards.append(Card(j,i))

    def draw_card(self):
        if len(self.cards) == 0:
            self.cards = self.discard[::-1]
            self.discard = []
        else:
            drawn_card = self.cards.pop()
            self.discard.append(drawn_card)
            return drawn_card
    
    def shuffle_deck(self):
        shuffle(self.cards)