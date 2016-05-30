# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusNextRound
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusNextRound(Status):
    def __init__(self):
        super().__init__('StatusNextRound', StatusType.next_round, StatusType.round_start, StatusType.game_end)
    
    def update(dungeon):
        print('StatusNextRound')
        
        players = dungeon.player_list()
        
        no_winner = True        
        for player in players:
            if player.victory_point() == 2:
                has_winner = False
        
        surviver_count = 0
        for player in players:
            if player.life_point() > 0:
                surviver_count += 1
                
        if no_winner or surviver_count > 1:
            return self.success_end_status()
        else:
            return self.failed_end_status()
        