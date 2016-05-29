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

    def DeclareSlayerableMonster(self,monsterName):
        self.__can_slayer_slayer_monsters.clear()
        self.__can_slayer_slayer_monsters.append(monsterName)
