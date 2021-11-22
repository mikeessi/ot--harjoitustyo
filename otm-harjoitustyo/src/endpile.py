
class Endpile:

    def __init__(self,suit,deck):
        self.deck = deck
        self.suit = suit
        self.pile = []

    def dragged_card(self):
        if len(self.pile) == 0:
            return None
        card = self.pile.pop(-1)
        return card

    def update(self):
        if len(self.pile) == 0:
            card = None
        else:
            card = self.pile[-1]
        origin = "empty_" + str(self.suit)
        return card, origin

    def check_move(self, card):
        if card.suit == self.suit:
            if len(self.pile) == 0:
                if card.value == 0:
                    self.pile.append(card)
                    return True
            else:
                if card.value == self.pile[-1].value+1:
                    self.pile.append(card)
                    return True

        return False
