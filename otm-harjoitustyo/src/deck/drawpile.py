
class Drawpile:
    """Luokka, joka mallintaa pelipakan nostopakkaa.

    Args:
        deck:  Pelipakka, jonka nostopakka mallinnettaan.
    """

    def __init__(self,deck):
        """Luokan konstruktori, joka luo nostopakan

        Args:
            deck: Pelipakka
        """
        self.deck = deck

    def update(self):
        """Renderöintiä varten palauttaa tiedon siitä, onko pakka tyhjä vai ei

        Returns:
            None, "empty_draw", jos pakka tyhjä, None, "draw", jos ei.
        """
        if len(self.deck.cards) == 0:
            origin = "empty_draw"
        else:
            origin = "draw"
        return None, origin
