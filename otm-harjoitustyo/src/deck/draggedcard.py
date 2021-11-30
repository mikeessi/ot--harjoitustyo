
class DraggedCard:

    def __init__(self, origin, card):
        self.origin = origin
        self.card = card

    def cancel_drag(self):
        self.origin.append(self.card)

    def update(self):
        return self.card, "drag"