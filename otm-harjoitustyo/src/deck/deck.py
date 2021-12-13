from random import shuffle
from deck.card import Card


class Deck:
    """Luokka, joka mallintaa itse korttipakkaa.

    Attributes:
        cards: Lista Card-olioista nostopakassa.
        discard: Lista Card-olioista hylkypinossa.
        deck_flips: Pisteytystä varten laskuri pakan käännöistä. 
    """
    def __init__(self):
        """Luokan konstruktori, joka luo uuden pelipakan, ja samalla sen kortit Card-olioina.

        """
        self.cards = []
        self.discard = []
        self.deck_flips = 0
        for i in range(4):
            for j in range(13):
                self.cards.append(Card(j,i))

    def draw_card(self):
        """Nostaa pakasta kortin.

        Jos nostopakka on tyhjä, nostamisen sijaan kääntää pakan.

        Returns:
            Kortti, joka nostettiin, jos pakassa oli kortteja, muussa tapauksessa None.
        """
        if len(self.cards) == 0:
            self.cards = self.discard[::-1]
            self.discard = []
            self.deck_flips += 1
            return None

        drawn_card = self.cards.pop()
        self.discard.append(drawn_card)
        return drawn_card

    def shuffle_deck(self):
        """Sekoittaa korttipakan.
        """
        shuffle(self.cards)
