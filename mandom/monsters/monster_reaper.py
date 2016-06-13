# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# MonsterReaper
#

from mandom.monsters.monster      import Monster
from mandom.monsters.monster_type import MonsterType

class MonsterReaper(Monster):
    def __init__(self):
        super().__init__(MonsterType.reaper, 'Reaper', 6)
