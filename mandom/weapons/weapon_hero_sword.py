# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# WeaponHeroSword
#

from mandom.weapons.weapon import Weapon
from mandom.weapons.weapon_type import WeaponType
from mandom.monsters.monster_type import MonsterType

class WeaponHeroSword(Weapon):
    slayer_monsters = []
    def __init__(self):
        super().__init__(WeaponType.hero_sword, 'Hero Sword', 0, WeaponHeroSword.slayer_monsters)
        
    def declare_target_monster(self,monster_code):
        self.reset_slayer_monster()
        self.add_slayer_monster(monster_code)