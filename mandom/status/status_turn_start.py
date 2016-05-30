# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusTurnStart
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusTurnStart(Status):
    def __init__(self):
        super().__init__('StatusTurnStart', StatusType.turn_start, StatusType.turn_end)
    
    def update(dungeon):
        print('StatusTurnStart')
        
        dungeon.turn.reset()
        
        return self.success_end_status()
        