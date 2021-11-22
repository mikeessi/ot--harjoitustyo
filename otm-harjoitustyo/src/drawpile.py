
class Drawpile:
    
    def __init__(self,deck):
        self.deck = deck

    def update(self):
        if len(self.deck.cards) == 0:
            origin = "empty_draw"
        else:
            origin = "draw"
        return None, origin