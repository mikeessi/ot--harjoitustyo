

class Endpile:
    """Luokka, joka mallintaa pelin loppupinoja.
    
    Attributes:
        deck: Pinoihin liittyvä pelipakka.
        suit: Pinon maa.
        pile: Lista Card-olioista.
    """

    def __init__(self,suit,deck):
        """Luokan konstruktori, joka luo uuden loppupinon.
        
        Args:
            deck: Pinoon liittyvä pelipakka.
            suit: Pinon maa.
        """
        self.deck = deck
        self.suit = suit
        self.pile = []

    def dragged_card(self):
        """Nostaa pinon päällimäisen kortin.
        
        Returns:
            Päällimmäinen kortti, jos sellainen on, muuten None.
        """
        if len(self.pile) == 0:
            return None
        card = self.pile.pop(-1)
        return card

    def update(self):
        """Renderöintiä varten palauttaa tiedon päällimmäisestä kortista.
        
        Returns:
            Päällimmäinen kortti, tieto pinon maasta. Jos pino tyhjä niin None, tieto maasta.
        """
        if len(self.pile) == 0:
            card = None
        else:
            card = self.pile[-1]
        origin = "empty_" + str(self.suit)
        return card, origin

    def check_move(self, dragged_card):
        """Tarkistaa kortin siirron laillisuuden.

        Tarkistaa, ettei argumentin olio sisällä yli yhtä korttia, ja sitten tarkistaa, että
        raahatun kortin maa ja arvo ovat sopivat.
        
        Args:
            dragged_card: DraggedCard-olio, joka mallintaa valittua korttia.
        
        Returns:
            True, jos siirto on laillinen, muuten False.
        """
        if len(dragged_card.cards) != 1:
            return False
        if dragged_card.card.suit == self.suit:
            if len(self.pile) == 0:
                if dragged_card.card.value == 0:
                    return True
            else:
                if dragged_card.card.value == self.pile[-1].value+1:
                    return True

        return False
