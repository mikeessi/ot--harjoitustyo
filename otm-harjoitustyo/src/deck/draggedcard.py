
class DraggedCard:
    """Luokka, joka mallintaa peliruudulla raahattavia kortteja
    
    Attributes:
        origin: Kortin sijainti ennen kortin valintaa.
        cards: Lista kortteja, jotka valittiin.
        card: Korttilistan ensimmäinen kortti
    """

    def __init__(self, origin, cards):
        """"Luokan konstruktori, joka luo uuden raahattavan kortin/pinon kortteja
        
        Args:
            origin: Kortin alkuperäinen sijainti.
            cards: Lista valituista korteista.
            card: Listan ensimmäinen jäsen
        """
        self.origin = origin
        self.cards = cards
        self.card = cards[0]

    def cancel_drag(self):
        """Palauttaa raahatut kortit alkuperäiseen sijaintiin.
        
        """
        for card in self.cards:
            self.origin.append(card)
        self.cards = []
