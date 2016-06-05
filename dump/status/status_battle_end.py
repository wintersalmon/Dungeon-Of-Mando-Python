# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusBattleEnd
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType
from mandom.dungeon import Dungeon

class StatusBattleEnd(Status):
    def __init__(self):
        super().__init__('StatusBattleEnd', StatusType.battle_end, StatusType.next_battle)
    
    def update(self,dungeon):
        print('StatusBattleEnd')
        
        monster = dungeon.battle.battle_monster
        dungeon.battle.monster_in_dungeon.remove(monster)
        
        return self.success_end_status()
