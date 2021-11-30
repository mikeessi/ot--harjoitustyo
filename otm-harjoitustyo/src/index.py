import pygame
from gameloop import GameLoop 
from clock import Clock
from eventqueue import EventQueue
from renderer import Renderer

def main():

    width = 1024
    height = 768

    positions = {"discard": (900,20),
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
    
    images = {"discard": "empty_discard.png",
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

    card_size = (71,96)
    

    display = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Solitaire")

    clock = Clock()
    event_queue = EventQueue()
    renderer = Renderer(positions, images)
    game_loop = GameLoop(clock, event_queue, display, renderer, positions, card_size)
    


    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()