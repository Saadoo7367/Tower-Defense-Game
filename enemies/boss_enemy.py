import pygame
from enemies.enemy import Enemy
import os
from path import Path

class Boss_Enemy(Enemy):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'enemy_assets', 'evil_boss_enemy.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None


    def __init__(self, screen):
        super().__init__(health=5000, speed=0.1, image=Boss_Enemy.pic, bounty=5000, name="Boss", screen=screen)
        self.position = Path().get_path_points()[0]
        self.current_point_index = 0
        self.reached_end = False
