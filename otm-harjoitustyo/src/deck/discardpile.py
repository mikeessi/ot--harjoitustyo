
class DiscardPile:

    def __init__(self, deck):
        self.deck = deck

    def dragged_card(self):
        if len(self.deck.discard) == 0:
            return None

        card = self.deck.discard.pop(-1)
        return card

    def update(self):
        if len(self.deck.discard) == 0:
            card = None
        else:
            card = self.deck.discard[-1]
        return card, "discard"
