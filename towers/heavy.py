import pygame
from towers.tower import Tower

class Heavy(Tower):
    keybind = pygame.K_r #default keybind
    
    def __init__(self, screen):
        super().__init__(name="Heavy", footprint_size=(100, 100), screen=screen)
        self.position = (0,0)
