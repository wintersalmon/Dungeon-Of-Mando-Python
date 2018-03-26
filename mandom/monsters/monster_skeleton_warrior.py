# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# MonsterSkeletonWarrior
#

from mandom.monsters.monster import Monster
from mandom.monsters.monster_type import MonsterType


class MonsterSkeletonWarrior(Monster):
    def __init__(self):
        super().__init__(MonsterType.skeletonWarrior, 'SkeletonWarrior', 2)
