from turtle import position
import pygame
from assets import tower_assets
from enemies.enemy import Enemy
import glob
import os


class Projectile:
    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets', 'projectiles', 'turd.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    def __init__(self, name, damage, speed, image, screen, position, enemies, target_enemy, lifetime=100):
        self.lifetime = lifetime 
        self.name = name
        self.damage = damage
        self.speed = speed
        self.image = image
        self.screen = screen
        self.position = position
        self.enemies = enemies
        self.target_enemy = target_enemy 

        if self.image == None:
            self.image = Projectile.pic
        
        self.image = pygame.transform.scale(self.image, (20, 20))

    def move_towards_enemy(self):
        tower_x, tower_y = self.position
        enemy_x, enemy_y = self.target_enemy.get_position()

        direction_x = enemy_x - tower_x
        direction_y = enemy_y - tower_y

        length = (direction_x ** 2 + direction_y ** 2) ** 0.5
        if length != 0:
            direction_x /= length
            direction_y /= length

        #update position
        new_x = tower_x + direction_x * self.speed  
        new_y = tower_y + direction_y * self.speed 
        self.position = (new_x, new_y)

        #draw projectile
        self.screen.blit(self.image, self.position)

        if ((new_x - enemy_x) ** 2 + (new_y - enemy_y) ** 2) ** 0.5 < 5:
            self.target_enemy.take_damage(self.damage)
            if self.name == "Grenade": 
                self.explode()
        
            self.lifetime = 0
            return self.target_enemy

    def is_alive(self):
        self.lifetime -= 1
        if self.lifetime < 0:

            if self.name == "Grenade":
                self.explode()

            return False
        
    def get_dmg(self):
        return self.damage
    
    def upgrade(self, amount):
        self.damage = amount

    def find_enemies(self, range):
        enemies_in_range = []
        for enemy in self.enemies:
            enemy_x, enemy_y = enemy.get_position()
            proj_x, proj_y = self.position

            distance = ((enemy_x - proj_x) ** 2 + (enemy_y - proj_y) ** 2) ** 0.5

            if distance <= range:
                enemies_in_range.append(enemy)            
               
        return enemies_in_range    