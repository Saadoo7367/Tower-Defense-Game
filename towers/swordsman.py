import pygame
from towers.tower import Tower

class Swordsman(Tower):
    keybind = pygame.K_e #default keybind

    def __init__(self, screen):
        super().__init__(name="Swordsman", footprint_size=(75, 75), screen=screen)
        self.position = (0,0)