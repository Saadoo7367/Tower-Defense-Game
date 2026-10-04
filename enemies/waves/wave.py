class Wave:
    def __init__(self, wave_info):
        self.wave_info = wave_info
        self.wave_num = 0
        self.list_of_enemies = []

    def set_wave_info(self):
        self.wave_num = self.wave_info["wave_num"]
        #keep repeating until wave num is changed
        """
        self.wave_num = self.wave_info["wave_num"]
        self.normal_cnt = self.wave_info["normal_cnt"]
        self.normal_time_btwn = self.wave_info["normal_time_btwn"]
        self.speedy_cnt = self.wave_info["speedy_cnt"]
        self.speedy_time_btwn = self.wave_info["speedy_time_btwn"]
        self.tank_cnt = self.wave_info["tank_cnt"]
        self.tank_time_btwn = self.wave_info["tank_time_btwn"]        
        self.zombie_cnt = self.wave_info["zombie_cnt"]
        self.zombie_time_btwn = self.wave_info["zombie_time_btwn"]    
        self.boss = self.wave_info["boss"]
        self.boss_time_btwn = self.wave_info["boss_time_btwn"]
        """

    def set_enemy_grouping_info(self, enemy_type, enemy_count, time_between):
        chunk = {
            "enemy_type": enemy_type,
            "enemy_count": enemy_count,
            "time_between": time_between
        }

        return chunk

    def get_enemy_type_info(self, enemy_type):
        if enemy_type == "NORMAL":
            return (self.normal_cnt, self.normal_time_btwn)
        elif enemy_type == "SPEEDY":
            return (self.speedy_cnt, self.speedy_time_btwn)
        elif enemy_type == "TANK":
            return (self.tank_cnt, self.tank_time_btwn)
        elif enemy_type == "ZOMBIE":
            return (self.zombie_cnt, self.zombie_time_btwn)
        elif enemy_type == "BOSS":
            return (self.boss, self.boss_time_btwn)
