import pygame

class Path:
    def __init__(self):
        self.path_points = []
        self.rects = [
            (260, 0, 75, 160),
            (83, 87, 177, 75),
            (83, 87, 75, 150),
            (83, 217, 365, 75),
            (380, 217, 75, 283),
            (380, 500, 0, 0)  # Endpoint
        ]
        self.enemy_path = [
            (295, 0),
            (295, 100),
            (100, 100),
            (100, 220),
            (390, 220),
            (390, 500)
        ]
        for point in self.rects:
            self.path_points.append(point[0:2])
    
    def get_path_points(self):
        return self.path_points

    def get_rects(self):
        return self.rects
    
    def get_enemy_path(self):
        return self.enemy_path
    
    def draw_rectangles(self, screen):
        for rect in self.rects:
            pygame.draw.rect(screen, (255, 0, 0), rect)  # Draw red rectangles for debugging