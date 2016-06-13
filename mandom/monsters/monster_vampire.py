# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# MonsterVampire
#

from mandom.monsters.monster      import Monster
from mandom.monsters.monster_type import MonsterType

class MonsterVampire(Monster):
    def __init__(self):
        super().__init__(MonsterType.vampire, 'Vampire', 4)