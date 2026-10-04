import pygame
from assets import tower_assets
from towers.thrower import Thrower
from towers.swordsman import Swordsman 
from towers.grenadier import Grenadier
from towers.heavy import Heavy
from path import Path

class Tower_Summoner():
    def __init__(self, towers, screen):
        self.screen = screen
        self.tower_types = {
            Thrower.keybind: Thrower,
            Grenadier.keybind: Grenadier,
            Heavy.keybind: Heavy,
            Swordsman.keybind: Swordsman
        }
        self.towers = towers

    def place_tower(self, keybind):
        path = Path()
        path_rects = path.get_rects()
        tower_footprints = [tower.get_footprint() for tower in self.towers]

        for k, v in self.tower_types.items():
            if k == keybind:
                chosen_tower = v(self.screen) #make object
                break
        
        if chosen_tower:
            tower_instance = chosen_tower 

            mouse_pos = pygame.mouse.get_pos()

            if any(pygame.Rect(rect).collidepoint(mouse_pos) for rect in path_rects):
                return None  # Can't place tower on the path
            
            if any(pygame.Rect(rect).collidepoint(mouse_pos) for rect in tower_footprints):
                return None  # Can't place tower on top of another tower
            
            
            tower_instance.position = (mouse_pos[0] - 50, mouse_pos[1] - 50)
            tower_instance.screen.blit(tower_instance.image, mouse_pos)
            tower_instance.make_footprint()
            chosen_tower.upgrade()

            return tower_instance
        return None