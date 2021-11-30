

class Tableau:

    def __init__(self, id):
        self.cards = []
        self.id = id


    def check_move(self, dragged_card):

        if len(self.cards) == 0:
            if dragged_card.card.value == 12:
                return True

        else:
            top_card = self.cards[-1]
            if top_card.color != dragged_card.card.color:
                if top_card.value == dragged_card.card.value+1:
                    return True

        return False

    def dragged_cards(self, card_rank):
        if card_rank > len(self.cards):
            return None
        else:
            dragged_cards = self.cards[card_rank:]
            self.cards = self.cards[:card_rank]
            

        return dragged_cards

            

    def update(self):
        origin = f"tableau_{self.id}"
        if len(self.cards) == 0:
            return None, origin
        else:
            card = self.cards[-1]
            return card, origin
            
        
        
        