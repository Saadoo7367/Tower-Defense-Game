# import pygame package
import pygame
from path import Path
from controls import Controls
from towers.tower import Tower
from towers.tower_summoner import Tower_Summoner
from player_ui import PlayerUI
from enemies.waves.wave_structure import Wave_Structure
from towers.tower_upgrade_ui import TowerUpgradeUI
from towers.tower_upgrades.upgrade_info import Upgrade_Info
from references.enemy_stats import enemy_type_map
# initializing imported module

def reset_game():
    global is_alive, money, enemies, towers, ws, counter, boss_died, display_upgrade, base_hp, curr_wave_bonus, wave_bonus_increment
    ui.current_health = ui.max_health
    money = 500
    enemies.clear()
    towers.clear()
    ws.wave = 1
    counter = 500
    is_alive = True
    boss_died = False
    display_upgrade = False
    base_hp = ui.max_health
    curr_wave_bonus = orig_wave_bonus
    wave_bonus_increment = 120
    print("Game reset! Good luck on the next run!")

pygame.init()
# displaying a window of height
# 500 and width 400
screen = pygame.display.set_mode((500, 500))

# Setting name for window
pygame.display.set_caption('Tower Defense game')

# creating a bool value which checks 
# if game is running
running = True

bg_image = pygame.image.load("assets/ui_assets/map.png")
path_image = pygame.image.load("assets/ui_assets/path.png")
screen.blit(bg_image, (0,0))

ui = PlayerUI(100, screen)

path = Path()
path_points = path.get_path_points()

ws = Wave_Structure(screen)

ctrls = Controls(screen)

tower_upg_ui = TowerUpgradeUI(screen)  # Initialize with None, will set tower later when a tower is clicked
display_upgrade = False

Upgrade_Info.read()  # Load upgrade info from CSV files

enemies = []

counter = 500
is_alive = True
towers = []
clicked_tower = None
last_clicked_tower = None

money = 500    

wave_over = True

started = False

boss_died = False

orig_wave_bonus = 0
curr_wave_bonus = orig_wave_bonus
wave_bonus_increment = 120
previous_wave = 0

ts = Tower_Summoner(towers, screen)

