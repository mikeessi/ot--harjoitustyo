import pygame
from deck.gameloop import GameLoop
from interface.clock import Clock
from interface.eventqueue import EventQueue
from interface.menu import Menu
from interface.renderer import Renderer
from interface.hitboxes import Hitboxes as Hb


WIDTH = 1024
HEIGHT = 768

POSITIONS = {"discard": (900,20),
                "draw": (800,20),
                "empty_draw": (800,20),
                "drag": None,
                "empty_0": (200,20),
                "empty_1": (300,20),
                "empty_2": (400,20),
                "empty_3": (500,20),
                "tableau_0": (100,150),
                "tableau_1": (200,150),
                "tableau_2": (300,150),
                "tableau_3": (400,150),
                "tableau_4": (500,150),
                "tableau_5": (600,150),
                "tableau_6": (700,150)}

IMAGES = {"discard": "empty_discard.png",
        "empty_draw": "empty_draw.png",
        "draw": "back_1.png",
        "empty_0": "empty_0.png",
        "empty_1": "empty_1.png",
        "empty_2": "empty_2.png",
        "empty_3": "empty_3.png",
        "tableau_0": "empty_discard.png",
        "tableau_1": "empty_discard.png",
        "tableau_2": "empty_discard.png",
        "tableau_3": "empty_discard.png",
        "tableau_4": "empty_discard.png",
        "tableau_5": "empty_discard.png",
        "tableau_6": "empty_discard.png"}

CARD_SIZE = (71,96)

def main():

    display = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Solitaire")

    pygame.init()

    clock = Clock()
    hitboxes = Hb(POSITIONS, CARD_SIZE)
    event_queue = EventQueue()
    renderer = Renderer(POSITIONS, IMAGES)
    game_loop = GameLoop(clock, event_queue, display, renderer, hitboxes)
    menu = Menu(game_loop)

    menu.menu.mainloop(display)


if __name__ == "__main__":
    main()
