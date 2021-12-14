
class DiscardPile:
    """Luokka, joka mallintaa hylkypakkaa.

    Attributes:
        deck: Pelipakka, jonka hylkypakkaa mallinnetaan.
    """

    def __init__(self, deck):
        """Luokan konstruktori, joka luo hylkypakan.

        Args:
            deck: Hylkypakkaan liittyvä pelipakka.
        """
        self.deck = deck

    def dragged_card(self):
        """Poistaa hylkypakasta päällimmäisen kortin.

        Jos päällimmäistä korttia ei ole, palauttaa None.

        Returns:
            Päällimäinen hylkypakan kortti, jos sellainen on olemassa, muuten None.
        """
        if len(self.deck.discard) == 0:
            return None

        card = self.deck.discard.pop(-1)
        return card

    def update(self):
        """Renderöintiä varten kertoo, mikä pakan päällimmäinen kortti on.

        Returns:
            Päällimmäinen kortti ja merkkijono "discard", tai None ja merkkijono "discard",
            jos päällimmäistä korttia ei ole.
        """
        if len(self.deck.discard) == 0:
            card = None
        else:
            card = self.deck.discard[-1]
        return card, "discard"
