import pygame
from path import Path
import os

class Enemy:
    # load first PNG from project's assets/enemy_assets folder (relative to this file)
    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'enemy_assets', 'evil_enemy.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    def __init__(self, health, speed, image, bounty, name, screen):
        self.health = health
        self.speed = speed
        self.image = image
        self.bounty = bounty
        self.name = name
        self.path = Path().get_enemy_path()
        self.position = self.path[0][0] # Start at the beginning of the path
        self.current_point_index = 0
        self.reached_end = False
        self.screen = screen


    def move(self):
        if not self.speed:
            raise NotImplementedError("Move method not implemented for this enemy type.")
            return False
        
        if self.image == None:
            self.image = Enemy.pic
        
        self.image = pygame.transform.scale(self.image, (50, 50))

        if self.health <= 0:
            return False

        if self.current_point_index == len(self.path): #checks if enemy reached end of path
            self.reached_end = True
            damage_dealt = self.health
            end_info = (self.reached_end, damage_dealt)
            return end_info

        next_pos = self.path[self.current_point_index] #cool variable

        if self.position == self.path[self.current_point_index]: #if the position is at the current point, move to next point
            next_pos = self.path[self.current_point_index + 1]
        
        next_pos_x, next_pos_y = next_pos
        current_pos_x, current_pos_y = self.position

        #calculate direction
        direction_x = next_pos_x - current_pos_x
        direction_y = next_pos_y - current_pos_y

        #why r we doing this, does this not calculate next position as well?
        length = (direction_x ** 2 + direction_y ** 2) ** 0.5
        if length != 0:
            direction_x /= length
            direction_y /= length

        #update position
        new_x = current_pos_x + direction_x * self.speed  
        new_y = current_pos_y + direction_y * self.speed 
        self.position = (new_x, new_y)

        self.screen.blit(self.image, self.position)

        if (abs(new_x - next_pos_x) <= self.speed) and (abs(new_y - next_pos_y) <= self.speed):
            self.current_point_index += 1
            self.position = next_pos

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            return self
        else:
            return self

    def get_position(self):
        return self.position
    
    def get_bounty(self):
        return self.bounty
    
    def get_name(self):
        return self.name