# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# WeaponShield
#

from mandom.weapons.weapon import Weapon
from mandom.weapons.weapon_type import WeaponType


class WeaponShield(Weapon):
    slayer_monsters = []

    def __init__(self):
        super().__init__(WeaponType.shield, 'Shield', 3, WeaponShield.slayer_monsters)
