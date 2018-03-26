# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# WeaponHolyGrail
#

from mandom.monsters.monster_type import MonsterType
from mandom.weapons.weapon import Weapon
from mandom.weapons.weapon_type import WeaponType


class WeaponHolyGrail(Weapon):
    slayer_monsters = [MonsterType.skeletonWarrior, MonsterType.vampire, MonsterType.reaper]

    def __init__(self):
        super().__init__(WeaponType.holy_grail, 'HolyGrail', 0, WeaponHolyGrail.slayer_monsters)
