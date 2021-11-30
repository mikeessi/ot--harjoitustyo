
class DraggedCard:

    def __init__(self, origin, cards):
        self.origin = origin
        self.cards = cards
        self.card = cards[0]

    def cancel_drag(self):
        for card in self.cards:
            self.origin.append(card)
        self.cards = []
