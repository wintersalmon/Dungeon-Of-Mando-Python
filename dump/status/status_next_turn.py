# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusNextTurn
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusNextTurn(Status):
    def __init__(self):
        super().__init__('StatusNextTurn', StatusType.next_turn, StatusType.turn_start, StatusType.challenge_start)
    
    def update(self, dungeon):
        print('StatusNextTurn')
        
        player_in_round = dungeon.round.player_in_round
        if len(player_in_round) > 1:
            return self.success_end_status()
        else:
            return self.failed_end_status()