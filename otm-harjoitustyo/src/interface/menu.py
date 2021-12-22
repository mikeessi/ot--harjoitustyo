from string import ascii_letters
import pygame_menu
from interface.renderer import Renderer
from interface.hitboxes import Hitboxes as Hb
from deck.gameloop import GameLoop
from data.hiscores import Hiscores
from initialize_database import get_db_connection

class Menu:
    """Luokka, joka mallintaa alkuvalikkoa.

    Attributes:
        positions: Dict, jossa tieto pelipinojen sijainnista matolla.
        images: Dict, jossa tieto pelikorttien tiedostonimistä.
        display: Pelimatto.
        hitboxes: Hitboxes-olio.
        renderer: Renderer-olio.
        event_queue: EventQueue-olio.
        clock: Clock-olio.
        hiscores: Hiscores-olio, joka käsittelee tietokantaoperaatiot.
        hiscore_menu: HiscoreMenu-olio, joka mallintaa hiscoreja.
        menu: pygame_menu.Menu-olio, joka on itse varsinainen menu.
        user_name: Menussa oleva tekstikenttä, johon nimi syötetään.
        """

    def __init__(self, positions, card_size, images, event_queue, clock, display):
        """Luokan konstruktori, joka luo itse pygame_menu.Menu-olion, ja siihen
        muutaman painikkeen.
        """
        self.positions = positions
        self.images = images
        self.display = display
        self._valid_char_list = list(ascii_letters)

        self.hitboxes = Hb(positions, card_size)
        self.renderer = Renderer(self.positions, self.images)
        self.event_queue = event_queue
        self.clock = clock
        self.hiscores = Hiscores(get_db_connection())
        self.hiscore_menu = HiscoreMenu(self.hiscores)
        self.menu = pygame_menu.Menu("Solitaire",800,600,theme = pygame_menu.themes.THEME_DARK)
        self.user_name = self.menu.add.text_input("Name: ", default = "", maxchar = 8,
                                                    valid_chars = self._valid_char_list)
        self.menu.add.button("New game", self.start_game)
        self.menu.add.selector("Cardback :", [("Red",1),("Blue",2)],onchange=self.set_cardback)
        self.menu.add.button("Hiscores", self.hiscore_menu.menu)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)


    def set_cardback(self, name, index):
        """Vaihtaa korttien selkäkuvaa.

        Args:
            name: Menun selektorissa oleva nimi.
            index: Menun selektorin valitun kohdan indeksi.
        """
        self.images["draw"] = f"back_{index}.png"
        self.renderer = Renderer(self.positions, self.images)

    def start_game(self):
        """Aloittaa pelin luomalla uuden GameLoop-olion. Pelistä poistuttaessa
        tallentaa pisteet tietokantaan ja päivittää hiscoret.
        """
        game_loop = GameLoop(self.clock, self.event_queue,
                            self.display, self.renderer, self.hitboxes)
        game_loop.user_name = self.user_name.get_value()
        score, status = game_loop.start()

        if score > 0:
            self.hiscores.add_high_score(self.user_name.get_value(),score,status)
        self.update_hiscores()

    def update_hiscores(self):
        """Päivittää hiscoret tyhjentämällä koko hiscore-menun, ja luomalla
        sinne uudet taulukot. En keksinyt muuta keinoa päivittää hiscoreja
        'dynaamisesti'.
        """
        self.hiscore_menu.menu.clear(reset=True)
        self.hiscore_menu.hiscores = self.hiscores.get_hiscores()
        self.hiscore_menu.update()

class HiscoreMenu:
    """Luokka, joka mallintaa hiscore-menua.

    Attributes:
        menu = pygame_menu.Menu-olio, johon menun toiminta perustuu.
        hiscores = Top 10 lista tuloksista, joka haettu tietokannasta.
        """

    def __init__(self, hiscores):
        self.menu = pygame_menu.Menu("Solitaire",800,600,theme = pygame_menu.themes.THEME_DARK)
        self.hiscores = hiscores.get_hiscores()
        self.update()

    def update(self):
        """Muodostaa hiscore-taulukon uusiksi joka kerralla."""
        hiscore_table = self.menu.add.table(table_id ="hiscores",
                                             font_color = "black", font_size = 20)
        hiscore_table.default_cell_padding = 5
        hiscore_table.default_row_background_color = "grey"
        hiscore_table.add_row(["Name", "Score", "Status"],
                                cell_font = pygame_menu.font.FONT_OPEN_SANS_BOLD)
        for row in range(10):
            try:
                data = list(self.hiscores[row])
                if data[2] == 1:
                    data[2] = "Complete"
                else:
                    data[2] = "DNF"
            except IndexError:
                data = ["---", "---", "---"]

            hiscore_table.add_row(data, cell_align=pygame_menu.locals.ALIGN_CENTER)
