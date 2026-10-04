import pygame
from towers.tower import Tower

class Thrower(Tower):
    keybind = pygame.K_q #default keybind

    def __init__(self, screen):
        super().__init__(name="Thrower", footprint_size=(60,60), screen=screen)
        self.position = (0,0)
    