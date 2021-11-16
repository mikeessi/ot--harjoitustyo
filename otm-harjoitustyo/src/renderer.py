import pygame

class Renderer:

    def render(self, list):
        for object in list:
            object.update()
        pygame.display.flip()
        