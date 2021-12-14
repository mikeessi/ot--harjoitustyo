import pygame_menu

class Menu:

    def __init__(self, game_loop):
        self.game_loop = game_loop
        self.menu = pygame_menu.Menu("Solitaire",800,600,theme = pygame_menu.themes.THEME_DARK)
        self.menu.add.button("New game", self.start_game)
        self.menu.add.selector("Cardback :", [("TODO",1)],onchange=self.set_cardback)
        self.menu.add.button("Hiscores", self.show_hiscores)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)


    def set_cardback(self, i,j):
        pass

    def start_game(self):
        self.game_loop.restart()

    def show_hiscores(self):
        pass
