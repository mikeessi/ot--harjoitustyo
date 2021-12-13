from random import shuffle
from deck.card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.discard = []
        self.deck_flips = 0
        for i in range(4):
            for j in range(13):
                self.cards.append(Card(j,i))

    def draw_card(self):
        if len(self.cards) == 0:
            self.cards = self.discard[::-1]
            self.discard = []
            self.deck_flips += 1
            return None

        drawn_card = self.cards.pop()
        self.discard.append(drawn_card)
        return drawn_card

    def shuffle_deck(self):
        shuffle(self.cards)
