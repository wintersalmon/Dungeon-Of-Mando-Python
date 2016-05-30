# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusGameStart
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusGameStart(Status):
    def __init__(self):
        super().__init__('StatusGameStart', StatusType.game_start, StatusType.next_round)
    
    def update(dungeon):
        
        print('StatusGameStart')
        
        players = dungeon.player_list()
        for player in players:
            player.reset()
        
        return self.success_end_status()