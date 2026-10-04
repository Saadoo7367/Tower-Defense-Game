import os
import pygame
from towers.tower_upgrades.upgrade_info import Upgrade_Info

class TowerUpgradeUI:
    pic_location = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'ui_assets', 'tower_upgrade_ui.png'))
    try:
        pic = pygame.image.load(pic_location) 
    except Exception:
        pic = None

    def __init__(self, screen):
        self.screen = screen
        self.upd_ui = pygame.transform.scale(TowerUpgradeUI.pic, (200, 500))
        self.rect = pygame.Rect(323, 205, 156, 80)  # x, y, width, height
        self.sell_rect = pygame.Rect(320, 445, 160, 80)  # x, y, width, height
        

    def display_upgrade_options(self, tower):
        #pygame.draw.rect(self.screen, (0, 0, 0), self.rect)  # Draw the button (green)
        name = tower.name
        lvl = tower.get_level()
        if lvl == 5:
            cost = "MAX"            
            dmg = Upgrade_Info.get_attribute(name, lvl, "damage")
            range = Upgrade_Info.get_attribute(name, lvl, "range")
            fireRate = Upgrade_Info.get_attribute(name, lvl, "attack_speed")
            next_dmg = ""
            next_range = ""
            next_fireRate = ""
            total_spent = tower.get_total_cost()
            tower_lvl = "lvl 5"
        else:            
            cost = Upgrade_Info.get_attribute(name, lvl + 1, "upgrade_cost")
            dmg = Upgrade_Info.get_attribute(name, lvl, "damage")
            range = Upgrade_Info.get_attribute(name, lvl, "range")
            fireRate = Upgrade_Info.get_attribute(name, lvl, "attack_speed")
            next_dmg = " -> " + str(Upgrade_Info.get_attribute(name, lvl + 1, "damage"))
            next_range = " -> " + str(Upgrade_Info.get_attribute(name, lvl + 1, "range"))
            next_fireRate = " -> " + str(Upgrade_Info.get_attribute(name, lvl + 1, "attack_speed"))
            total_spent = tower.get_total_cost()
            tower_lvl = str(lvl)

        range_circle = pygame.draw.circle(self.screen, (102, 178, 255, 100), (tower.position[0]+40, tower.position[1]+40), tower.range)  # Draw the range circle around the tower
        self.screen.blit(self.upd_ui, (300, 0)) # Display the upgrade UI on the right side of the screen

        text_surface = pygame.font.Font(None, 36).render(f"${cost}", True, (255, 255, 50))
        self.screen.blit(text_surface, (300, 0))
        text_surface = pygame.font.Font(None, 30).render(f"DMG: {dmg}{next_dmg}", True, (255, 0, 50))
        self.screen.blit(text_surface, (315, 290))
        text_surface = pygame.font.Font(None, 30).render(f"Range: {range}{next_range}", True, (0, 50, 255))
        self.screen.blit(text_surface, (315, 320))
        text_surface = pygame.font.Font(None, 30).render(f"ROF: {fireRate}{next_fireRate}", True, (0, 255, 50))
        self.screen.blit(text_surface, (315, 350))
        text_surface = pygame.font.Font(None, 28).render(f"Tower Level: {tower_lvl}", True, (0, 0, 0))
        self.screen.blit(text_surface, (313, 380))
        text_surface = pygame.font.Font(None, 28).render(f"Total Spent: ${total_spent}", True, (155, 155, 50))
        self.screen.blit(text_surface, (313, 410))

        return self.rect
    
    def clicked_upgrade(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouse_pos):
            return True
        return False

    def clicked_sell(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.sell_rect.collidepoint(mouse_pos):
            return True
        return False
        