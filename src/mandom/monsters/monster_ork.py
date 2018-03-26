# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# MonsterOrk
#

from mandom.monsters.monster import Monster
from mandom.monsters.monster_type import MonsterType


class MonsterOrk(Monster):
    def __init__(self):
        super().__init__(MonsterType.ork, 'Ork', 3)
