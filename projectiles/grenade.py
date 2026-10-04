import pygame
from projectiles.projectile import Projectile
import os

class Grenade(Projectile):

    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'projectiles', 'grenade.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    explosion_pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'projectiles', 'explosion.png'))
    try:
        explosion_pic = pygame.image.load(explosion_pic_location) 
    except Exception:
        explosion_pic = None

    def __init__(self, screen, position, enemies, target_enemy, damage):
        super().__init__(name="Grenade", speed=7.8, image=Grenade.pic, screen=screen, position=position, enemies=enemies, target_enemy=target_enemy, damage=damage, lifetime=120)
        self.image = pygame.transform.scale(Grenade.pic, (30, 30))
    
    def explode(self):
        size = (60, 60)
        self.position = (self.position[0], self.position[1])
        explosion_image = pygame.transform.scale(Grenade.explosion_pic, size)

        pygame.draw.circle(self.screen, (102, 178, 255, 100), self.position, size[0])  # Draw the range circle around the tower
        self.screen.blit(explosion_image, self.position)

        enemies = self.find_enemies(size[0])

        for enemy in enemies:
                enemy.take_damage(self.damage)    