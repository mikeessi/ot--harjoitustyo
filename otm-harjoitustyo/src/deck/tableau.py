
class Tableau:
    """Luokka, joka mallintaa pelipinoja.

    Attributes:
        cards: Lista Card-olioista, jotka pelipinossa ovat.
        tab_id: Pelipinon indeksi.
    """

    def __init__(self, tab_id):
        """Luokan konstruktori, joka luo uuden pelipinon.

        Args:
            tab_id: Pelipinon id.
        """
        self.cards = []
        self.tab_id = tab_id


    def check_move(self, dragged_card):
        """Tarkistaa pelipinoon kohdistuvan siirron laillisuuden.

        Jos pelipino on tyhjä, antaa siirtää vain kuninkaan.
        Muutoin tarkistaa, että värit eivät ole samat, ja kortin arvo on sopiva.

        Args:
            dragged_card: DraggedCard-olio, jota koitetaan siirtää pelipinoon.

        Returns:
            True, jos siirto on laillinen, muutoin False.
        """

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
        """Nostaa pelipinosta kortit halutusta kohdasta raahattavaksi.

        Tarkistaa, että halutussa sijainnissa on kortti.
        Tarkistaa, että kortti, josta lähtien nosto halutaan tehdä, on naama ylös.
        Jos pelipinon viimeinen kortti on naama alas, niin kääntää kortin.
        Muutoin nostaa kortit halutusta kortista lähtien raahattavaksi.

        Args:
            card_rank: Kortin indeksi self.cards-listassa.

        Returns:
            None, jos nosto ei sallittu, muutoin listan Card-olioita.
        """
        if card_rank >= len(self.cards):
            return None
        if self.cards[-1].face_down is True:
            self.turn_card()
            return None
        if self.cards[card_rank].face_down is True:
            return None
        dragged_cards = self.cards[card_rank:]
        self.cards = self.cards[:card_rank]

        return dragged_cards

    def turn_card(self):
        """Kääntää pelipinon päällimmäisen kortin naama ylös.
        """
        self.cards[-1].face_down = False
