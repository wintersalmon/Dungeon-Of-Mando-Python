# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# MonsterGoblin
#

from mandom.monsters.monster import Monster
from mandom.monsters.monster_type import MonsterType


class MonsterGoblin(Monster):
    def __init__(self):
        super().__init__(MonsterType.goblin, 'Goblin', 1)
