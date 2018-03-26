# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# WeaponArmor
#

from mandom.weapons.weapon import Weapon
from mandom.weapons.weapon_type import WeaponType


class WeaponArmor(Weapon):
    slayer_monsters = []

    def __init__(self):
        super().__init__(WeaponType.armor, 'Armor', 5, WeaponArmor.slayer_monsters)
