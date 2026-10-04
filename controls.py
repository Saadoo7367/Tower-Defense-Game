import pygame

class Controls:
    def __init__(self, screen):
        self.screen = screen

    def clicked_tower(self, towers):
        mouse_pos = pygame.mouse.get_pos()
        for tower in towers:
            tower_x, tower_y = tower.position
            footprint_width, footprint_height = tower.footprint_size

            if (tower_x <= mouse_pos[0] <= tower_x + footprint_width and
                tower_y <= mouse_pos[1] <= tower_y + footprint_height):
                print("Tower clicked at position:", tower.position)
                return tower
    
        return None