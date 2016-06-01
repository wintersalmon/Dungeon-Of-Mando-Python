# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusTurnExecute
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusTurnExecute(Status):
    def __init__(self):
        super().__init__('StatusTurnExecute', StatusType.turn_execute, StatusType.turn_end)
    
    def update(self, dungeon):
        print('StatusTurnExecute')
        
        # dungeon.turn.turn_action
        # dungeon.turn.turn_player
        # dungeon.turn.turn_draw_monster
        # dungeon.turn.turn_remove_weapon
        
        if dungeon.turn.turn_action != None:
            return self.success_end_status()
        else:
            return self.failed_end_status()