
class Card:
    """Luokka, joka mallintaa korttipakan yksittäistä korttia.

    Attributes:
        suit: Kortin maa.
        value: Kortin arvo.
        face_down: Tieto siitä, kummin päin kortti on.
        color: Kortin väri.
    """

    suits = ["diamonds", "clubs", "hearts", "spades"]

    values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, value, suit):
        """Luokan konstruktori, joka luo korttipakan kortin.

        Args:
            value: Kortin arvo.
            suit: Kortin maa.
        """
        self.suit = suit
        self.value = value
        self.face_down = False
        if suit in [0,2]:
            self.color = "Red"
        else:
            self.color = "Black"

    def __repr__(self):
        """Muodostaa kortista korttia vastaavan kuvan tiedostonimen merkkijonona.

        Returns:
            Merkkijono, jossa on korttia vastaavan kuvan tiedostonimi.
        """
        name = str(self.suit) + "_" + str(self.value)+".png"
        return name
