import os
import pygame
from enemies.enemy import Enemy
from path import Path

class Fast_Enemy(Enemy):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'enemy_assets', 'evil_speedy_enemy.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    def __init__(self, screen):
        super().__init__(health=8, speed=3, image=Fast_Enemy.pic, bounty=20, name="Fast", screen=screen)
        self.position = Path().get_path_points()[0]
        self.current_point_index = 0
        self.reached_end = False
