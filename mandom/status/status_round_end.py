# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusRoundEnd
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusRoundEnd(Status):
    def __init__(self):
        super().__init__('StatusRoundEnd', StatusType.round_end, StatusType.next_round)
    
    def update(dungeon):
        print('StatusRoundEnd')
        
        player_in_round = dungeon.round.player_in_round
        challenger = player_in_round[0] if len(player_in_round) > 0 else None
        dungeon.round.last_challenger = challenger
        
        return self.success_end_status()