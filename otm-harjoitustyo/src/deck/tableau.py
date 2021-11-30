

class Tableau:

    def __init__(self, id):
        self.cards = []
        self.id = id


    def check_move(self, card):

        if len(self.cards) == 0:
            if card.value == 12:
                self.cards.append(card)
                return True

        else:
            top_card = self.cards[-1]
            if top_card.color != card.color:
                if top_card.value == card.value+1:
                    self.cards.append(card)
                    return True

        return False

    def update(self):
        origin = f"tableau_{self.id}"
        if len(self.cards) == 0:
            return None, origin
        else:
            card = self.cards[-1]
            return card, origin
            
        
        
        