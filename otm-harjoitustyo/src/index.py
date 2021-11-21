import pygame
from gameloop import GameLoop 
from clock import Clock
from eventqueue import EventQueue
from renderer import Renderer

def main():

    width = 1024
    height = 768

    coordinates = {"discard": (900,20),
                   "draw": (800,20),
                   "empty_draw": (800,20),
                   "drag": None}

    card_size = (71,96)
    

    display = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Card Game")

    clock = Clock()
    event_queue = EventQueue()
    renderer = Renderer(coordinates)
    game_loop = GameLoop(clock, event_queue, display, renderer, coordinates, card_size)
    


    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()