# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusBattleStart
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusBattleStart(Status):
    def __init__(self):
        super().__init__('StatusBattleStart', StatusType.battle_start, StatusType.battle_execute)
    
    def update(self,dungeon):
        print('StatusBattleStart')
        
        dungeon.battle.reset()
        
        return self.success_end_status()