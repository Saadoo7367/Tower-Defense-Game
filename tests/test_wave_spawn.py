import unittest
import pygame

pygame.init()
pygame.font.init()

from enemies.waves.wave_structure import Wave_Structure
from enemies.reg_enemy import Reg_Enemy
from enemies.fast_enemy import Fast_Enemy
from enemies.tank_enemy import Tank_Enemy


class TestWaveSpawn(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.Surface((500, 500))
        self.ws = Wave_Structure(self.screen)
        self.ws.read("easy")

    def test_read_builds_nested_waves(self):
        self.assertIn("total_chunks", self.ws.enemy_groups[0])
        self.assertIn(1, self.ws.enemy_groups[0])
        self.assertEqual(self.ws.enemy_groups[0][1]["enemy_type"], Reg_Enemy)
        self.assertEqual(self.ws.enemy_groups[0][1]["enemy_count"], 3)
        self.assertEqual(self.ws.enemy_groups[1]["total_chunks"], 2)
        self.assertEqual(self.ws.enemy_groups[1][1]["enemy_type"], Fast_Enemy)
        self.assertEqual(self.ws.enemy_groups[1][2]["enemy_type"], Reg_Enemy)

    def test_first_wave_chunk_is_armed_after_read(self):
        self.assertEqual(self.ws.wave, 1)
        self.assertEqual(self.ws.current_chunk, 1)
        self.assertEqual(self.ws.enemy_reserves, 3)
        self.assertEqual(self.ws.enemy_btwn, 50)

    def test_spawns_all_enemies_across_waves(self):
        counter = 500
        spawned = []
        # Enough frames for: delay + wave1(3) + delay + wave2(5+2) + delay + wave3(1)
        for _ in range(20_000):
            enemy_cls, counter = self.ws.attempt_spawn(counter)
            if enemy_cls is not None:
                spawned.append(enemy_cls)
            if self.ws.wave > self.ws.last_wave and self.ws.enemy_reserves == 0:
                break
            # Must never freeze on the broken "glory" timer
            self.assertLess(counter, 1_000_000)

        self.assertEqual(len(spawned), 3 + 5 + 2 + 1)
        self.assertEqual(spawned.count(Reg_Enemy), 3 + 2)
        self.assertEqual(spawned.count(Fast_Enemy), 5)
        self.assertEqual(spawned.count(Tank_Enemy), 1)


if __name__ == "__main__":
    unittest.main()
