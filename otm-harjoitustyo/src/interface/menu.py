import pygame_menu
from interface.renderer import Renderer
from interface.hitboxes import Hitboxes as Hb
from deck.gameloop import GameLoop

class Menu:

    def __init__(self, positions, card_size, images, event_queue, clock, display):
        self.positions = positions
        self.images = images
        self.display = display

        self.hitboxes = Hb(positions, card_size)
        self.renderer = Renderer(self.positions, self.images)
        self.event_queue = event_queue
        self.clock = clock

        self.menu = pygame_menu.Menu("Solitaire",800,600,theme = pygame_menu.themes.THEME_DARK)
        self.menu.add.button("New game", self.start_game)
        self.menu.add.selector("Cardback :", [("Red",1),("Blue",2)],onchange=self.set_cardback)
        self.menu.add.button("Hiscores", self.show_hiscores)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)


    def set_cardback(self, name, i):
        self.images["draw"] = f"back_{i}.png"
        self.renderer = Renderer(self.positions, self.images)

    def start_game(self):
        game_loop = GameLoop(self.clock, self.event_queue, self.display, self.renderer, self.hitboxes)
        game_loop.start()

    def show_hiscores(self):
        pass
