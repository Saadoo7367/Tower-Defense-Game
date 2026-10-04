import pygame
from projectiles.projectile import Projectile
import os

class Sword(Projectile):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'projectiles', 'sword.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    def __init__(self, screen, position, enemies, target_enemy, damage):
        super().__init__(name="Sword", damage=damage, speed=6, image=Sword.pic, screen=screen, position=position, enemies=enemies, target_enemy=target_enemy, lifetime=100)
        self.image = pygame.transform.scale(Sword.pic, (40, 40))