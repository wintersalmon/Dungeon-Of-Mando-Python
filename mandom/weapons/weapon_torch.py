# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# WeaponTorch
#

from mandom.weapons.weapon import Weapon
from mandom.weapons.weapon_type import WeaponType
from mandom.monsters.monster_type import MonsterType

class WeaponTorch(Weapon):
    slayer_monsters = [MonsterType.goblin, MonsterType.skeletonWarrior, MonsterType.ork]
    def __init__(self):
        super().__init__(WeaponType.torch, 'Torch', 0, WeaponTorch.slayer_monsters)
