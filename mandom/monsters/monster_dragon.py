# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# MonsterDragon
#

from mandom.monsters.monster      import Monster
from mandom.monsters.monster_type import MonsterType

class MonsterDragon(Monster):
    def __init__(self):
        super().__init__(MonsterType.dragon, 'Dragon', 9)