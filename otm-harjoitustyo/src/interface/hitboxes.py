import pygame

class Hitboxes:
    """Luokka, joka hallitsee kaikkien peliruudulla näkyvien objektien hitboxeja
    pygame.Rect-olioina.

    Attributes:
        discardpile_rect: Hylkypakan hitbox.
        drawpile_rect: Nostopakan hitbox.
        endpile_rects: Loppupinojen hitboxit.
        tableau_rects: Pelipinojen korttien hitboxit.
        tableau_union_rects: Pelipinojen korttien hitboxien yhdistehitboxi.
    """

    def __init__(self, positions, card_size):
        """Luokan konstruktori, joka luo hitboxit.

        Args:
            positions: dict, joka sisältää tiedot kaikkien pelimaton objektien sijainnista.
            card_size: Pelikorttien koko.
        """

        self.discardpile_rect = pygame.Rect(positions["discard"], card_size)
        self.drawpile_rect = pygame.Rect(positions["draw"], card_size)

        self.endpile_rects = []
        for suit in range(4):
            self.endpile_rects.append(pygame.Rect(positions[f"empty_{suit}"], card_size))

        self.tableau_rects = []
        self.tableau_union_rects = []

        for tabl_id in range(7):
            pos_base = positions[f"tableau_{tabl_id}"]
            single_pile_rects = []
            pos_adjust = 0
            for i in range(20):
                pos = (pos_base[0],pos_base[1]+pos_adjust)
                single_pile_rects.append(pygame.Rect(pos,card_size))
                pos_adjust += 20
            self.tableau_rects.append(single_pile_rects)

        for sequence in self.tableau_rects:
            first_rect = sequence[0]
            union_rect = first_rect.unionall(sequence[1:])
            self.tableau_union_rects.append(union_rect)

    def check_rects(self, mouse_pos, tabl_list):
        """Tarkistaa, onko hiiri klikkaushetkellä jonkin hitboxin kohdalla.

        Args:
            mouse_pos: Hiiren koordinaatit.
            tabl_list: Lista tableau-olioiden korttipakan pituudesta.
                       Tätä tarvitaan helpottamaan korttien klikkausta pelipinoissa.
        """

        if self.check_drawpile(mouse_pos) is not None:
            return self.check_drawpile(mouse_pos)
        elif self.check_discardpile(mouse_pos) is not None:
            return self.check_discardpile(mouse_pos)
        elif self.check_endpiles(mouse_pos) is not None:
            return self.check_endpiles(mouse_pos)
        elif self.check_tableaus(mouse_pos, tabl_list) is not None:
            return self.check_tableaus(mouse_pos, tabl_list)
        else:
            return None, None, None

    def check_lists(self, mouse_pos, rect_list, reverse):
        """Tarkistaa argumentissa annetun yksittäisen listan hiiren osumilta.

        Pelipinojen toteutuksen takia niiden korttilistat joutuu käymään läpi
        käänteisessä järjestyksessä, ettei vahingossa klikkaa alempaa korttia
        päällä olevan kortin läpi.

        Args:
            mouse_pos: Hiiren koordinaatit.
            rect_list: Lista hitboxeista, jotka tarkistetaan.
            reverse: Boolean-arvo, joka False muissa tapauksissa, paitsi pelipinoja käsitellessä.

        Returns:
            rect_list-listan indeksin, johon hiiri osui,
            None, jos osumia ei havaittu.
        """

        if reverse:
            rects = reversed(list(enumerate(rect_list)))
        else:
            rects = enumerate(rect_list)

        for rect_index, rect in rects:
            if rect.collidepoint(mouse_pos):
                return rect_index
        return None

    def check_endpiles(self, mouse_pos):
        """Hoitaa loppupinojen tarkistamisen.

        Metodi palauttaa joko None tai 3 paluuarvoa, mikä johtuu siitä, että pelipinojen
        osumien hoitamiseen tarvitsee palauttaa yhden ylimääräisen paluuarvon, ja
        GameLoop-oliossa sama metodi hoitaa molemmat asiat, jolloin se odottaa 3 paluu-
        arvoa takaisin.

        Args:
            mouse_pos: Hiiren koordinaatit.

        Returns:
            None, jos ei osumia.
            Merkkijonon "endpile", osutun loppupinon indeksin, ja None.
        """

        endpile_index = self.check_lists(mouse_pos, self.endpile_rects, False)
        if endpile_index is not None:
            return "endpile", endpile_index, None

        return None

    def check_drawpile(self, mouse_pos):
        """Hoitaa nostopinon tarkistamisen.

        Args:
            mouse_pos: Hiiren koordinaatit.

        Returns:
            None, jos ei osumia.
            Merkkijonon "drawpile", pinon indeksin, ja None.
        """

        drawpile = self.check_lists(mouse_pos, [self.drawpile_rect], False)
        if drawpile is not None:
            return "drawpile", drawpile, None

        return None

    def check_discardpile(self, mouse_pos):
        """Hoitaa hylkypakan tarkistamisen.

        Args:
            mouse_pos: Hiiren koordinaatit.

        Returns:
            None, jos ei osumia.
            Merkkijonon "discardpile", pinon indeksin ja None.
        """

        discardpile = self.check_lists(mouse_pos, [self.discardpile_rect], False)
        if discardpile is not None:
            return "discardpile", discardpile, None

        return None

    def check_tableaus(self, mouse_pos, tabl_list):
        """Hoitaa pelipinojen tarkistamisen.

        Tarkistaa pelipinojen korttien osumat sen perusteella, miten monta
        korttia pelipinossa on kullakin hetkellä.

        Args:
            mouse_pos: Hiiren koordinaatit.
            tabl_list: Lista pelipinojen korttien määristä.

        Returns:
            None, jos ei osumia.
            Merkkijonon "tableau", pelipinon indeksin, ja osutun kortin indeksi pelipinossa.
        """

        tableau_index = self.check_lists(mouse_pos, self.tableau_union_rects, False)
        if tableau_index is not None:
            hitbox_detect_start = len(tabl_list[tableau_index].cards)
            tableau = self.tableau_rects[tableau_index]
            tableau_rank = self.check_lists(mouse_pos, tableau[:hitbox_detect_start], True)
            if tableau_rank is None:
                tableau_rank = 0
            return "tableau", tableau_index, tableau_rank

        return None
