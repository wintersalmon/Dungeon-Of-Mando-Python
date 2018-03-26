# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# MonsterGolam
#

from mandom.monsters.monster import Monster
from mandom.monsters.monster_type import MonsterType


class MonsterGolam(Monster):
    def __init__(self):
        super().__init__(MonsterType.golam, 'Golam', 5)
