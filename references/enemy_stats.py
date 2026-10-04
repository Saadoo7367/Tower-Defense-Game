from enemies.reg_enemy import Reg_Enemy
from enemies.fast_enemy import Fast_Enemy
from enemies.tank_enemy import Tank_Enemy
from enemies.zombie_enemy import Zombie_Enemy
from enemies.boss_enemy import Boss_Enemy

enemy_type_map = {
    "NORMAL": Reg_Enemy,
    "SPEEDY": Fast_Enemy,
    "TANK": Tank_Enemy,
    "ZOMBIE": Zombie_Enemy,
    "BOSS": Boss_Enemy
}