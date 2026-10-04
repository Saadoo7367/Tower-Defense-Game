import pygame
from projectiles.projectile import Projectile
import os

class Bullet(Projectile):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'projectiles', 'bullet.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    def __init__(self, screen, position, enemies, target_enemy, damage):
        super().__init__(name="Bullet", damage=damage, speed=8, image=Bullet.pic, screen=screen, position=position, enemies=enemies, target_enemy=target_enemy, lifetime=500)
        self.image = pygame.transform.scale(Bullet.pic, (30, 30))