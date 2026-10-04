import pygame
import os
from projectiles.turd import Turd
from projectiles.sword import Sword
from projectiles.grenade import Grenade
from projectiles.bullet import Bullet

class Upgrade_Info:
    projectiles = {
        "Turd": Turd,
        "Sword": Sword,
        "Grenade": Grenade,
        "Bullet": Bullet
    }
    towers = {
            "Thrower": {
                "range": [],
                "damage": [],
                "attack_speed": [],
                "upgrade_cost": [],
                "image": [],
                "projectile": []
                },
            "Swordsman": {
                "range": [],
                "damage": [],
                "attack_speed": [],
                "upgrade_cost": [],
                "image": [],
                "projectile": []
                },
            "Grenadier": {
                "range": [],
                "damage": [],
                "attack_speed": [],
                "upgrade_cost": [],
                "image": [],
                "projectile": []
                },
            "Heavy": {
                "range": [],
                "damage": [],
                "attack_speed": [],
                "upgrade_cost": [],
                "image": [],
                "projectile": []
                }
        }

    def read():
        for tower in Upgrade_Info.towers:
            with open(f'towers/tower_upgrades/{tower}.csv', 'r') as file:
                next(file)  # Skip header
                for line in file:
                    level, range, damage, attack_speed, upgrade_cost, image, projectile = line.strip().split(',')

                    pic_location = os.path.normpath(os.path.join(f'assets/tower_assets/{image}'))
                    try:
                        pic = pygame.image.load(pic_location) 
                    except Exception:
                        print(f"yo where he at? U know? {tower} {image}")
                        pygame.quit()
                        
                    pic = pygame.transform.scale(pic, (75, 75))

                    projectile_class = Upgrade_Info.projectiles[projectile]

                    Upgrade_Info.towers[tower]["range"].append(int(range))
                    Upgrade_Info.towers[tower]["damage"].append(int(damage))
                    Upgrade_Info.towers[tower]["attack_speed"].append(int(attack_speed))
                    Upgrade_Info.towers[tower]["upgrade_cost"].append(int(upgrade_cost))
                    Upgrade_Info.towers[tower]["projectile"].append(projectile_class)                  
                    Upgrade_Info.towers[tower]["image"].append(pic)


    def get_attribute(tower_name, level, attribute):
     return Upgrade_Info.towers[tower_name][attribute][level]
 
        