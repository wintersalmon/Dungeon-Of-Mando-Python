# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusRoundStart
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusRoundStart(Status):
    def __init__(self):
        super().__init__('StatusRoundStart', StatusType.round_start, StatusType.next_turn)
    
    def update(self, dungeon):
        print('StatusRoundStart')
        
        dungeon.round.reset()
        
        return self.success_end_status()
        
