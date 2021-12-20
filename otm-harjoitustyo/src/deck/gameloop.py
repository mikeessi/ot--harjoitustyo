import pygame
from pygame.constants import K_ESCAPE, MOUSEBUTTONDOWN, KEYDOWN
from deck.draggedcard import DraggedCard
from deck.endpile import Endpile
from deck.drawpile import Drawpile
from deck.deck import Deck
from deck.discardpile import DiscardPile
from deck.tableau import Tableau

class GameLoop:
    """Luokka, joka mallintaa pelin päälooppia.

    Attributes:
        clock: Clock-olio, toimii kellona.
        event_queue: EventQueue-olio, joka tarkistaa pygame-tapahtumat.
        display: Itse peliruutu.
        renderer: Renderer-olio, joka piirtää kuvat ruudulle.
        hb: Hitboxes-olio, joka pitää huolta pygame.Rect-olioista.
        deck: Deck-olio, joka toimii pelipakkana.
        discardpile: DiscardPile-olio, joka toimii hylkypakkana.
        drawpile: DrawPile-olio, joka toimii nostopakkana.
        renderer_list: Lista renderöitävistä objekteista renderöijälle.
        endpile_list: Lista Endpile-olioista, jotka toimivat pelin loppupinoina.
        tableau_list: Lista Tableau-olioista, jotka toimivat pelipinoina.
        currently_dragging: Tieto siitä, raahataanko tällä hetkellä korttia.
        dragged_card: Tällä hetkellä raahattava DraggedCard-olio.
        no_hits: Tieto siitä, osuttiinko klikkauksella mihinkään Rect-olioon.
        points: Tämänhetkiset pisteet.
        deck_length: Pakan korttien määrä (pelin alussa).
        tabl_length: Korttien määrä pelipinoissa (pelin alussa).
        endpile_length: Korttien määrä loppupinoissa (pelin alussa).
    """

    def __init__(self,clock,event_queue,display,renderer,hitboxes):
        """Luokan konstruktori, joka luo peliloopin.

        Args:
            clock: Clock-olio, joka toimii kellona.
            event_queue: EventQueue-olio, joka käsittelee pygame-tapahtumat.
            display: Peliruutu.
            renderer: Renderer-olio, joka hoitaa pelin piirtämisen.
            hitboxes: Hitboxes-olio, joka pitää huolen pygame.Rect-olioista.
        """

        self.clock = clock
        self.event_queue = event_queue
        self.display = display
        self.renderer = renderer
        self.hb = hitboxes

        self.deck = Deck()
        self.discardpile = DiscardPile(self.deck)
        self.drawpile = Drawpile(self.deck)

        self.renderer_list = [self.drawpile,self.discardpile]

        self.endpile_list = []
        for suit in range(4):
            endpile = Endpile(suit,self.deck)
            self.renderer_list.append(endpile)
            self.endpile_list.append(endpile)

        self.tableau_list = []

        for tabl_id in range(7):
            tableau = Tableau(tabl_id)
            self.tableau_list.append(tableau)

        self.currently_dragging = False
        self.dragged_card = None
        self.no_hits = True

        self.points = 0
        self.face_down_cards = 21
        self.deck_length = 24
        self.tabl_lenght = 28
        self.endpile_length = 0


    def start(self):
        """Aloittaa pelin ja sisältää itse peliloopin.

        Ennen pelin alkua sekoittaa pakan ja jakaa kortit alkusijainteihin.
        Loopissa päivittää ruudun tapahtumat.
        """

        self.deck.shuffle_deck()
        self.setup_game()

        while True:
            if self.handle_events() is False:
                break

            self.renderer.render(self.display,self.renderer_list,self.tableau_list,
            self.dragged_card, self.points)


        self.clock.tick(60)

    def handle_events(self):
        """Käsittelee tapahtumat, jotka EventQueue-olio antaa.

        Käsittelee käyttäjän syötteet ja toimii sopivalla tavalla syötteestä riippuen.

        Returns:
            False, kun painetaan Esc, tai ruksia, ts. kun peli halutaan sulkea.
        """
        for event in self.event_queue.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                self.no_hits = False
                pile, index, rank = self.hb.check_rects(mouse_pos, self.tableau_list)
                if pile == "drawpile":
                    self.handle_drawpile()
                if pile == "discardpile":
                    self.handle_discardpile()
                if pile == "endpile":
                    self.handle_endpiles(index)
                if pile == "tableau":
                    self.handle_tableaus(index, rank)
                if pile is None:
                    self.no_hits = True
                    self.handle_no_hits()

            if event.type == MOUSEBUTTONDOWN and event.button == 3:
                if self.currently_dragging is True:
                    self.cancel_drag(None, False)

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False

            if event.type == pygame.QUIT:
                return False

    def cancel_drag(self, destination, success):
        """Peruu kortin raahauksen.

        Siirtää kortit joko alkuperäiseen sijaintiin tai kohteeseen riippuen siitä,
        oliko liike sallittu.
        Kutsuu pisteidenpäivttäjää jokaisen siirron jälkeen joka tapauksessa.

        Args:
            destination: Raahattujen korttien määränpää.
            success: Tieto siitä, oliko liike sallittu.
        """
        if success is False:
            self.dragged_card.cancel_drag()
        else:
            for card in self.dragged_card.cards:
                destination.append(card)
        self.calculate_points()
        self.dragged_card = None
        self.currently_dragging = False

    def handle_endpiles(self, endpile_index):
        """Käsittelee loppupinojen klikkauksen.

        Jos kortteja raahataan, tarkistaa siirron laillisuuden, jos kortteja ei raahata, niin nostaa
        päällimäisen kortin loppupinosta raahattavaksi.

        Args:
            endpile_index: Klikatun loppupinon indeksi endpile_list-listassa.
        """
        self.no_hits = False
        if self.currently_dragging is False:
            card = self.endpile_list[endpile_index].dragged_card()
            if card:
                self.currently_dragging = True
                self.dragged_card = DraggedCard(self.endpile_list[endpile_index].pile,[card])
        elif self.currently_dragging is True:
            if self.endpile_list[endpile_index].check_move(self.dragged_card) is True:
                self.cancel_drag(self.endpile_list[endpile_index].pile, True)

    def handle_drawpile(self):
        """Käsittelee nostopinon klikkauksen.

        Jos korttia raahataan klikatessa, ei tee mitään, jos ei raahata, niin nostaa kortin.
        """
        if self.currently_dragging is True:
            pass
        else:
            self.deck.draw_card()

    def handle_discardpile(self):
        """Käsittelee hylkypinon klikkauksen.

        Jos korttia raahataan, niin peruu raahauksen, jos ei raahata, niin ottaa
        päällimäisen kortin raahattavaksi.
        """
        if self.currently_dragging is False:
            card = self.discardpile.dragged_card()
            if card:
                self.currently_dragging = True
                self.dragged_card = DraggedCard(self.deck.discard, [card])
        elif self.currently_dragging is True:
            self.cancel_drag(None, False)

    def handle_tableaus(self, tableau_index, tableau_rank):
        """Käsittelee pelipinojen klikkauksen.

        Jos kortteja ei raahata klikkaushetkellä,
        koittaa nostaa klikatun kortin raahattavaksi, mikäli sallittua.
        Muutoin tarkistaa, onko raahattujen korttien siirto mahdollista klikattuun pinoon.

        Args:
            tableau_index: Klikatun pelipinon indeksi tableau_list-listassa.
            tableau_rank: Klikatun kortin indeksi sitä vastaavassa Tableau.cards-listassa.
        """
        if self.currently_dragging is False:
            cards = self.tableau_list[tableau_index].dragged_cards(tableau_rank)
            if cards:
                self.currently_dragging = True
                self.dragged_card = DraggedCard(self.tableau_list[tableau_index].cards, cards)
        elif self.currently_dragging is True:
            if self.tableau_list[tableau_index].check_move(self.dragged_card) is True:
                self.cancel_drag(self.tableau_list[tableau_index].cards, True)

    def handle_no_hits(self):
        """Käsittelee tilanteen, kun klikataan ohi kaikesta.
        """
        if self.currently_dragging is True:
            if self.no_hits is True:
                self.cancel_drag(None, False)

    def setup_game(self):
        """Jakaa kortit naama alas pelipinoihin ja kääntää sitten viimeisen kortin naama ylös.
        """
        for i in range(1,8):
            for rank in range(i):
                card = self.deck.cards.pop(-1)
                card.face_down = True
                self.tableau_list[i-1].cards.append(card)
        for tabl in self.tableau_list:
            tabl.cards[-1].face_down = False

    def calculate_points(self):
        """Laskee pisteet.

        Vertaa jokaisella siirrolla korttien määrää eri pinoissa,
        ja sen perusteella vähentää tai lisää pisteitä.
        Varmistaa, että pisteet eivät mene negatiiviseksi.
        """
        curr_tabl_lengths = sum([len(tabl.cards) for tabl in self.tableau_list])
        curr_endpile_lengths = sum([len(endpile.pile) for endpile in self.endpile_list])
        curr_deck_length = len(self.deck.cards)+len(self.deck.discard)

        if curr_deck_length < self.deck_length and curr_tabl_lengths > self.tabl_lenght:
            self.points += 5

        elif curr_deck_length < self.deck_length and curr_endpile_lengths > self.endpile_length:
            self.points += 10

        elif curr_tabl_lengths < self.tabl_lenght and curr_endpile_lengths > self.endpile_length:
            self.points += 10

        elif curr_tabl_lengths > self.tabl_lenght and curr_endpile_lengths < self.endpile_length:
            self.points -= 15

        self.endpile_length = curr_endpile_lengths
        self.deck_length = curr_deck_length
        self.tabl_lenght = curr_tabl_lengths

        if self.count_face_down_cards() < self.face_down_cards:
            self.points += 5
            self.face_down_cards = self.count_face_down_cards()

        self.points = max(self.points, 0)

    def count_face_down_cards(self):
        """Laskee pelipinoissa olevien naama alaspäin olevien korttien määrän.

        Returns:
            Naama alaspäin olevien korttien määrän.
        """
        curr_face_down_cards = 0
        for tabl in self.tableau_list:
            for card in tabl.cards:
                if card.face_down is True:
                    curr_face_down_cards +=1
        return curr_face_down_cards
