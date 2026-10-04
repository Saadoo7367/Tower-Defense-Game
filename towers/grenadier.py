import pygame
from towers.tower import Tower

class Grenadier(Tower):
    keybind = pygame.K_w

    def __init__(self, screen):
        super().__init__(name="Grenadier", footprint_size=(100, 100), screen=screen)
        self.position = (0,0)

        
