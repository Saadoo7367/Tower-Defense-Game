import pygame
from enemies.reg_enemy import Reg_Enemy
from enemies.fast_enemy import Fast_Enemy
from enemies.tank_enemy import Tank_Enemy
from enemies.zombie_enemy import Zombie_Enemy
from enemies.boss_enemy import Boss_Enemy



class Wave_Structure():
    def __init__(self, screen):
        self.screen = screen
        self.wave = 1
        self.current_chunk = 0
        self.last_wave = 10
        self.enemy_groups = []
        self.enemies = []
        self.enemy_reserves = 0
        self.enemy_btwn = 0
        self.enemy_type_map = {
            "NORMAL": Reg_Enemy(self.screen),
            "SPEEDY": Fast_Enemy(self.screen),
            "TANK": Tank_Enemy(self.screen),
            "ZOMBIE": Zombie_Enemy(self.screen),
            "BOSS": Boss_Enemy(self.screen)
        }

    def current_wave_display(self):
        text_surface = pygame.font.Font(None, 36).render(f"wave:{self.wave}", True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 50))

        return self.wave

    
    """ ADDED - helper method to get next info"""
    def get_next_enemy_chunk(self):
        if self.wave <= self.last_wave:
            self.enemy_reserves = self.enemy_groups[self.wave - 1]["chunks"][self.current_chunk]["enemy_count"]
            self.enemy_btwn = self.enemy_groups[self.wave - 1]["chunks"][self.current_chunk]["time_between"]
        else:
            self.enemy_reserves = 0
            self.enemy_btwn = 500
            

    def attempt_spawn(self, counter):
        spawned_enemy = None
        counter -= 1
        if counter <= 0:
            print("Counter reached zero, attempting to spawn enemy.")
            # Spawn an enemy
            if self.enemy_reserves > 0:
                print(f"Wave {self.wave}, Chunk {self.current_chunk}: Spawning enemy. Remaining enemies in chunk: {self.enemy_reserves}")
                
                spawned_enemy = self.enemy_groups[self.wave - 1]["chunks"][self.current_chunk]["enemy_type"] 
                #spawned_enemy = self.enemy_type_map["NORMAL"] #for now, just spawn normal enemies
                counter = self.enemy_btwn
                self.enemy_reserves -= 1

            else:  # or try to advance to next enemy chunk
                print("No more enemies in this chunk. Attempting to advance to next chunk.")

                if self.current_chunk < self.enemy_groups[self.wave - 1]["total_chunks"]: 
                    self.current_chunk += 1
                    self.get_next_enemy_chunk()
                    

                else:
                    counter = 500 # Wave time btwn, its like 5secs
                    self.current_chunk = 1
                    self.wave += 1
            
            # Handle next wave            
            if len(self.enemies) == 0:

                if self.wave-1 > self.last_wave:
                    return(None, 0)
                else:
                    counter = 5
        
        return (spawned_enemy, counter)
        

    """ ADDED - int conversion """
    def read(self, difficulty):
        in_header = True
        all_chunks = []
        with open(f"enemies/waves/waves_{difficulty}_new.csv", mode="r") as file:
            for row in file:
                if in_header == True:
                    in_header = False
                    continue
                #--------------------------------Enemy Group Maker----------------------------------#
                wave_num, current_chunk, total_chunks, enemy_type, enemy_count, time_between = row.strip().split(',')

                wave_num = int(wave_num)
                current_chunk = int(current_chunk)
                total_chunks = int(total_chunks)
                enemy_type = self.enemy_type_map[enemy_type]
                enemy_count = int(enemy_count)
                time_between = int(time_between)

                chunk = {
                    "wave_num": wave_num,
                    "current_chunk": current_chunk,
                    "total_chunks": total_chunks,
                    "enemy_type": enemy_type,
                    "enemy_count": enemy_count,
                    "time_between": time_between
                }

                all_chunks.append(chunk)
                #-----------------------------------------------------------------------------------#
        prev_wave_num = 0
        this_wave_chunks = []
        for chunk in all_chunks:
            wave_num = chunk["wave_num"]
            current_chunk = chunk["current_chunk"]
            total_chunks = chunk["total_chunks"]

            # Ensure the enemy_groups list has enough waves
            if prev_wave_num == wave_num:
                this_wave_chunks.append(chunk)

            #once the wave has changed, add the previous wave's chunks to the wave_info library
            else:
                if prev_wave_num != 0:
                    wave_info = {
                        "total_chunks": len(this_wave_chunks),
                        "chunks": this_wave_chunks
                    }
                    self.enemy_groups.append(wave_info)

            prev_wave_num = wave_num

        #preset reserves and btwn for first wave
        self.get_next_enemy_chunk()

        


