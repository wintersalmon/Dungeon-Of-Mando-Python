# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusTurnEnd
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusTurnEnd(Status):
    def __init__(self):
        super().__init__('StatusTurnEnd', StatusType.turn_end, StatusType.next_turn)
    
    def update(self, dungeon):
        print('StatusTurnEnd')
        
        player_in_round = dungeon.round.player_in_round
        cur_turn_player = dungeon.turn.turn_player
        if cur_turn_player == player_in_round[0]:
            player = player_in_round.pop(0)
            player_in_round.append(player)
            
        return self.success_end_status()