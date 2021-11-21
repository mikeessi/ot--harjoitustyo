import pygame

class Renderer:

    def render(self, list):
        for object in list:
            if object:
                object.update()
        pygame.display.flip()
        