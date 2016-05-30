# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusGameEnd
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusGameEnd(Status):
    def __init__(self):
        super().__init__('StatusGameEnd', StatusType.game_end, StatusType.none)
    
    def update(dungeon):
        print('StatusGameEnd')
        
        return self.success_end_status()