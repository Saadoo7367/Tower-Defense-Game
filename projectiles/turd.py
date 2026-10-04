import pygame
from projectiles.projectile import Projectile
import os

class Turd(Projectile):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'projectiles', 'turd.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    def __init__(self, screen, position, enemies, target_enemy, damage):
        super().__init__(name="Turd", damage=damage, speed=6, image=Turd.pic, screen=screen, position=position, enemies=enemies, target_enemy=target_enemy, lifetime=100)
        self.image = pygame.transform.scale(Turd.pic, (20, 20))