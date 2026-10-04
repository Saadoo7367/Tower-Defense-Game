import pygame
import glob
import os
from towers.tower_upgrades.upgrade_info import Upgrade_Info

class Tower:
    assets_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'tower_assets'))
    pngs = glob.glob(os.path.join(assets_dir, '*.png'))
    try:
        pic = pygame.image.load(pngs[0]) if pngs else None
    except Exception:
        pic = None

    def __init__(self, name, footprint_size, screen):
        self.name = name
        self.level = -1
        self.range = Upgrade_Info.get_attribute(self.name, self.level, "range")
        self.image = Upgrade_Info.get_attribute(self.name, self.level, "image")
        self.projectile = Upgrade_Info.get_attribute(self.name, self.level, "projectile")
        self.cost = Upgrade_Info.get_attribute(self.name, 0, "upgrade_cost")
        self.cd = Upgrade_Info.get_attribute(self.name, self.level, "attack_speed")
        self.dmg = Upgrade_Info.get_attribute(self.name, self.level, "damage")
        self.keybind = pygame.K_q #default keybind
        self.footprint_size = footprint_size 
        self.screen = screen
        self.position = (0,0)
        self.enemies_in_range = []
        self.projectiles_alive = []
        self.current_cd = 0 # Initialize current cooldown
        self.total_spent = 0

    def get_Keybind(self):
        return self.keybind
    
    def get_coords(self):
        return (self.image, self.position)
    
    def find_enemy(self, enemies):
        self.enemies_in_range = []
        for enemy in enemies:
            enemy_x, enemy_y = enemy.get_position()
            tower_x, tower_y = self.position

            distance = ((enemy_x - tower_x) ** 2 + (enemy_y - tower_y) ** 2) ** 0.5

            if distance <= self.range:
                self.enemies_in_range.append(enemy)            
               
        return self.enemies_in_range

    def projectile_movement(self):
        for projectile in self.projectiles_alive:
            movement = projectile.move_towards_enemy()
            if projectile.is_alive() == False:
                self.projectiles_alive.remove(projectile)

            elif movement == False:
                self.projectiles_alive.remove(projectile)

            elif not movement == False:
                return movement

    def shoot(self, enemies):
        self.enemies_in_range = self.find_enemy(self.enemies_in_range)

        if len(self.enemies_in_range) > 0:
            target_enemy = self.enemies_in_range[0] # change up the targeting list later

        if len(self.enemies_in_range) == 0:
            return  
        
        if self.current_cd > 0:
            self.current_cd -= 1
            self.projectile_movement()

        else:
            self.current_cd = self.cd  # Reset cooldown
            self.projectiles_alive.append(self.projectile(self.screen, self.position, enemies, target_enemy, self.dmg))            
            self.projectile_movement()

    def upgrade(self):
        if self.level < 5:
            self.level += 1
            cost = Upgrade_Info.get_attribute(self.name, self.level, "upgrade_cost")
            print(f"{self.name} tower upgraded to level {self.level}! spent ${cost}")

            self.total_spent += cost
            self.range = Upgrade_Info.get_attribute(self.name, self.level, "range")
            self.cd = Upgrade_Info.get_attribute(self.name, self.level, "attack_speed")
            self.image = Upgrade_Info.get_attribute(self.name, self.level, "image")
            self.dmg = Upgrade_Info.get_attribute(self.name, self.level, "damage")

        if self.level > 5:
            self.level = 5

    def make_footprint(self):
        footprint_rect = pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(self.position[0], self.position[1], self.footprint_size[0], self.footprint_size[1]))
        return footprint_rect

    def get_cost(self):
        if self.level < 5 and self.level >= 0:
            return Upgrade_Info.get_attribute(self.name, self.level + 1, "upgrade_cost")
        return Upgrade_Info.get_attribute(self.name, self.level, "upgrade_cost")
    
    def get_place_cost(self):
        return self.cost
    
    def get_level(self):
        return self.level
    
    def get_footprint(self):
        return pygame.Rect(self.position[0], self.position[1], self.footprint_size[0], self.footprint_size[1])
    
    def get_total_cost(self):
        return self.total_spent
    