clock = pygame.time.Clock()  # Create a clock object to control the frame rate
# Game loop
# keep game running till running is true
while running:
    # Check for event if user has pushed 
    # any event in queue
    if started:
        wave = ws.current_wave_display()
        
        if wave != previous_wave:
            previous_wave = wave
            money += curr_wave_bonus
            print(f"Wave {wave} started! You earned ${curr_wave_bonus} for completing the previous wave.")
            curr_wave_bonus += wave_bonus_increment
            wave_bonus_increment = int(wave_bonus_increment * 1.1)

        if is_alive == True:
            spawned_enemy, counter = ws.attempt_spawn(counter)
            if spawned_enemy:
                enemies.append(spawned_enemy)  # For now, just spawn normal enemies
       

        for enemy in enemies:
            if enemy.move():
                damage = enemy.health
                base_hp = ui.take_damage(damage)
                money += enemy.get_bounty()

                if enemy.get_name() == "Boss" and base_hp > 0:
                    boss_died = True

                enemies.remove(enemy)
                if base_hp <= 0:
                    max_enemies = 0
                    is_alive = False

                    for enemy_alive in enemies:
                        enemies.remove(enemy_alive)
                            
            if enemy.health <= 0:
                if enemy.get_name() == "Boss":
                    boss_died = True     

                money += enemy.get_bounty()
                enemies.remove(enemy)   

        for tower in towers:
            if len(tower.find_enemy(enemies)) > 0:
                enemy_shot = tower.shoot(enemies)
            
                if enemy_shot:
                    if enemy_shot.health <= 0:
                        enemies = enemies.remove(enemy_shot)
                        tower.find_enemy(enemies)
                    
            pos = tower.get_coords()
            screen.blit(pos[0], pos[1])


    for event in pygame.event.get():        
        if pygame.mouse.get_pressed()[0]:
            #----------------------------------------Upgrading Towers----------------------------------------#
            clicked_tower = ctrls.clicked_tower(towers)
            if tower_upg_ui.clicked_upgrade() and display_upgrade:
                lvl = last_clicked_tower.get_level()
                cost = last_clicked_tower.get_cost()
                print(f"Upgrade cost: {cost}, Player money: {money}, Tower level: {lvl}")
                if money >= cost and lvl < 5:  # Check if player has enough money for upgrade
                    last_clicked_tower.upgrade()
                    money -= cost  # Deduct upgrade cost, adjust as needed  

            elif tower_upg_ui.clicked_sell() and display_upgrade:
                sell_value = (last_clicked_tower.get_total_cost() * 0.7)
                money += sell_value  # Add sell value to player's money
                towers.remove(last_clicked_tower)  # Remove tower from the game
                display_upgrade = False  # Hide upgrade UI after selling      
                print(f"Tower sold for ${sell_value}. R.I.P")  # Print sell value, adjust as needed

            else:
                if display_upgrade == True:
                    display_upgrade = False if clicked_tower else False
                else:
                    display_upgrade = True if clicked_tower else False
                last_clicked_tower = clicked_tower
            
            #--------------------------------------- try again Button ---------------------------------------#
            if ui.clicked_again_button() and not is_alive:
                reset_game()
                # Reset game state for a new game   

            if not started:
                #----------------------------------------  Play  Button  ----------------------------------------#
                if ui.clicked_play_button():
                    if ui.difficulty is None:
                        print("Pick a difficulty before pressing Play.")
                    else:
                        started = True
                        reset_game()  # Reset game state when play button is clicked
                        ws.read(ui.difficulty)  # Load wave info based on selected difficulty
                #---------------------------------------- Diff Selection ----------------------------------------#
                difficulty = ui.clicked_difficulty()
                if difficulty:
                    print(f"Difficulty selected: {difficulty}")         

        if event.type == pygame.KEYDOWN:
            if started:
                if event.key == pygame.K_q:
                    new_tower = ts.place_tower(pygame.K_q)
                    if new_tower != None: 
                        cost = new_tower.get_place_cost()
                        if money >= cost:
                            towers.append(new_tower)
                            money -= new_tower.get_place_cost()
                        else:
                            print("Not enough money to place tower.")

                if event.key == pygame.K_w:
                    new_tower = ts.place_tower(pygame.K_w)
                    if new_tower != None: 
                        cost = new_tower.get_place_cost()
                        if money >= cost:
                            towers.append(new_tower)
                            money -= new_tower.get_place_cost()
                        else:
                            print("Not enough money to place tower.")

                if event.key == pygame.K_e:
                    new_tower = ts.place_tower(pygame.K_e)
                    if new_tower != None: 
                        cost = new_tower.get_place_cost()
                        if money >= cost:
                            towers.append(new_tower)
                            money -= new_tower.get_place_cost()
                        else:
                            print("Not enough money to place tower.")

                if event.key == pygame.K_r:
                    new_tower = ts.place_tower(pygame.K_r)
                    if new_tower != None: 
                        cost = new_tower.get_place_cost()
                        if money >= cost:
                            towers.append(new_tower)
                            money -= new_tower.get_place_cost()
                        else:
                            print("Not enough money to place tower.")

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False

    clock.tick(100)

    pygame.display.update()

    screen.blit(bg_image, (0, 0))
    path.draw_rectangles(screen)

    if started:        
        if display_upgrade:
            tower_upg_ui.display_upgrade_options(last_clicked_tower)
            
        ui.draw_health_bar()
        text_surface = pygame.font.Font(None, 36).render(f"${money}", True, (255, 255, 50))
        screen.blit(text_surface, (120, 50))
        ws.current_wave_display()

        if is_alive == False:
            ui.display_lose_message()

        if boss_died:
            ui.display_win_message()

    else:
        ui.draw_play_button()
        ui.difficulty_selection()
    
