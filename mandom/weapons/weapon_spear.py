# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# WeaponSpear
#

from mandom.monsters.monster_type import MonsterType
from mandom.weapons.weapon import Weapon
from mandom.weapons.weapon_type import WeaponType


class WeaponSpear(Weapon):
    slayer_monsters = [MonsterType.dragon]

    def __init__(self):
        super().__init__(WeaponType.spear, 'Spear', 0, WeaponSpear.slayer_monsters)
